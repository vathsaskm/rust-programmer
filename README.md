# Rust

**A practical Rust engineering workflow. A searchable library of 265 Rust rules. Install either one.**

[Get the latest release](https://github.com/vathsaskm/Rust/releases/latest) · [Rust Engineer](skills/rust-engineer/SKILL.md) · [Rust Skills](skills/rust-skills/SKILL.md) · [MIT license](LICENSE)

Give your coding agent a repeatable way to build, debug, refactor, and review Rust. Choose the engineering workflow, the detailed guidelines, or both. Each package works independently and includes its own supporting files and license.

## Choose your package

| Package | What it gives you | Use it when |
| --- | --- | --- |
| **Rust Engineer** | An engineering brief covering repository context, ownership, APIs, errors, async work, unsafe code, and focused verification | You want the agent to carry a Rust task from investigation through checked changes |
| **Rust Skills** | 265 rules across 26 categories, with examples and an index | You want detailed guidance for a specific design, implementation, or review decision |

Rust Engineer is packaged as a Codex skill with agent-facing instructions and optional UI metadata. Its `agents/openai.yaml` describes how the skill appears in the app. Each host supplies the model, tools, and execution permissions.

There are no references between the two packages, shared files, required companion skills, bundled credentials, or installation scripts. Preferred documentation integrations are optional. Normal Rust development still needs the project's compiler, dependencies, and any services the task uses.

## Install in Codex

Clone the repository:

```sh
git clone https://github.com/vathsaskm/Rust.git
cd Rust
mkdir -p "$HOME/.agents/skills"
```

Install **Rust Engineer**:

```sh
cp -R skills/rust-engineer "$HOME/.agents/skills/"
```

Or install **Rust Skills**:

```sh
cp -R skills/rust-skills "$HOME/.agents/skills/"
```

Run both copy commands if you want both packages. Review existing installations before replacing them.

For a project-specific installation, copy the selected folder into that project's `.agents/skills/` directory instead.

Codex discovers skills in these locations. If a newly installed skill does not appear, restart Codex. See the [official skill documentation](https://learn.chatgpt.com/docs/build-skills) for discovery, invocation, and configuration.

### Install from a release ZIP

Download either package from [Releases](https://github.com/vathsaskm/Rust/releases/latest), verify it against `SHA256SUMS`, and extract it into your skill directory. Each ZIP contains one top-level skill folder, including its license and supporting resources.

On macOS:

```sh
shasum -a 256 rust-engineer-v1.0.0.zip
unzip rust-engineer-v1.0.0.zip -d "$HOME/.agents/skills"
```

For Rust Skills, substitute `rust-skills-v1.0.0.zip`. Compare the printed checksum with the corresponding entry in `SHA256SUMS` before extraction.

## Put it to work

Mention the installed skill in your Codex prompt:

```text
Use $rust-engineer to fix this borrow-checker error. Preserve the public API
and run the checks appropriate to the affected crate.
```

```text
Use $rust-engineer to review this Rust diff. Report actionable findings with
file and line evidence, and explain which checks you actually ran.
```

```text
Use $rust-skills to review ownership and error handling in this module.
Read only the rules relevant to the code and explain the concrete tradeoffs.
```

The instructions are plain Markdown with `SKILL.md` manifests. Other agents can read them, but their installation paths, invocation syntax, and metadata support depend on the host.

## What the engineer does

1. Reads repository instructions, callers, tests, the manifest, and the pinned toolchain.
2. Checks language and library contracts against the relevant official sources.
3. Implements a scoped change that preserves the intended behavior and compatibility.
4. Runs appropriate formatting, tests, and lint checks, then reports the outcome and limitations.

It keeps ownership and lifetimes explicit, expected failures recoverable, concurrent work bounded where needed, and unsafe operations tied to a specific safety argument. Verification follows the repository's requirements and the risk of the change.

## What the rules cover

Ownership and borrowing · error handling · memory · unsafe code · API design · async · concurrency · compiler optimization · numeric safety · type safety · traits · conversions · const evaluation · Serde · pattern matching · macros · closures · collections · naming · testing · documentation · observability · performance · project structure · linting · anti-patterns.

Start with the [rule index](skills/rust-skills/SKILL.md), then open the relevant rule files. These guidelines need judgment: check the actual compiler, crate version, public contract, and project conventions before applying an example.

## Repository layout

```text
skills/
  rust-engineer/
    SKILL.md
    LICENSE
    agents/openai.yaml
    references/official-rust.md
  rust-skills/
    SKILL.md
    LICENSE
    rules/                 # 265 Markdown rules
scripts/verify_release.py   # Structure, independence, and privacy checks
.github/workflows/check.yml # Validation and secret scanning
```

## Release checks

Run the package validator and [Gitleaks](https://github.com/gitleaks/gitleaks) before publishing:

```sh
python3 scripts/verify_release.py
gitleaks dir . --redact --ignore-gitleaks-allow
gitleaks git . --redact --ignore-gitleaks-allow
```

The validator checks both packages in isolation, local documentation links, file types, and common private-data patterns. CI repeats validation and scans Git history with a pinned Gitleaks version. Release ZIPs include package files only, use normalized metadata, and ship with SHA-256 checksums.

See [SECURITY.md](SECURITY.md) for the review scope and private reporting guidance. Automated checks and review reduce risk; they cannot prove the absence of every possible secret.

## License and attribution

The original Rust Engineer package and repository materials are available under the [MIT license](LICENSE).

Rust Skills is derived from [leonardomso/rust-skills](https://github.com/leonardomso/rust-skills). The bundled manifest identifies version `1.5.1`; this repository distributes a local snapshot rather than claiming to mirror an upstream release. Its original [MIT license and copyright notice](skills/rust-skills/LICENSE) are preserved. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

This is an independent project. The Rust project, OpenAI, and referenced crate authors have not endorsed it.
