---
name: agentic-workflow-bootstrap
description: Bootstrap a reusable agent documentation and iteration workflow in a software repository. Use when the user asks to set up AGENTS.md, agent instructions, code style rules, documentation update rules, module docs, changelogs, reflect/incident logs, or a repeatable AI coding-agent workflow for a new or existing project.
---

# Agentic Workflow Bootstrap

## Overview

Install and adapt a documentation-first agent workflow for a repository. The workflow gives coding agents a clear operating contract: read the right docs first, protect user changes, keep edits minimal, update module documentation and changelogs with code, review data-load changes, and record only high-value incidents or reflections.

## Workflow

1. Inspect the target repository before writing:
   - Run `git status --short` and identify the current branch.
   - Read existing `AGENTS.md`, `README.md`, package manifests, docs directories, and obvious architecture entry points.
   - Detect commands for dev, typecheck, test, build, migration, deploy, and UI tests from project files.
   - Identify the main modules, high-risk domains, data stores, deployment targets, and project-specific safety rules.

2. Read references as needed:
   - Read `references/customization-guide.md` before adapting templates to an existing repo with meaningful docs or architecture.
   - Read `references/workflow-model.md` when changing the workflow rules themselves or explaining why each document exists.

3. Install the template:
   - Prefer the script for a first pass:

```bash
python3 /path/to/agentic-workflow-bootstrap/scripts/install_agent_workflow.py --target .
```

   - Use `--dry-run` first when the repo already has agent docs.
   - Use `--project-name`, `--language`, `--primary-module`, `--primary-module-title`, and repeated `--main-path` flags to seed better placeholders.
   - Do not use `--force` unless the user explicitly wants existing files overwritten.

4. Customize the generated docs:
   - Replace placeholders and remove sections that do not apply.
   - Keep the root `AGENTS.md` short enough to be useful in every turn.
   - Put long module facts in `docs/modules/`, routing in `docs/agent/CODEBASE_INDEX.md`, and detailed standards in `docs/agent/`.
   - Convert generic high-risk data rules into concrete project rules, such as bounded queries, idempotent webhooks, privacy controls, or deployment approvals.
   - Add project-specific module changelog files for every real module.

5. Verify the installation:
   - Run `rg -n "\{\{[A-Z0-9_]+\}\}" AGENTS.md docs/agent docs/modules docs/changelog docs/features.yaml` and resolve remaining placeholders or mark them intentionally.
   - Run `git diff --check`.
   - Review generated docs for project-specific false claims.
   - If the target repo has existing docs, confirm they were merged or linked rather than replaced.

## Document Set

The template installs:

- `AGENTS.md`: root contract for coding agents.
- `docs/agent/AGENTS.md`: short index to the deeper agent docs.
- `docs/agent/CLAUDE.md`: commands, architecture, environment, deploy notes, and known pitfalls.
- `docs/agent/CODE_STYLE.md`: minimal-change, naming, helper, export, and module-boundary rules.
- `docs/agent/CODEBASE_INDEX.md`: module routing and required reading map.
- `docs/agent/DOCUMENTATION_SYSTEM.md`: documentation update triggers and changelog rules.
- `docs/modules/`: durable module facts.
- `docs/changelog/`: chronological module change records.
- `docs/patterns/`, `docs/decisions/`, `docs/reflect/`, `docs/incidents/`, `docs/specs/`, and `docs/plans/`: places for reusable patterns, ADRs, serious bug learnings, production incidents, specs, and implementation plans.
- `docs/features.yaml`: long-lived user-visible feature inventory.

## Editing Rules

- Preserve existing repo instructions unless the user asks to replace them.
- Do not copy source-project names, secrets, URLs, database table names, or deployment commands into the new repo unless they are true for that repo.
- Prefer concrete project facts over generic process language after installation.
- Keep the data-load review requirement, but customize what "load" means for the target system: database queries, API calls, queue jobs, analytics events, file scans, model calls, or cloud costs.
- Keep reflect/incident entry criteria narrow. Routine reminders and one-off feedback belong in `AGENTS.md`, `docs/agent/`, `docs/patterns/`, or module docs.

## Forward Test

For substantial changes to this skill, test it against a temporary repo:

```bash
python3 scripts/install_agent_workflow.py --target /tmp/example-repo --project-name "Example App" --dry-run
python3 scripts/install_agent_workflow.py --target /tmp/example-repo --project-name "Example App"
python3 /path/to/skill-creator/scripts/quick_validate.py /path/to/agentic-workflow-bootstrap
```
