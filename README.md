# Rust

**Independent agent and skill packages for practical Rust development.**

[![Validation](https://github.com/vathsaskm/Rust/actions/workflows/check.yml/badge.svg)](https://github.com/vathsaskm/Rust/actions/workflows/check.yml)
[![MIT License](https://img.shields.io/badge/license-MIT-f08052)](LICENSE)

[Latest release](https://github.com/vathsaskm/Rust/releases/latest) · [Download the agent](https://github.com/vathsaskm/Rust/releases/download/v1.0.1/rust-engineer-v1.0.1.zip) · [Download the skill](https://github.com/vathsaskm/Rust/releases/download/v1.0.1/rust-skills-v1.0.1.zip)

Rust Engineer helps an agent carry a Rust development task through investigation, implementation, and verification. Rust Skills provides focused guidance and examples for understanding code and making design decisions.

Choose the package that fits your work. Each includes its own instructions, supporting content, and license, and installs on its own.

![Rust Engineer and Rust Skills are separate, complete packages with no dependency between them.](docs/assets/independent-packages.svg)

## Choose what you need

| | Rust Engineer · Agent | Rust Skills · Skill |
| --- | --- | --- |
| **Purpose** | Carry a Rust task through to a verified result | Explain a Rust concept or support a specific design decision |
| **Typical work** | Implementation, debugging, refactoring, and code review | Targeted explanations, examples, and tradeoff analysis |
| **Included** | Engineering instructions, a reference map, display metadata, and a license | A searchable guidance index, supporting examples, and a license |
| **Installation** | Install the agent package by itself | Install the skill package by itself |

## Install

### Download a release

Get either ZIP from [v1.0.1](https://github.com/vathsaskm/Rust/releases/tag/v1.0.1):

- [Rust Engineer](https://github.com/vathsaskm/Rust/releases/download/v1.0.1/rust-engineer-v1.0.1.zip)
- [Rust Skills](https://github.com/vathsaskm/Rust/releases/download/v1.0.1/rust-skills-v1.0.1.zip)
- [SHA-256 checksums](https://github.com/vathsaskm/Rust/releases/download/v1.0.1/SHA256SUMS)

Compare your download's SHA-256 digest with the matching entry in `SHA256SUMS`, then extract the selected ZIP into your Codex skill directory. On macOS:

```sh
shasum -a 256 rust-engineer-v1.0.1.zip
mkdir -p "$HOME/.agents/skills"
unzip rust-engineer-v1.0.1.zip -d "$HOME/.agents/skills"
```

For Rust Skills, use `rust-skills-v1.0.1.zip` instead. Review an existing installation before replacing it.

### Install from source

```sh
git clone https://github.com/vathsaskm/Rust.git
cd Rust
mkdir -p "$HOME/.agents/skills"
```

Install the agent:

```sh
cp -R skills/rust-engineer "$HOME/.agents/skills/"
```

Or install the skill:

```sh
cp -R skills/rust-skills "$HOME/.agents/skills/"
```

For project-specific use, copy the selected folder into that project's `.agents/skills/` directory. If Codex does not discover it automatically, restart Codex. See the [official installation and invocation documentation](https://learn.chatgpt.com/docs/build-skills).

Rust Engineer is an agent workflow distributed in a Codex skill folder. Its optional display metadata configures how it appears in the app; your host supplies the model, tools, and execution permissions. Other agents can read the Markdown instructions, with installation and invocation adapted to their host.

## Use the agent

```text
Use $rust-engineer to investigate this compiler error and implement a fix.
Preserve the public API and verify the affected behavior.
```

```text
Use $rust-engineer to review this Rust change. Explain actionable findings
with file and line evidence, and report the checks actually performed.
```

![The engineering workflow moves from understanding the request, through design and implementation, to verification and a clear handoff.](docs/assets/engineering-workflow.svg)

## Use the skill

```text
Use $rust-skills to help me understand the ownership choices in this module.
Show relevant examples and explain the tradeoffs for this code.
```

```text
Use $rust-skills to assess this API design against the crate's compatibility
requirements and explain the alternatives.
```

Start with the [skill index](skills/rust-skills/SKILL.md) and load the supporting material relevant to the task. Apply it in the context of the actual compiler, library version, and repository conventions.

## Independence and release quality

Each ZIP is validated in isolation, with the other package absent. Documentation references stay within their package or point to public reference material. There are no shared package files or cross-package imports.

Releases include separate archives and SHA-256 checksums. Validation covers package structure, local references, archive metadata, and common private-data patterns. Gitleaks scans published files, Git history, and release archives; GitHub repeats validation and scanning in CI.

The packages contain no account credentials or machine configuration. Scan results describe the checks performed and do not establish an unconditional security guarantee. See [SECURITY.md](SECURITY.md) for details and private reporting.

## Explore the project

- [Agent instructions](skills/rust-engineer/SKILL.md)
- [Agent reference map](skills/rust-engineer/references/official-rust.md)
- [Skill index](skills/rust-skills/SKILL.md)
- [Release history](CHANGELOG.md)
- [Validation script](scripts/verify_release.py)

## License and attribution

Rust Engineer and the original repository materials are available under the [MIT license](LICENSE).

Rust Skills includes an attributed snapshot derived from [leonardomso/rust-skills](https://github.com/leonardomso/rust-skills). Its original [license](skills/rust-skills/LICENSE) and attribution are preserved. See [third-party notices](THIRD_PARTY_NOTICES.md) for provenance.

This independent project is not endorsed by the Rust project, OpenAI, or referenced crate authors.
