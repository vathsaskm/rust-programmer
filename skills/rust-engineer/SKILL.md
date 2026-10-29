---
name: rust-engineer
description: "Implement, debug, refactor, and review Rust code using official documentation, idiomatic ownership, and focused verification. Use for Rust coding tasks in an existing or new crate."
license: MIT
---

# Rust Engineer

Deliver working Rust that fits the repository. Make the design as simple as the behavior permits, and spend verification effort where a failure would matter.

## Establish the contract

Read repository instructions, the affected code and callers, and the tests that define the behavior. Check the relevant Cargo manifest and pinned toolchain for edition, MSRV, features, and dependency versions. Preserve public behavior and compatibility unless the request calls for changing them. For a review request, return findings with file and line evidence; implement when the user requests changes.

Use narrow searches and targeted reads. Ask about a consequential ambiguity that the code cannot resolve, and continue independent work. Once the behavior and constraints are clear, start implementing.

## Use the right source

Inspect available capabilities before choosing a workaround. Prefer a connected source-control provider for repository and PR operations, local tools for local edits, and a supported review tool when available. Use the project's established database and authentication tooling when those systems are involved. If a preferred integration is unavailable, use an appropriate local tool or primary documentation.

For language semantics or standard-library contracts, consult the relevant official documentation. For a crate API or version-sensitive behavior, use Context7 when available and verify against the crate's own versioned docs or source. Firecrawl can extract a known page; ordinary web search can locate one. Local toolchain docs are useful when current online docs target a newer compiler. Report a lookup failure and use the next available source.

When a language question, diagnostic, or documentation lookup needs a starting point, read [the official Rust reference map](references/official-rust.md) and follow the relevant link. Read only the material needed to settle the decision.

Use the engineering guidance below and the bundled reference map directly. Resolve a specific decision against repository constraints, the actual toolchain, and the relevant official API contract. Add a dependency or optimization only when the task needs it.

## Implement idiomatic Rust

- Make ownership reflect the data lifecycle. Borrow and accept slices when the API only needs a view; return owned data when its lifetime requires it. Use cloning and shared ownership when their semantics are intentional. Diagnose the ownership relationship before changing types to satisfy a compiler error.
- Model meaningful states with enums and small types. Validate external data at the boundary and carry established invariants through types. Keep abstractions and trait bounds proportional to real callers; choose generics or dynamic dispatch for their actual constraints.
- Represent expected absence with `Option` and recoverable failures with `Result`. Propagate useful causes and context. Reserve panic for a justified internal invariant or API contract; `expect` and `unwrap` remain reasonable in tests and demonstrably infallible cases. Follow the project's error conventions.
- Preserve text, numeric, and resource semantics: account for UTF-8 boundaries, overflow or narrowing, and cleanup when those matter to the change. Prefer standard library and existing dependencies. Retain the current edition and MSRV unless a migration is requested.
- For async or concurrent code, make sharing, task ownership, cancellation, and shutdown deliberate. Keep locks short and executor work nonblocking. Bound queues or concurrency where the workload can grow; verify the runtime's documented behavior for the affected operations.
- Prefer a safe implementation. When unsafe code is necessary, keep it contained and document the operation's specific safety argument, including the obligations a safe caller cannot be allowed to violate. For performance work, measure the relevant path before trading clarity for complexity.

## Verify in proportion to the change

Follow existing required checks. For an ordinary Rust code change, format the touched code, run focused `cargo test` coverage, and use `cargo clippy` scoped to the affected package or targets with the repository's normal features and lint policy. Tests and Clippy already compile code; add a separate build or `cargo check` when it resolves a distinct concern.

Add a regression or behavior test when it exercises a meaningful contract. Documentation-only edits and mechanical changes can use lighter verification. Choose feature-matrix runs, Miri, concurrency model checking, fuzzing, or benchmarks when the actual change warrants them. Add new CI, broad lint policies, or verification infrastructure only when requested or necessary for the task.

Address failures caused by the change. Once appropriate checks pass, finish; repeat or expand them when new evidence warrants it. If a check is unavailable, needs credentials, or fails in pre-existing code, state the exact limitation without claiming success or silently changing the repository's policies.

## Deliver

Briefly report the resulting behavior, material design decisions, checks actually run, and unresolved limitations. Cite the primary documentation when a non-obvious API or language decision depends on it. Keep unrelated changes and speculative follow-up work out of the patch.
