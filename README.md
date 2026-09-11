# Codex Configuration

Portable working instructions and a personal orchestration skill for Codex.
This repository contains curated text files, not a copy of the Codex runtime
or its account data.

## Contents

- `AGENTS.md`: global working instructions to merge into the destination account.
- `skills/open-source-orchestrator/SKILL.md`: shared Codex CLI and desktop app
  issue and PR workflow, including native desktop subagent operations.
- `skills/open-source-orchestrator/references/herdr.md`: conditional herdr pane
  instructions, loaded only for Codex CLI running in herdr.

The skill loads `references/review-process.md` for PR reviews and
`references/pytorch-review.md` only for applicable PyTorch reviews. The common
process adds caller/contract investigation, candidate deduplication, and separate
fact-checking; PyTorch guidance is read from the reviewed repository revision
rather than copied into this configuration. Preserve the entire references
folder when installing or updating the skill.

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
5. In a new Codex CLI or desktop app session, ask Codex to load
   `$open-source-orchestrator` and summarize its scope and manager/worker roles.
   This checks discovery, not actual worktree creation or worker execution.

The repository does not change live settings automatically. Model selection
and reasoning effort must still be checked in the actual execution environment.

## Management policy

The orchestration workflow applies to Codex CLI and the Codex desktop app for
open-source issue and PR work. IDE extensions and other hosts do not activate
it automatically. The separately referenced Development Branch Workflow keeps
its existing scope.

Use GPT-6 Astra with high reasoning effort as the initial manager evaluation
baseline. This is a migration starting point, not a proven optimal setting.
Before describing the manager policy as optimized, compare Astra/high with
Astra/medium on comparable work. Medium is a candidate for planning,
decomposition, and delegation that need judgment; high remains appropriate for
complex agentic work. Choose for requirement coverage first, then compare cost
and latency among settings that meet the quality bar. Keep handoffs concise and
avoid repeatedly loading full logs.

Evaluate the migration in stages: first compare Sol/high with Astra/high, then
compare Astra/high with Astra/medium. Within each comparison, hold the task
revision, inputs, instructions, tools, and acceptance criteria constant. Record
requirement coverage, decomposition quality, evidence judgment, unnecessary
pauses, rework, elapsed time, and total manager, worker, and automatic-review
usage and workflow cost. Tune prompts in separate trials only when an observed
problem warrants a change, so prompt effects are not attributed to the model or
effort setting.
Treat API-price calculations as estimates separate from Codex subscription
consumption. These repository instructions define the evaluation policy; they
do not claim that comparative trials have already been performed.

The manager may select stronger settings proactively when known complexity or
risk supports that choice; repeated failures are not a prerequisite. Use
`xhigh` only when evaluation shows a clear benefit for the task class, and
evaluate `max` against `xhigh` before adopting it. Keep cheaper worker roles for
bounded work and preserve task-appropriate worker selection.

High-risk PRs receive proactive semantic/contract review with Astra at high
reasoning or above, a separate independent counterexample review, and focused
execution checks. The manager uses the Astra/high initial evaluation baseline;
the semantic review remains a separate worker assignment. Reviewers must report
exact revisions, coverage, evidence, and missing verification; material gaps
prevent an unqualified approval. See the skill's High-Risk PR Review procedure.

Each task has one active manager. The initial session may manage or hand off to
an appropriately configured fresh session. Transfer goals, constraints, approval
scope, worktrees, results, pending decisions, and the worker roster before the
former manager becomes idle. Do not run two managers for the same task.

In Codex CLI running inside herdr, name worker panes
`<management-pane-name>-<number>`, such as `review-1`
and `review-2`. Start numbering at 1, avoid collisions, and retain names when
reusing panes. See the herdr reference for manager handoff naming details.

In the desktop app, use native subagents rather than separate sidebar tasks.
Assign explicit worktree paths and file ownership; spawning a worker does not
establish checkout isolation. Keep independent reviews in fresh conversations.
Separate sidebar tasks require an explicit user request.

Installing these files does not change a running CLI or desktop session's model
or reasoning settings, or a herdr launch command. Verify actual settings and
available controls on each host; disclose settings that cannot be verified.

## Privacy and version control

The ignore file allows only the explicitly listed configuration, reference,
documentation, and license files.
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
