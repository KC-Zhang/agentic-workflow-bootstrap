# Agentic Workflow Bootstrap

Reusable agent skill for installing a documentation-first coding-agent workflow into a software repository.

The skill sets up files such as `AGENTS.md`, `docs/agent/`, `docs/modules/`, `docs/changelog/`, `docs/reflect/`, and related workflow documentation so future coding-agent sessions have clear operating instructions.

## Installation

Install with the `skills` CLI:

```bash
npx skills add KC-Zhang/agentic-workflow-bootstrap --skill agentic-workflow-bootstrap
```

To install globally instead of into the current project:

```bash
npx skills add KC-Zhang/agentic-workflow-bootstrap --skill agentic-workflow-bootstrap --global
```

To list the skills exposed by this repository without installing:

```bash
npx skills add KC-Zhang/agentic-workflow-bootstrap --list
```

## Usage

After installation, ask your coding agent to use the skill in the repository where you want the workflow installed:

```text
Use $agentic-workflow-bootstrap to install an agent documentation and iteration workflow in this repository.
```

For an existing repository with agent docs already present, ask for a dry run first:

```text
Use $agentic-workflow-bootstrap to dry-run the workflow installation in this repository and show what would change.
```

## What It Installs

- `AGENTS.md`
- `docs/agent/`
- `docs/modules/`
- `docs/changelog/`
- `docs/patterns/`
- `docs/decisions/`
- `docs/reflect/`
- `docs/incidents/`
- `docs/specs/`
- `docs/plans/`
- `docs/features.yaml`

## Manual Script

The bundled installer can also be run directly from a checked-out copy of this skill:

```bash
python3 scripts/install_agent_workflow.py --target /path/to/repo --dry-run
python3 scripts/install_agent_workflow.py --target /path/to/repo
```

Use `--dry-run` before writing into repositories that already have documentation or agent instructions.
