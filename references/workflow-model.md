# Workflow Model

Use this reference when explaining or modifying the workflow itself.

## Core Contract

The workflow is built around four ideas:

1. Agent context must be discoverable from the repository, not reconstructed from chat memory.
2. Code, tests, and durable documentation move together for non-trivial changes.
3. Agents should make minimal, scoped changes and avoid overwriting unrelated user work.
4. Every handoff should include validation and a load/risk review, even when the answer is "none".

## File Responsibilities

- `AGENTS.md`: always-on behavior contract for coding agents in the repo.
- `docs/agent/CLAUDE.md`: practical repo guide: commands, architecture, environment, deploy, and known pitfalls.
- `docs/agent/CODE_STYLE.md`: coding standards that should be checked before implementation.
- `docs/agent/CODEBASE_INDEX.md`: routing map from a task area to code entry points, tests, and required docs.
- `docs/agent/DOCUMENTATION_SYSTEM.md`: update rules for module docs, changelogs, features, ADRs, incidents, and reflections.
- `docs/modules/*.md`: current facts about production behavior and module boundaries.
- `docs/changelog/*.md`: chronological behavior-change log per module.
- `docs/patterns/*.md`: reusable implementation patterns that are too specific for generic style docs.
- `docs/decisions/*.md`: long-term architecture decisions with alternatives and consequences.
- `docs/reflect/*.md`: hard-to-find, high-risk, recurring bug lessons.
- `docs/incidents/*.md`: production incidents, costs, outages, security events, or third-party failures.
- `docs/features.yaml`: inventory of durable user-visible features.

## Iteration Loop

For non-trivial work, the agent loop is:

1. Inspect current branch and dirty worktree.
2. Read the root instructions and relevant docs before claiming project facts.
3. Locate the smallest code surface that can satisfy the request.
4. Implement without unrelated refactors or formatting churn.
5. Add or update focused tests for changed behavior.
6. Update module docs and changelog entries required by the documentation system.
7. Run affected validation.
8. Review load, cost, privacy, and operational effects.
9. Finalize with files changed, tests run, unresolved risk, and load-change conclusion.

## Data-Load Review

Keep a mandatory load review, but adapt the object of review to the project:

- Database apps: new or changed queries, writes, indexes, transactions, and hot-path scans.
- API clients: new external calls, retry behavior, rate limits, and authentication scope.
- Event systems: new producers, consumers, queue volume, idempotency, and replay behavior.
- Analytics: event volume, user identification, privacy, and vendor cost.
- AI apps: model calls, prompt size, streaming behavior, retries, fallbacks, and content logging.
- Static/documentation-only changes: explicitly state `Load change: none`.

## Reflection Threshold

`docs/reflect/` should stay small. Add a reflection only when a bug was hard to locate, high impact, likely to recur, and relevant to production stability, correctness, security, cost, or user trust. Put routine guidance in `AGENTS.md`, `docs/agent/`, `docs/patterns/`, or module docs instead.
