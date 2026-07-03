# Documentation Update System

This file defines long-term documentation maintenance rules. For non-trivial code changes, agents should treat code, tests, and docs as one delivery unit.

## Documentation Directories

| Path | Purpose | Update when |
| --- | --- | --- |
| `docs/agent/` | Agent entry points, code map, documentation system | Agent workflow, commands, module routing, or repo operating rules change |
| `docs/modules/` | Current module facts: responsibilities, entry points, data, tests, risks | Module behavior, API, data dependency, boundary, or validation changes |
| `docs/changelog/` | Per-module chronological change records | Any non-trivial code change |
| `docs/features.yaml` | Durable user-visible feature inventory | User-visible features are added, renamed, deprecated, removed, or materially changed |
| `docs/patterns/` | Reusable implementation patterns | A new cross-file pattern appears or repeated pitfalls need codified guidance |
| `docs/decisions/` | Architecture decision records | A long-term architecture, dependency, deployment, data, or cross-module contract decision is made |
| `docs/database/` | Schema, migrations, runtime config, data-access notes | Tables, fields, indexes, migrations, runtime config, or data-access rules change |
| `docs/reflect/` | Severe recurring bug lessons | A hard-to-find, high-risk, recurring production bug is fixed |
| `docs/incidents/` | Production incidents | Outage, cost spike, security event, data issue, or third-party incident occurs |
| `docs/specs/` | Feature specifications | Complex feature work starts |
| `docs/plans/` | Implementation plans | Multi-step migration, refactor, or rollout needs a durable plan |

## Change Types

Classify each change before finishing:

- `feat`: new user-visible or operator-visible capability.
- `fix`: production or latent bug fix.
- `refactor`: structure change without intended behavior change.
- `perf`: performance, cost, caching, or query optimization.
- `docs`: documentation only.
- `test`: tests only.
- `chore`: build, dependency, config, or script maintenance.

## Required Updates

| Signal | Required update |
| --- | --- |
| API route or public endpoint changes | Module doc, module changelog, route tests |
| User-visible feature changes | `docs/features.yaml`, module doc, module changelog |
| Admin/operator capability changes | Relevant module doc and changelog |
| Core business logic changes | Module doc and changelog; add pattern docs if the approach becomes reusable |
| Auth, billing, payments, privacy, deletion, migrations, queues, analytics, external providers, or AI/model calls | Module doc, changelog, focused tests, and relevant risk docs |
| Database schema, migration, index, enum, or runtime config changes | `docs/database/`, module doc, changelog |
| Long-term architecture decision | New `docs/decisions/YYYY-MM-DD-title.md` |
| Hard-to-find, high-risk, recurring production bug fix | New `docs/reflect/YYYY-MM-DD-bug-name.md` |
| Production incident, security event, data issue, cost spike, or third-party outage | New `docs/incidents/YYYY-MM-DD-incident-name.md` |
| New durable module | Module doc, changelog, `docs/agent/CODEBASE_INDEX.md`, and `docs/features.yaml` if user-visible |

## Load Review

Every non-trivial task must include a load review. Consider:

- Database reads/writes, scans, transactions, locks, migrations, and indexes.
- External API calls, retries, rate limits, and provider costs.
- Queue jobs, scheduled jobs, fanout, and idempotency.
- Analytics event volume, identity calls, privacy, and vendor cost.
- AI/model calls, prompt size, streaming, fallbacks, and logging.
- Filesystem scans, generated artifacts, and build/deploy work.

Final response or changelog should state one of:

- `Load change: increase` with path, frequency, and mitigation.
- `Load change: decrease` with removed or reduced work.
- `Load change: none` for no runtime load effect.

## Changelog Format

Add new entries at the top of `docs/changelog/{module}.md`.

```markdown
## YYYY-MM-DD - type(scope): short summary

- Change: Explain how user or system behavior changes.
- Code: List key paths.
- Tests: List commands run, or explain why not run.
- Docs: List docs updated.
- Risk: Note remaining risk or manual verification.
- Load change: increase/decrease/none, with reason.
- PR: pending / #123
```

Docs-only changes belong in `docs/changelog/docs-system.md`.

## Reflect Threshold

Before adding a reflect file, decide whether the lesson belongs in `AGENTS.md`, `docs/agent/`, `docs/patterns/`, `docs/modules/`, or `docs/changelog/` instead.

Only use `docs/reflect/` for bugs that are all of:

- Hard to locate.
- High impact.
- Likely to recur.
- Relevant to production stability, correctness, data integrity, security, privacy, cost, or user trust.

## Testing Relationship

Documentation does not replace tests. After changing code:

1. Add or update focused tests.
2. Run affected validation.
3. Update module docs and changelog with the test commands.
4. If automated testing is not practical, write manual verification steps and residual risk.
