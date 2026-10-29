# Library selection: work matrix

Source for the candidate examples: [Blessed.rs crate directory](https://blessed.rs/crates), reviewed 2026-10-29. Refresh the relevant category when making a dependency decision; the entries below are a starting shortlist.

## Choose for the actual project

1. Define the operation, target platforms, compiler/MSRV, runtime, and required integration points. Inspect existing dependencies and repository decisions first. Use the standard library or an existing dependency when it already meets the need.
2. Open the relevant category in the live Blessed.rs catalog and use the work matrix to identify candidates. For a work area outside this table, find its corresponding category directly in the catalog.
3. Read the candidate's official versioned documentation or source. Use Context7 when available to find documentation, then verify the APIs, enabled features, target support, and compatibility with the actual project. Follow the catalog's links to primary documentation rather than treating the catalog summary as an API contract.
4. Compare the candidates against the project's constraints. Check license compatibility and current upstream maintenance where relevant. Explain why the selected crate fits better than keeping the existing approach or another plausible candidate. Verify security-sensitive decisions against the appropriate primary guidance.
5. Record the need, catalog category and access date, selected crate/version/features, rationale, primary evidence, and planned verification before adding or replacing the dependency. Keep the record brief and proportional to the decision.

## Task-to-library matrix

Candidate names come from the linked catalog. The decision questions are project-specific prompts for evaluating them. This table sets no fixed crate versions or universal defaults.

| Work | Catalog candidates to investigate | Decision questions before choosing |
| --- | --- | --- |
| Error boundaries | `anyhow`, `thiserror` | Is this an application boundary or a reusable public error API? What information must callers recover? |
| Observability | `tracing`, `log` | What subscriber/facade already exists, and which events, context, or structured fields are needed? |
| Structured formats | `serde`, `serde_json`, `toml` | Which wire/configuration format, schema guarantees, and compatibility rules apply? |
| Calendar/time | `jiff`, `time`, `chrono` | Which timezone, parsing, arithmetic, and existing integration requirements apply? |
| Async execution | `tokio`, `smol` | Which runtime do existing dependencies require? What cancellation and blocking contracts must hold? |
| Outbound HTTP | `reqwest`, `ureq` | Is the caller synchronous or asynchronous? Which TLS, timeout, streaming, and deployment constraints apply? |
| Web services | `axum`, `actix-web` | Which runtime, middleware, routing, and framework integrations does the project need? |
| RPC/WebSockets | `tonic`, `tokio-tungstenite` | Which protocol is required? What schema, streaming, shutdown, and executor compatibility is needed? |
| SQL access | `sqlx`, `diesel`, `rusqlite` | Which database and query/ORM approach fit? Verify transactions, migrations, pooling, and execution model. |
| Data services | `redis`, `mongodb` | Which server, protocol/version, topology, and client capabilities are actually required? |
| Terminal tools | `clap`, `ratatui` | Is the requirement argument handling or an interactive terminal interface? Check the appropriate component. |
| Parallel work/messaging | `rayon`, `crossbeam-channel`, `flume` | Is the problem parallel computation or communication? Establish scheduling, delivery, and backpressure needs. |
| Numerical work | `nalgebra`, `ndarray` | Which data shape, operations, precision, memory layout, and interoperability constraints matter? |
| Language interop | `bindgen`, `cxx`, `pyo3` | Which foreign language and ABI are involved? Verify generation, build, ownership, and safety obligations. |
| Native interfaces | `egui`, `iced` | Which rendering, accessibility, deployment, and existing application integration requirements apply? |
| Text/IDs/temp files | `regex`, `uuid`, `tempfile` | Which exact operation is needed, and what validation, lifetime, or resource-cleanup contract applies? |

## Evidence and fallback

Record why a dependency is needed and how the chosen candidate meets the actual constraints. An existing project dependency or another well-supported crate can be the right choice even when it is outside this shortlist; verify and explain that decision from primary sources.

If Blessed.rs cannot be read, report the failed lookup and use this bundled matrix for discovery while consulting primary documentation or dependency source. An unavailable catalog does not establish or invalidate an API contract. A required contract that remains unverified keeps the affected implementation behind the documentation gate.

This reference is included in full within the package. Its decision workflow and prompts are original project material, copyright (c) 2026 Rust contributors, distributed under the [MIT terms](../LICENSE). Linked external materials retain their own terms.
