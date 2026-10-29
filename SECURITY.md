# Security and privacy

This repository distributes instructions and examples. It includes no service credentials, account configuration, or executable installation hooks. The optional repository validation workflow runs only the published validation script and pinned scanning tools.

## Publication review

The initial release is prepared from an explicit list of package and repository files in a new Git history. Personal configuration directories, source-machine Git history, caches, local audit output, and filesystem metadata are excluded.

The release process checks:

- Secret patterns and encoded content with Gitleaks, using redacted output and ignoring inline suppression comments.
- Machine-specific paths, non-example contact addresses, authenticated URLs, and private-data patterns.
- Each package's documentation links in isolation, with cross-package references rejected.
- Commit and tag identities, using a generic project identity and a noreply address.
- Extracted release archives, checksums, and normalized ZIP metadata.

Upstream license attribution, public documentation links, reserved example addresses, and the repository's public GitHub owner are intentional public information. They are distinct from private contact details or account secrets.

Validation and scanners have limits. A passing report is evidence of the checks performed, not an unconditional security guarantee. Future changes need the same review before publication.

## Report a concern

Use the repository's **Security → Report a vulnerability** option for confidential reports when available. Do not put a credential or personal data into a public issue. Report the affected path and a redacted description through the private channel.

If a live credential is exposed, revoke or rotate it before treating content removal as sufficient.
