# Code Style Instructions

These rules optimize for clear, maintainable production code rather than cosmetic abstraction.

## Core Principles

- Keep changes minimal and scoped to the task.
- Prefer existing project patterns, helper APIs, error handling, and tests.
- Avoid unnecessary complexity. Do not duplicate a parallel system for one exception when a clear flag, configuration, or small extension fits the existing model.
- Production code must be driven by production needs. Do not add functions, types, constants, return fields, exports, or intermediate state only to make tests easier.
- Add an abstraction only when it expresses a real domain concept, hides meaningful complexity, reduces substantial duplication, or protects a rule that will be reused.

## Functions And Helpers

- Keep functions small and focused, but do not create one-line wrappers just to look abstract.
- Search for existing same-domain helpers before adding a new one.
- Private helpers are fine when they clarify a real production rule.
- A helper can be tested directly only if production code also calls it.
- If a helper exists only for tests, move it to the test file or remove it.
- Inline simple boolean expressions unless a named function clearly communicates a domain rule or hides non-trivial complexity.

## Tests And Production Boundaries

- Test files may define factories, fixtures, and assertion helpers.
- Production modules should not expose internals solely for tests.
- After adding or changing an export, audit production and test references separately with `rg`.
- If a symbol has only test references and no production path, remove it or move it to tests.
- Keep long-term exports only for real cross-module contracts.

## Naming

- Names must explain what a thing is, why it exists, or how it is used.
- Avoid vague names such as `variant`, `unit`, `entity`, `handler`, `manager`, `data`, `info`, `item`, `value`, `result`, `temp`, and `stable` when a domain word is available.
- Use the concrete domain name when all callers pass the same kind of value. For example, prefer `conversationId` over `assignmentKey` if the value is always a conversation id.
- Use generic role names only when multiple real domains share the helper, and document the role.
- Do not reuse an old name after the meaning changes. Rename the concept or preserve the old semantics.

## Module Boundaries

- Module names should reveal runtime boundaries.
- Shared/client-imported modules must not statically import databases, secrets, server SDKs, filesystem-only helpers, or server-only configuration.
- Server-only behavior belongs in server-only modules or clearly named server paths.
- Keep side effects out of modules that provide pure constants, types, and shared helpers.

## Comments

- Add comments only when they save future readers from non-obvious reasoning.
- Prefer names and structure over comments that restate code.
- Comments explaining a business rule should link to the module doc, pattern, decision, reflect, or incident when relevant.
