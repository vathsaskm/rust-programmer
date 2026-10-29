#!/usr/bin/env python3
"""Validate distributable skill packages without printing sensitive matches."""

import argparse
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit


PACKAGE_NAMES = ("rust-engineer", "rust-skills")
EXCLUDED = {".git", "dist", "audit-private", "__pycache__", ".venv"}
CONTACT = re.compile(r"[A-Za-z0-9_.+%-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})")
HOME_PATH = re.compile(r"(?:/Users/|/home/)[A-Za-z0-9_.-]+/")
WINDOWS_HOME = re.compile(r"[A-Za-z]:\\Users\\[A-Za-z0-9_.-]+\\")
AUTH_URL = re.compile(r"(?:https?|postgres(?:ql)?|mysql|redis)://[^\s/:'\"]+:[^\s/@'\"]+@")
LINK = re.compile(r"(?<!!)\[[^\]\n]*\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)")
ALLOWED_EMAIL_DOMAINS = {"example.com", "example.org", "example.net", "users.noreply.github.com"}
ALLOWED_SUFFIXES = {".md", ".yaml", ".yml", ".py"}


def files_in(root):
    for path in sorted(root.rglob("*")):
        if any(part in EXCLUDED for part in path.relative_to(root).parts):
            continue
        yield path


def inspect_text(path, content, errors):
    for number, line in enumerate(content.splitlines(), 1):
        if HOME_PATH.search(line) or WINDOWS_HOME.search(line):
            errors.append(f"{path.name}:{number}: machine-specific home path")
        if AUTH_URL.search(line):
            errors.append(f"{path.name}:{number}: URL containing credentials")
        for match in CONTACT.finditer(line):
            domain = match.group(1).lower()
            if domain not in ALLOWED_EMAIL_DOMAINS:
                errors.append(f"{path.name}:{number}: non-example contact address")


def inspect_links(path, content, boundary, errors):
    in_fence = False
    for number, line in enumerate(content.splitlines(), 1):
        if line.lstrip().startswith(("```", "~~~")):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        line = re.sub(r"(`+).*?\1", "", line)
        for match in LINK.finditer(line):
            target = unquote(match.group(1).strip("<>"))
            if urlsplit(target).scheme or target.startswith("#"):
                continue
            resolved = (path.parent / target.split("#", 1)[0]).resolve()
            if not resolved.is_relative_to(boundary.resolve()):
                errors.append(f"{path.name}:{number}: reference leaves package")
            elif not resolved.exists():
                errors.append(f"{path.name}:{number}: missing local reference")


def inspect_package(root, errors):
    name = root.name
    if name not in PACKAGE_NAMES:
        errors.append("Unrecognized package name")
        return
    required = [root / "SKILL.md", root / "LICENSE"]
    if name == "rust-engineer":
        required += [root / "agents/openai.yaml", root / "references/official-rust.md"]
    for path in required:
        if not path.is_file():
            errors.append(f"{name}: missing required file {path.name}")
    manifest = root / "SKILL.md"
    if manifest.is_file():
        content = manifest.read_text(encoding="utf-8")
        frontmatter = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", content, re.S)
        if not frontmatter or not re.search(rf"^name: {re.escape(name)}$", frontmatter[1], re.M):
            errors.append(f"{name}: invalid manifest name or frontmatter")
        if not frontmatter or not re.search(r"^description:\s*\S", frontmatter[1], re.M):
            errors.append(f"{name}: missing description")
    peer = next(item for item in PACKAGE_NAMES if item != name)
    for path in files_in(root):
        if path.is_symlink():
            errors.append(f"{name}: symlink is not distributable")
            continue
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8")
        if peer in content.lower():
            errors.append(f"{name}/{path.name}: cross-package reference")
        if path.suffix == ".md":
            inspect_links(path, content, root, errors)
    if name == "rust-skills":
        rules = list((root / "rules").glob("*.md"))
        categories = Counter(path.name.split("-", 1)[0] for path in rules)
        if len(rules) != 265 or len(categories) != 26:
            errors.append("rust-skills: expected 265 rules across 26 categories")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", type=Path, help="Validate one independently extracted package")
    args = parser.parse_args()
    root = args.package.resolve() if args.package else Path(__file__).resolve().parents[1]
    errors = []
    count = 0
    for path in files_in(root):
        if path.is_symlink():
            errors.append(f"{path.name}: symlink is not distributable")
            continue
        if not path.is_file():
            continue
        count += 1
        if path.name not in {"LICENSE", ".gitignore"} and path.suffix not in ALLOWED_SUFFIXES:
            errors.append(f"{path.name}: unexpected file type")
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"{path.name}: non-text content")
            continue
        inspect_text(path, content, errors)
        if not args.package and path.suffix == ".md":
            inspect_links(path, content, root, errors)
    packages = [root] if args.package else [root / "skills" / name for name in PACKAGE_NAMES]
    for package in packages:
        inspect_package(package, errors)
    if errors:
        print("Release validation failed:")
        print("\n".join(f"- {item}" for item in errors))
        return 1
    print(f"PASS: {count} text files; structure, local references, independence, and privacy patterns")
    return 0


if __name__ == "__main__":
    sys.exit(main())
