# Agent Instructions for $PROJECT_NAME

This file gives AI coding agents project-specific guidance for working in this repository.

## Collaboration

- Default collaboration language: $COLLABORATION_LANGUAGE.
- Code, variable names, type names, log keys, database fields, and public APIs should follow the repository's existing naming style.
- Read code and docs before making claims about project behavior. Verify uncertain facts from repository files.
- Keep changes minimal and scoped to the user request. Do not reformat unrelated files or overwrite user changes.
- Prefer simple, readable code over speculative flexibility. Add abstractions only when they express a real domain concept, hide meaningful complexity, or remove substantial duplication.

## Project Overview

TODO(owner): Replace this section with a short description of the product, runtime, deployment target, and most important modules.

Primary module: `$PRIMARY_MODULE`

Main paths:
$MAIN_PATH_LIST

## Required Reading

Before non-trivial code changes, read:

- `docs/agent/CLAUDE.md`: commands, architecture, environment, deployment, and known pitfalls.
- `docs/agent/CODE_STYLE.md`: coding rules for helpers, naming, tests, exports, and module boundaries.
- `docs/agent/CODEBASE_INDEX.md`: module map, entry points, tests, and required docs.
- `docs/agent/DOCUMENTATION_SYSTEM.md`: mandatory documentation update rules.
- Relevant `docs/modules/*.md`, `docs/patterns/*.md`, `docs/database/*.md`, `docs/decisions/*.md`, `docs/reflect/*.md`, and `docs/incidents/*.md` for the touched area.

## Common Commands

```bash
$DEV_COMMAND
$CHECK_COMMAND
$TEST_COMMAND
$BUILD_COMMAND
```

TODO(owner): Add migration, e2e, lint, preview, and deploy commands if they exist.

## Development Workflow

### Before Editing

1. Run `git status --short` and understand existing changes.
2. Do not revert or overwrite user changes unless explicitly asked.
3. Avoid editing directly on protected branches such as `main` or `master` unless the user or repo policy explicitly allows it.
4. Read the relevant code and docs from `docs/agent/CODEBASE_INDEX.md`.
5. Look for similar implementations and tests before adding new patterns.
6. If the change touches data access, payments, auth, privacy, deployment, queues, analytics, AI/model calls, or migrations, read the relevant module docs, patterns, decisions, reflects, and incidents first.

### While Editing

- Use `rg` / `rg --files` for searching.
- Put server-only logic in server-only modules and keep secrets out of shared/client code.
- Use existing data-access helpers, error handling, logging, and test patterns when they fit.
- Check async flows for cancellation, retries, idempotency, cleanup, and failure paths.
- Do not log secrets, tokens, full cookies, private keys, payment secrets, or unnecessary sensitive user data.

### After Editing

1. Add or update focused tests for changed behavior.
2. Run affected tests and type/lint checks.
3. Update required docs according to `docs/agent/DOCUMENTATION_SYSTEM.md`.
4. Review load changes: database queries/writes, external API calls, queue volume, analytics events, model calls, file scans, or cloud costs.
5. If the change is purely documentation/configuration with no runtime effect, state `Load change: none`.

## Testing Expectations

- API route changes need tests for success, invalid input, authorization/permissions, and failure paths.
- Business logic changes need unit tests for normal cases, boundaries, and invalid input.
- Payments, balances, webhooks, auth, migrations, and data deletion need idempotency, replay, rollback, and permission coverage.
- UI changes need component or end-to-end coverage when they affect user workflows.
- Pure docs/config changes usually do not need automated tests, but explain what was not run and why.

## Documentation System

- Every non-trivial code change updates the relevant `docs/changelog/{module}.md`.
- Changes to module behavior, entry points, data dependencies, or boundaries update `docs/modules/{module}.md`.
- User-visible feature changes update `docs/features.yaml`.
- New API routes, runtime config, schema, permissions, migrations, analytics events, deployment behavior, or architectural decisions require the corresponding docs listed in `docs/agent/DOCUMENTATION_SYSTEM.md`.
- Only hard-to-find, high-risk, recurring production bugs belong in `docs/reflect/`.

## Git

- Confirm `git status --short` before finalizing.
- Commit only task-related files when a commit is requested or useful.
- Do not push, force-push, amend, rebase, reset, or deploy without explicit user approval.
- Never run destructive commands unless the user explicitly requests and confirms the target environment.

## Final Checklist

- Relevant code and docs were read.
- Existing unrelated changes were not overwritten.
- New exports or helpers are used by production code, not only by tests.
- Tests/checks were run or a clear reason was given.
- Required module docs and changelogs were updated.
- Load change was reviewed and reported.
- No secrets or unnecessary sensitive data were exposed.
