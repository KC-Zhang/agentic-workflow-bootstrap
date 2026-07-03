# Repository Guide

This file gives coding agents practical context for working in `$PROJECT_NAME`.

## Commands

```bash
# Development
$DEV_COMMAND

# Typecheck / lint
$CHECK_COMMAND

# Tests
$TEST_COMMAND

# Build
$BUILD_COMMAND
```

TODO(owner): Add commands for migrations, preview, e2e tests, seed data, formatting, and deploy.

## Environment

- Package manager: `$PACKAGE_MANAGER`
- TODO(owner): Document required language/runtime versions.
- TODO(owner): Document local environment variables and safe setup steps.
- TODO(owner): Document secrets policy and which files must never be committed.

## Architecture

TODO(owner): Replace with a concise request/job flow and important runtime boundaries.

Example:

```text
Client / caller
  -> route, controller, or command
  -> service layer
  -> data access / external provider
  -> persistence, events, or response
```

## Key Directories

| Path | Purpose |
| --- | --- |
| TODO | TODO |

## Data Stores

TODO(owner): Document databases, queues, object storage, caches, search indexes, analytics vendors, and migration tools.

## Deployment

TODO(owner): Document build artifacts, deploy commands, approval requirements, environment differences, rollback steps, and smoke tests.

## Known Pitfalls

TODO(owner): Record operational hazards, flaky commands, migration gotchas, provider quirks, and high-risk code paths. Link to `docs/reflect/` or `docs/incidents/` when the issue meets the threshold.
