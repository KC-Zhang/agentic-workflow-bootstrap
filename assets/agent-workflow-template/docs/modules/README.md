# Module Docs

Module docs record how the system currently works. They are not wishlists.

Update a module doc when code changes affect:

- Responsibilities.
- Entry points.
- API behavior.
- Data dependencies.
- Runtime configuration.
- Permissions.
- Tests or validation commands.
- Operational risks.

Current modules:

- `$PRIMARY_MODULE.md`

When adding a module:

1. Create `docs/modules/{module}.md`.
2. Create `docs/changelog/{module}.md`.
3. Update `docs/agent/CODEBASE_INDEX.md`.
4. Update `docs/features.yaml` if the module owns durable user-visible features.
