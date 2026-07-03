#!/usr/bin/env python3
"""Install the agentic workflow documentation template into a repository."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from string import Template


TEXT_SUFFIXES = {
    ".md",
    ".yaml",
    ".yml",
    ".txt",
    ".json",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy agent workflow docs into a target repository."
    )
    parser.add_argument("--target", default=".", help="Target repository root.")
    parser.add_argument("--project-name", help="Project name for generated docs.")
    parser.add_argument(
        "--language",
        default="English",
        help="Default collaboration language to write into AGENTS.md.",
    )
    parser.add_argument(
        "--primary-module",
        default="core",
        help="Primary module slug for initial module docs and changelog.",
    )
    parser.add_argument(
        "--primary-module-title",
        default="Core",
        help="Human-readable primary module title.",
    )
    parser.add_argument(
        "--main-path",
        action="append",
        default=[],
        help="Important source path to include in the initial module docs. Repeatable.",
    )
    parser.add_argument("--dev-command", help="Override detected dev command.")
    parser.add_argument("--check-command", help="Override detected typecheck command.")
    parser.add_argument("--test-command", help="Override detected test command.")
    parser.add_argument("--build-command", help="Override detected build command.")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files. Use only after reviewing current docs.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned writes without changing files.",
    )
    return parser.parse_args()


def detect_package_manager(target: Path) -> str:
    if (target / "pnpm-lock.yaml").exists():
        return "pnpm"
    if (target / "yarn.lock").exists():
        return "yarn"
    if (target / "package-lock.json").exists():
        return "npm"
    if (target / "bun.lockb").exists() or (target / "bun.lock").exists():
        return "bun"
    return "npm"


def package_run_command(package_manager: str, script_name: str) -> str:
    if package_manager == "npm":
        return f"npm run {script_name}"
    if package_manager == "yarn":
        return f"yarn {script_name}"
    if package_manager == "bun":
        return f"bun run {script_name}"
    return f"{package_manager} {script_name}"


def read_package_scripts(target: Path) -> dict[str, str]:
    package_json = target / "package.json"
    if not package_json.exists():
        return {}
    try:
        data = json.loads(package_json.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    scripts = data.get("scripts")
    return scripts if isinstance(scripts, dict) else {}


def choose_command(
    scripts: dict[str, str],
    package_manager: str,
    candidates: list[str],
    fallback: str,
) -> str:
    for candidate in candidates:
        if candidate in scripts:
            return package_run_command(package_manager, candidate)
    return fallback


def detect_commands(target: Path, args: argparse.Namespace) -> dict[str, str]:
    package_manager = detect_package_manager(target)
    scripts = read_package_scripts(target)
    return {
        "PACKAGE_MANAGER": package_manager,
        "DEV_COMMAND": args.dev_command
        or choose_command(scripts, package_manager, ["dev", "start"], "TODO: add dev command"),
        "CHECK_COMMAND": args.check_command
        or choose_command(
            scripts,
            package_manager,
            ["check", "typecheck", "type-check", "lint"],
            "TODO: add typecheck or lint command",
        ),
        "TEST_COMMAND": args.test_command
        or choose_command(
            scripts,
            package_manager,
            ["test", "test:unit", "vitest"],
            "TODO: add test command",
        ),
        "BUILD_COMMAND": args.build_command
        or choose_command(scripts, package_manager, ["build"], "TODO: add build command"),
    }


def render_path(path: Path, replacements: dict[str, str]) -> Path:
    return Path(Template(str(path)).safe_substitute(replacements))


def render_text(text: str, replacements: dict[str, str]) -> str:
    return Template(text).safe_substitute(replacements)


def read_template(path: Path, replacements: dict[str, str]) -> str:
    return render_text(path.read_text(encoding="utf-8"), replacements)


def should_treat_as_text(path: Path) -> bool:
    return path.suffix in TEXT_SUFFIXES or path.name == "AGENTS.md"


def build_replacements(target: Path, args: argparse.Namespace) -> dict[str, str]:
    project_name = args.project_name or target.resolve().name
    main_paths = args.main_path or ["TODO: add main source path"]
    commands = detect_commands(target, args)
    replacements = {
        "PROJECT_NAME": project_name,
        "COLLABORATION_LANGUAGE": args.language,
        "PRIMARY_MODULE": args.primary_module,
        "PRIMARY_MODULE_TITLE": args.primary_module_title,
        "MAIN_PATH_LIST": "\n".join(f"- `{path}`" for path in main_paths),
        "TODAY": date.today().isoformat(),
    }
    replacements.update(commands)
    return replacements


def copy_templates(
    template_root: Path,
    target: Path,
    replacements: dict[str, str],
    force: bool,
    dry_run: bool,
) -> tuple[list[Path], list[Path]]:
    written: list[Path] = []
    skipped: list[Path] = []

    for template_file in sorted(p for p in template_root.rglob("*") if p.is_file()):
        relative_template_path = template_file.relative_to(template_root)
        relative_target_path = render_path(relative_template_path, replacements)
        target_file = target / relative_target_path

        if target_file.exists() and not force:
            skipped.append(relative_target_path)
            continue

        written.append(relative_target_path)
        if dry_run:
            continue

        target_file.parent.mkdir(parents=True, exist_ok=True)
        if should_treat_as_text(template_file):
            target_file.write_text(read_template(template_file, replacements), encoding="utf-8")
        else:
            target_file.write_bytes(template_file.read_bytes())

    return written, skipped


def main() -> int:
    args = parse_args()
    skill_root = Path(__file__).resolve().parents[1]
    template_root = skill_root / "assets" / "agent-workflow-template"
    target = Path(args.target).resolve()

    if not template_root.exists():
        raise SystemExit(f"Template directory not found: {template_root}")
    if not target.exists():
        raise SystemExit(f"Target directory not found: {target}")

    replacements = build_replacements(target, args)
    written, skipped = copy_templates(
        template_root=template_root,
        target=target,
        replacements=replacements,
        force=args.force,
        dry_run=args.dry_run,
    )

    action = "Would write" if args.dry_run else "Wrote"
    print(f"{action} {len(written)} files into {target}")
    for path in written:
        print(f"  + {path}")

    if skipped:
        print(f"Skipped {len(skipped)} existing files; rerun with --force to overwrite after review")
        for path in skipped:
            print(f"  - {path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
