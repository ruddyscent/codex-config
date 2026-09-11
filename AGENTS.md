# Global Codex Instructions

These instructions apply to all projects unless a repository-level
`AGENTS.md` provides more specific instructions.

## General Principles

- Prefer minimal, focused changes that directly address the requested task.
- Do not modify unrelated code, configuration, or documentation.
- Investigate the root cause before applying a workaround.
- Preserve the existing architecture, conventions, and coding style unless
  there is a clear reason to change them.
- Do not introduce unnecessary dependencies.
- Do not perform destructive operations unless explicitly requested.
- When requirements are ambiguous, inspect the existing project and infer
  intent from its code, tests, documentation, and history before asking the
  user.
- Clearly report assumptions, limitations, and anything that could not be
  verified.

## Project Instructions

- Look for repository-level `AGENTS.md` files before making changes.
- Follow the most specific applicable `AGENTS.md`.
- Treat repository-specific instructions as authoritative for that repository
  when they differ from these global defaults.

## Code Changes

- Understand the relevant code path before editing it.
- Prefer fixing the underlying cause rather than suppressing symptoms.
- Keep changes as small and localized as reasonably possible.
- Preserve backward compatibility unless the task explicitly requires a
  breaking change.
- Avoid speculative refactoring.
- Do not rewrite working code merely to match personal style preferences.
- Add comments only when they explain non-obvious behavior, constraints, or
  design decisions.
- Write code, comments, identifiers, and technical documentation in English
  unless the project explicitly uses another language.

## Testing and Verification

- For multi-stage work, establish completion criteria and required verification
  before implementation. Distinguish required outcomes from optional improvements.
- Reuse prior verification only when the relevant code, inputs, and environment
  remain applicable. Rerun affected checks after changes and disclose coverage
  gaps; retain required CI and independent verification.
- For cross-platform changes, check relevant environment and path assumptions
  early, before expensive validation.
- Run relevant tests after making code changes.
- Start with focused tests for the affected area when available.
- Run broader test suites when the change has wider impact or when practical.
- Do not claim that a change works unless it has been verified.
- If tests cannot be run, clearly state why.
- Report failing tests that appear unrelated to the change instead of silently
  modifying unrelated code to make them pass.
- Do not weaken, remove, or bypass tests merely to obtain a passing result.

## Git

- Inspect the working tree before modifying or committing files.
- Preserve unrelated user changes already present in the working tree.
- Do not discard, overwrite, reset, or clean user changes unless explicitly
  requested.
- Do not amend, rebase, force-push, or rewrite history unless explicitly
  requested.
- Do not push to a remote repository unless explicitly requested.

### Commits

- Create commits only when explicitly requested.
- Use a Conventional Commit-style prefix in the commit subject when compatible
  with the repository's conventions.
- Write a concise commit subject describing the change.
- Include a commit body explaining the important context, rationale, and
  implementation details when appropriate.
- Keep commits focused on a single logical change.
- Do not include unrelated modifications in a commit.

### Commit Signing

- Preserve Git commit signing when it is configured.
- Before creating a commit, verify that the configured signing mechanism is
  available.
- If GPG signing fails, diagnose and restore the signing environment before
  retrying the commit.
- When working over SSH with GPG agent forwarding, prefer the forwarded signing
  agent rather than importing or creating a secret signing key on the remote
  host.
- Do not disable commit signing with `commit.gpgsign=false`, `--no-gpg-sign`,
  or an equivalent workaround merely to make a commit succeed.
- Do not import, copy, generate, or persist a private signing key on a remote
  machine as a workaround unless explicitly requested.
- If signing requires user interaction or cannot be restored automatically,
  stop before committing and clearly explain what user action is required.

## GitHub

- Prefer the GitHub CLI (`gh`) for authenticated GitHub operations when
  appropriate.
- Before performing an authenticated GitHub operation, verify authentication
  with:

      gh auth status

- If authentication is expired, invalid, or missing, restore authentication
  before continuing.
- Use the appropriate `gh auth` command, such as `gh auth login`, to restore
  authentication.
- After authentication is restored, verify it again with:

      gh auth status

- Once authentication succeeds, automatically resume the originally requested
  GitHub operation. Do not require the user to repeat the original request.
- Do not work around an authentication failure by falling back to anonymous or
  unauthenticated access when the operation requires authentication.
- If authentication requires interactive browser, device-code, credential, or
  other user action, clearly tell the user exactly what action is required,
  wait for it to complete, verify authentication, and then continue the
  original task.
- Never expose authentication tokens, credentials, private keys, or secrets in
  logs, commits, patches, or responses.

## GitHub Issues and Pull Requests

- Read the relevant issue or pull request before making changes when the task
  references one.
- On follow-up work, review relevant issue comments and linked PR discussions,
  including reviews, inline threads, replies, and resolved or outdated threads.
  Reconcile completed work, remaining conditions, and superseded conclusions
  with the current code and evidence. Explain why prior evidence cannot be reused
  before repeating work, and disclose missing discussion or verification.
  Preserve independent review by withholding prior findings and verdicts until
  initial independent assessments are recorded.
- Use the issue description, discussion, acceptance criteria, and repository
  code as context for the implementation.
- Do not assume that an issue's proposed implementation is necessarily the
  correct technical solution; verify it against the codebase.
- When fixing a reported bug, reproduce or otherwise establish the failure
  condition when practical before changing the code.
- After fixing a bug, verify the behavior and run relevant regression tests.
- Before reporting issue work complete, reconcile each in-scope issue-body
  completion checkbox with evidence that still applies to the current revision
  and environment. When authorized, save the evidence-backed checkbox updates
  and verify the resulting body; otherwise report the exact pending updates or
  publication failure without claiming issue completion or expanding the
  authorization to comments, closure, commits, or pushes.
- When preparing a pull request, summarize what changed, why it changed, and
  how it was verified.
- Do not merge or close issues or pull requests unless explicitly requested.

### Open-Source Issue and PR Orchestration

- Apply the orchestration rules in this section in Codex CLI and the Codex
  desktop app when handling issues or reviewing pull requests in open-source
  projects. Verify the host from explicit runtime context; shell access alone
  does not establish the host. Do not activate this workflow automatically in
  IDE extensions, other hosts, or an unknown host. Explain any uncertainty.
  This scope does not change the separate Development Branch Workflow below.
- Use native subagents in the desktop app. herdr pane operations apply only
  to Codex CLI running inside herdr. Do not create separate sidebar tasks as
  workers unless the user explicitly requests separate tasks.
- Within that scope, the primary user-facing session must load and follow the
  `open-source-orchestrator` skill before substantive work. If it is not listed,
  check `~/.codex/skills/open-source-orchestrator/SKILL.md`. If unavailable,
  report the missing dependency rather than silently skipping the workflow.
- Designate exactly one active manager per task. The initial session may manage
  or hand off to a fresh session using the skill's handoff procedure.
  Use GPT-6 Astra (`gpt-6-astra`) with `high` reasoning effort as the initial
  evaluation baseline. Verify actual settings. Do not describe this as an
  optimized default until comparable evaluation includes Astra at `medium`.
  Follow the skill's evidence-based model and effort policy; known task risk or
  complexity can justify a stronger setting before a failure occurs, but
  `xhigh` and `max` require evaluation evidence rather than automatic selection.
  For high-risk PRs, keep that manager baseline and separately assign an
  Astra semantic reviewer at `high` or above plus an independent counterexample
  reviewer.
- Worker agents must execute their assigned tasks with their assigned settings.
  The management role and mandatory delegation do not apply recursively;
  further delegation requires an explicit assignment from the manager.

### Development Branch Workflow

- For GitHub projects, read and follow the Development Branch Workflow section
  in `open-source-orchestrator/SKILL.md` before an authorized commit from
  `master`. This reference also applies outside open-source issue and PR work;
  in that case, read only that section without activating the management workflow.

## Dependencies

- Avoid adding dependencies when the standard library or existing project
  dependencies can reasonably solve the problem.
- When adding or upgrading a dependency, understand why it is required and
  minimize its scope.
- Preserve lockfiles and dependency-management conventions used by the
  repository.
- Do not perform broad dependency upgrades as part of an unrelated task.

## Security

- Never expose secrets, tokens, passwords, private keys, or credentials.
- Do not commit `.env` files or other secret-bearing files unless the project
  explicitly uses a safe template containing no secrets.
- Treat external input as untrusted.
- Prefer secure defaults.
- Do not bypass security controls merely to make development more convenient.
- Flag security-sensitive behavior discovered while working on the requested
  area, but avoid unrelated large-scale security refactoring without approval.

## Documentation

- Update documentation when a code or configuration change makes existing
  documentation inaccurate.
- Keep documentation focused on behavior that users or developers need to know.
- Prefer examples that can actually be executed.
- Do not create new documentation files unless they provide clear value or are
  requested.

## Multi-Host Development

- Assume development may occur across macOS and remote Linux environments.
- Do not assume that credentials, GPG keys, paths, package managers, or system
  configuration are identical across hosts.
- Detect the current environment before performing host-specific operations.
- Preserve host-specific security boundaries.
- In particular, do not copy private credentials or signing keys between hosts
  merely to resolve an environment problem.
- Prefer portable project configuration over machine-specific changes when
  practical.

## Command Execution

- Prefer non-destructive inspection commands before commands that modify state.
- Review command effects before running destructive or irreversible operations.
- Do not use elevated privileges (`sudo`) unless required and justified.
- Avoid commands that broadly delete files, reset repositories, overwrite
  configuration, or modify system state unless explicitly required by the task.
- When a command fails, understand the failure before repeatedly retrying or
  applying increasingly broad workarounds.

## Completion

Before considering a coding task complete:

1. Review the resulting diff.
2. Confirm that only intended files were changed.
3. Run relevant tests or verification.
4. Check for obvious regressions, security issues, and unintended changes.
5. Report what was changed.
6. Report what was tested and the result.
7. Report anything that remains unresolved or could not be verified.
