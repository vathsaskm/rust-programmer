---
name: rust-engineer
description: >
  Use for every Rust programming or Rust development task. Provides an independent
  engineering workflow with required bundled-rule and version-matched documentation
  checks before coding, then implementation and verification. Covers planning,
  explanation, design, debugging, review, testing, refactoring, optimization, and
  Cargo/build/toolchain work. Also select when Rust is implied by .rs files, Cargo.toml,
  Cargo.lock, rustc, crates, workspaces, or repository context.
license: MIT
---

# Rust Engineer

Deliver working Rust that fits the repository. Make the design as simple as the behavior permits, and spend verification effort where a failure would matter.

## Before coding: pass the evidence gate

Before generating or editing Rust code, complete the contract, rules, and documentation checks below. Read code, reproduce failures, inspect dependencies, and run diagnostics as needed to establish the evidence. Begin implementation after the gate passes.

### 1. Establish the contract

Read repository instructions, relevant project documentation, affected code and callers, and the tests that define the behavior. Check the Cargo manifest, lockfile, and pinned toolchain for edition, MSRV, features, and actual dependency versions. Identify the intended behavior, compatibility constraints, and meaningful risks. For a review request, establish the same evidence before returning findings; implement when the user requests changes.

Use narrow searches and targeted reads. Resolve consequential ambiguity from the available code and documentation. Ask about an unresolved requirement when it changes the implementation, and continue independent investigation while waiting.

### 2. Read the applicable rules

Consult the [complete best-practices index](references/rust-guidance/INDEX.md), use its task-to-category mapping, and select the guidance relevant to the affected code. Open and read the corresponding detailed files in `references/rust-guidance/rules/`; the index headings alone do not satisfy this check. Prioritize the highest-impact applicable concerns.

Connect the selected rule identifiers to concrete implementation decisions: ownership and lifetimes, error propagation, API compatibility, concurrency, safety, performance, or other affected behavior. Reconcile recommendations with repository requirements and verified API contracts. Explain a material departure. Add dependencies, optimizations, lint policies, and configuration changes when justified by the task.

### 3. Verify the relevant documentation

Read the primary documentation that determines the planned implementation. For language semantics and standard-library contracts, open the relevant official Rust documentation. Use the [official Rust reference map](references/official-rust.md) to locate it; the map itself is a starting point, not a substitute for reading the source.

For a crate API or version-sensitive behavior, use Context7 when available to locate documentation, then verify against the crate's own versioned documentation or source for the resolved dependency and feature configuration. Check compatibility with the actual compiler and MSRV. If current online documentation targets a newer version, use installed toolchain documentation or the matching dependency source to establish the contract you will rely on.

Use available documentation tools directly. Firecrawl can extract a known page; web search can locate a primary source. Keep lookup queries limited to necessary public symbols and redacted diagnostics. Read the relevant page or source section: memory, search snippets, and unopened links do not complete this check. For unsafe operations, verify the specific safety obligations; for concurrent work, verify the relevant runtime's cancellation, blocking, and synchronization contracts.

If a lookup fails, report the actual failure and try another available primary source, including local documentation or dependency source. If a required contract remains unverified, keep the gate unmet for the affected implementation and continue work that does not depend on that contract. Do not claim the check passed without evidence.

### 4. Record the decision and proceed

Before the first code edit, give a concise progress update naming the rule identifiers read, the documentation actually consulted with links or local paths and applicable versions, the resulting design constraints or resolved tradeoffs, and the verification approach. Keep it proportional to the task; reuse evidence already checked for the same scope and versions.

The gate passes when the intended behavior is understood, applicable detailed rules have been read, the contracts needed for the implementation are verified for the target versions, material conflicts are resolved, and the checks for the change are identified. Proceed with implementation once these conditions are met. Revisit the affected checks when the scope, dependency version, feature configuration, or safety assumptions change.

## Use the right tools

Inspect available capabilities before choosing a workaround. Prefer a connected source-control provider for repository and PR operations, local tools for local edits, and a supported review tool when available. Use the project's established database and authentication tooling when those systems are involved. If a preferred integration is unavailable, use an appropriate available tool or primary documentation.

## Implement idiomatic Rust

- Make ownership reflect the data lifecycle. Borrow and accept slices when the API only needs a view; return owned data when its lifetime requires it. Use cloning and shared ownership when their semantics are intentional. Diagnose the ownership relationship before changing types to satisfy a compiler error.
- Model meaningful states with enums and small types. Validate external data at the boundary and carry established invariants through types. Keep abstractions and trait bounds proportional to real callers; choose generics or dynamic dispatch for their actual constraints.
- Represent expected absence with `Option` and recoverable failures with `Result`. Propagate useful causes and context. Reserve panic for a justified internal invariant or API contract; `expect` and `unwrap` remain reasonable in tests and demonstrably infallible cases. Follow the project's error conventions.
- Preserve text, numeric, and resource semantics: account for UTF-8 boundaries, overflow or narrowing, and cleanup when those matter to the change. Prefer standard library and existing dependencies. Retain the current edition and MSRV unless a migration is requested.
- For async or concurrent code, make sharing, task ownership, cancellation, and shutdown deliberate. Keep locks short and executor work nonblocking. Bound queues or concurrency where the workload can grow; verify the runtime's documented behavior for the affected operations.
- Prefer a safe implementation. When unsafe code is necessary, keep it contained and document the operation's specific safety argument, including the obligations a safe caller cannot be allowed to violate. For performance work, measure the relevant path before trading clarity for complexity.

## Verify in proportion to the change

Check the finished change against the rule decisions and documentation contracts established before coding. Follow existing required checks. For an ordinary Rust code change, format the touched code, run focused `cargo test` coverage, and use `cargo clippy` scoped to the affected package or targets with the repository's normal features and lint policy. Tests and Clippy already compile code; add a separate build or `cargo check` when it resolves a distinct concern.

Add a regression or behavior test when it exercises a meaningful contract. Documentation-only edits and mechanical changes can use lighter verification. Choose feature-matrix runs, Miri, concurrency model checking, fuzzing, or benchmarks when the actual change warrants them. Add new CI, broad lint policies, or verification infrastructure only when requested or necessary for the task.

Address failures caused by the change. Once appropriate checks pass, finish; repeat or expand them when new evidence warrants it. If a check is unavailable, needs credentials, or fails in pre-existing code, state the exact limitation without claiming success or silently changing the repository's policies.

## Deliver

Briefly report the resulting behavior, material design decisions, checks actually run, and unresolved limitations. Identify the applicable rules and primary documentation that informed material API, language, or safety decisions, reusing the pre-coding evidence when unchanged. Keep unrelated changes and speculative follow-up work out of the patch.
