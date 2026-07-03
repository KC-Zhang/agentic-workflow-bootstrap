# Customization Guide

Use this reference before installing or adapting the workflow in an existing repository.

## Repository Assessment

Gather these facts first:

- Project name and product purpose.
- Primary stack, language, package manager, framework, database, and deployment target.
- Commands for dev, typecheck, lint, tests, build, migration, preview, and deploy.
- Main source directories, route/API entry points, worker jobs, scripts, and tests.
- High-risk domains: auth, payments, billing, data deletion, privacy, analytics, queues, AI calls, mobile, migrations, infrastructure, or anything historically fragile.
- Existing docs, contribution rules, branch policy, release process, and incident logs.

## Adaptation Rules

- Replace every placeholder with a verified repo fact, not a guess.
- If a fact is unknown, leave a short `TODO(owner): ...` instead of inventing.
- Keep generic docs short; put deep module details in `docs/modules/`.
- Do not require heavyweight docs for trivial temporary experiments.
- Keep changelog entries focused on behavior, code paths, tests, docs, risk, and PR.
- Make the root `AGENTS.md` strict enough to guide agents but not so large that it buries project facts.

## Existing Repo Merge

When files already exist:

1. Run the installer with `--dry-run`.
2. Read existing files before changing them.
3. Merge the new workflow into existing instructions, preserving stricter local rules.
4. Prefer adding links from existing docs to the new docs over duplicating long text.
5. Do not overwrite custom deploy, security, or data rules without explicit approval.

## Module Index Construction

For each meaningful module, record:

- Human name and slug.
- Code entry points.
- Tests.
- Required docs.
- High-risk behaviors.
- Any module-specific validation commands.

Keep module slugs stable because changelog files and feature inventory reference them.

## Documentation Scope

Update docs when behavior, architecture, data dependencies, runtime config, APIs, features, or known risks change. Do not force docs updates for local-only scratch files, one-off experiments, generated artifacts, or purely mechanical formatting unless they affect how future agents should work.
