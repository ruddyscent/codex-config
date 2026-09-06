# Codex Configuration

Portable working instructions and a personal orchestration skill for Codex.
This repository contains curated text files, not a copy of the Codex runtime
or its account data.

## Contents

- `AGENTS.md`: global working instructions to merge into the destination account.
- `skills/open-source-orchestrator/SKILL.md`: Codex CLI-only issue and PR workflow.
- `skills/open-source-orchestrator/references/herdr.md`: conditional herdr pane
  instructions, loaded only for Codex CLI running in herdr.

## Apply to another account

1. Locate the destination Codex home (`CODEX_HOME` when configured; otherwise
   `~/.codex`) and confirm its personal skill discovery location.
2. Compare and back up existing destination files before making changes.
3. Copy `skills/open-source-orchestrator/` into the personal skills directory,
   preserving the `references/herdr.md` relative path. If it already exists,
   compare and merge local changes instead of overwriting them blindly.
4. Merge the desired instructions from `AGENTS.md` into the destination global
   `AGENTS.md`. Preserve unrelated account preferences. Adjust the fallback
   skill path in the orchestration section if the destination uses another
   location. Do not copy a source account's absolute paths.
5. In a new Codex CLI session, ask Codex to load `$open-source-orchestrator` and summarize
   its scope and manager/worker roles. This checks discovery, not actual
   worktree creation or herdr execution.

The repository does not change live settings automatically. Model selection
and reasoning effort must still be checked in the actual execution environment.

## Management policy

The orchestration workflow applies only to Codex CLI. The separately referenced
Development Branch Workflow keeps its existing scope.

Use GPT-5.6 Sol with high reasoning effort as the default manager. Delegate hard
technical decisions first; strengthen the manager only after repeated management
failures, recording the reason and returning to the default when resolved.
Evaluate cheaper settings through comparable trials rather than changing models
on every turn. Keep handoffs concise and avoid repeatedly loading full logs.

High-risk PRs receive proactive semantic/contract review with Astra at high
reasoning or above, a separate independent counterexample review, and focused
execution checks. The manager remains Sol/high. Reviewers must report exact
revisions, coverage, evidence, and missing verification; material gaps prevent
an unqualified approval. See the skill's High-Risk PR Review procedure.

Each task has one active manager. The initial session may manage or hand off to
an appropriately configured fresh session. Transfer goals, constraints, approval
scope, worktrees, results, pending decisions, and the worker roster before the
former manager becomes idle. Do not run two managers for the same task.

In herdr, name worker panes `<management-pane-name>-<number>`, such as `review-1`
and `review-2`. Start numbering at 1, avoid collisions, and retain names when
reusing panes. See the herdr reference for manager handoff naming details.

Installing these files does not change a running CLI session or herdr launch
command. Verify actual model and reasoning settings on each host.

## Privacy and version control

The ignore file allows the five reviewed configuration files and a root `LICENSE`.
Explicitly extend that list when adding intentional content. Never force-add
account data to bypass these exclusions.

Do not store credentials, authentication files, API keys, private keys, session
history, logs, caches, downloaded plugins, or machine-specific runtime settings.
Ignore rules do not protect files that are already tracked: inspect staged
changes before committing or publishing.

The initial text was manually reviewed and checked for personal account names,
absolute home paths, email addresses, network addresses, and common secret
formats. No such values were found. Generic paths such as `~/.codex` and the
herdr product name are intentional. These files do reveal workflow preferences.
This review is not a guarantee for later changes.

Before publication, also check Git author name/email and remote URLs: those
can disclose identity even when the file contents contain no personal data.
