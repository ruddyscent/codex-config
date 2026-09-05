# Codex Configuration

Portable working instructions and a personal orchestration skill for Codex.
This repository contains curated text files, not a copy of the Codex runtime
or its account data.

## Contents

- `AGENTS.md`: global working instructions to merge into the destination account.
- `skills/open-source-orchestrator/SKILL.md`: open-source issue and PR workflow.
- `skills/open-source-orchestrator/references/herdr.md`: conditional herdr pane
  instructions, loaded only when running in herdr.

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
5. In a new task, ask Codex to load `$open-source-orchestrator` and summarize
   its scope and manager/worker roles. This checks discovery, not actual
   worktree creation or herdr execution.

The repository does not change live settings automatically. Model selection
and reasoning effort must still be checked in the actual execution environment.

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
