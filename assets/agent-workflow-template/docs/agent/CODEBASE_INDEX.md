# Codebase Index

## How To Use This Index

For any non-trivial change:

1. Read the relevant module section below.
2. Read `docs/modules/{module}.md`.
3. Read each item listed under that section's required docs when the condition matches the touched behavior.
4. Read `docs/agent/DOCUMENTATION_SYSTEM.md` before finishing the task.
5. End with a load-change review.

If a change touches more than one module, follow the required reading for each affected module. Do not rely on code search alone for domains with production incidents, cost risk, security risk, payments, auth, migrations, data deletion, analytics, queues, or external provider calls.

## $PRIMARY_MODULE_TITLE

Start here:
$MAIN_PATH_LIST

Tests:

- TODO(owner): Add test paths.

Required docs:

- `docs/modules/$PRIMARY_MODULE.md`
- TODO(owner): Add relevant design, database, pattern, decision, reflect, or incident docs.

Risks:

- TODO(owner): Add high-risk paths such as auth, billing, privacy, data access, migrations, queues, analytics, AI calls, or deployment.

## Documentation System

Start here:

- `AGENTS.md`
- `docs/agent/CODE_STYLE.md`
- `docs/agent/DOCUMENTATION_SYSTEM.md`
- `docs/features.yaml`
- `docs/modules/`
- `docs/changelog/`
- `docs/patterns/`
- `docs/database/`
- `docs/decisions/`

Rules:

- Every non-trivial code change updates the relevant module changelog.
- User-visible feature changes update `docs/features.yaml`.
- Schema or runtime config changes update `docs/database/`.
- Only hard-to-find, high-risk, recurring production bugs update `docs/reflect/`.

## Adding A Module

When a new module becomes durable:

1. Create `docs/modules/{module}.md`.
2. Create `docs/changelog/{module}.md`.
3. Add a section in this file with entry points, tests, required docs, and risks.
4. Add or update `docs/features.yaml` if the module owns user-visible features.
