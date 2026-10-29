# Official Rust reference map

These are original engineering notes based on selected official documentation, consulted on 2026-10-22. They are a lookup map, not a copy of the manuals. Documentation evolves; use the repository's actual compiler, edition, and dependency versions when applying it.

## Ownership and APIs

[References and Borrowing](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html) explains that a reference borrows a value and must stay valid. Shared and exclusive access must respect the borrowing rules for the duration of their use; a reference's last use can end a borrow before its enclosing block ends. Resolve an ownership error by examining who owns and uses the value.

For arguments that only read data, slices and references often express the contract with fewer ownership requirements. Return owned data when the result must outlive its source. A useful clone is legitimate; distinguish duplicating a value from cloning an `Arc` handle. `Arc` shares ownership across threads and still requires its contents to satisfy the relevant thread-safety bounds.

Use [standard library documentation](https://doc.rust-lang.org/std/) for the exact contracts of types and methods and the [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/) when a public API needs closer design work. A compatibility-sensitive public signature needs a migration decision even when a different signature looks more idiomatic.

## Errors and invariants

[To panic! or Not to panic!](https://doc.rust-lang.org/book/ch09-03-to-panic-or-not-to-panic.html) recommends giving callers a recovery choice with `Result` when an operation can fail normally. Use panic for an unrecoverable contract violation or internal invariant when that matches the API. Tests and demonstrably infallible operations can reasonably use `unwrap` or `expect`; explain a non-obvious invariant. Never turn an expected input or I/O failure into an internal-invariant claim.

Validate untrusted data at its boundary, construct a valid domain type, and let that type carry the guarantee. Keep useful error causes. A small custom error can be enough; follow existing error conventions before adding `thiserror`, `anyhow`, or another dependency.

## Async and unsafe work

The [Future contract](https://doc.rust-lang.org/std/future/trait.Future.html) describes polling as nonblocking: incomplete work returns pending and arranges a wakeup. Keep executor work cooperative. Runtime-specific cancellation, task shutdown, channels, and blocking-work APIs require that runtime's own versioned documentation.

The [Reference on undefined behavior](https://doc.rust-lang.org/reference/behavior-considered-undefined.html) makes the programmer responsible for soundness in unsafe code. A safe wrapper must remain sound for every safe caller. Review validity, initialization, alignment, lifetime, aliasing, and thread-safety obligations relevant to the operation. An `unsafe` block or a clean tool run does not establish a proof of soundness; the Reference also states that its list of undefined behavior is not exhaustive.

For a concrete unsafe operation, also read its standard library safety contract and the relevant [Rustonomicon](https://doc.rust-lang.org/nomicon/) section. Choose Miri for a supported, focused memory-safety case when it provides useful evidence.

## Cargo, linting, and version compatibility

[cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html) compiles and runs tests. Package selection and test filters narrow the work; preserve the repository's required feature configuration. Passing a test-name filter does not establish that every integration path or documentation example was exercised.

[Clippy usage](https://doc.rust-lang.org/clippy/usage.html) supports individual lint levels and package selection. Its opinionated groups call for judgment. Apply the repository's established lint policy and fix relevant findings; broad new lint groups and warning-denial policies need their own justification.

The [Cargo Book](https://doc.rust-lang.org/cargo/), [Edition Guide](https://doc.rust-lang.org/edition-guide/), and [Compiler Error Index](https://doc.rust-lang.org/error-index.html) are the next stops for manifests, edition changes, and diagnostics. Read the project's pinned toolchain and `rust-version` before adopting a feature from current online docs. Local documentation for an installed toolchain can help reconcile a version mismatch.

## Learning entry point

The [official learning page](https://rust-lang.org/learn/) routes to the Book, [Rust by Example](https://doc.rust-lang.org/rust-by-example/), Rustlings, standard library docs, and deeper references. Reach for a targeted chapter or example when it resolves the task; reading the entire learning catalog is not a prerequisite to coding.
