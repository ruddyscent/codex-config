# Codex Configuration

Portable working instructions and personal workflow skills for Codex.
This repository contains curated text files, not a copy of the Codex runtime
or its account data.

## Contents

- `AGENTS.md`: global working instructions to merge into the destination account.
- `skills/oss-orchestrator/SKILL.md`: shared Codex CLI and desktop app
  issue and PR workflow, including native desktop subagent operations.
- `skills/oss-orchestrator/references/herdr.md`: conditional herdr pane
  instructions, loaded only for Codex CLI running in herdr.

The skill loads `references/review-process.md` for PR reviews and
`references/pytorch-review.md` only for applicable PyTorch reviews. The common
process adds caller/contract investigation, candidate deduplication, and separate
fact-checking; PyTorch guidance is read from the reviewed repository revision
rather than copied into this configuration. Preserve the entire references
folder when installing or updating the skill.

## Character relationship maps

`skills/character-relationship-map/` contains the installed relationship-map skill,
its registry templates, schema, and starter SVG renderer. Preserve the entire
folder when installing it as `~/.codex/skills/character-relation-map/`, and compare
and back up an existing installation first. The source folder is
`character-relationship-map`; the existing frontmatter name and invocation remain
`character-relation-map` for compatibility. Do not maintain a second source copy
under that installation name. Portrait constraints distinguish sourced
traits, user-directed choices, and unknown details; verify assets against these
constraints while preserving the semantic graph during style changes.

The starter renderer requires PyYAML and produces a basic text-and-edge SVG.
It does not implement portrait embedding or the full skill QA workflow; adapt
layout and inspect the result for the specific work.

## Apply to another account

1. Locate the destination Codex home (`CODEX_HOME` when configured; otherwise
   `~/.codex`) and confirm its personal skill discovery location.
2. Compare and back up existing destination files before making changes.
3. Copy `skills/oss-orchestrator/` into the personal skills directory,
   preserving the `references/herdr.md` relative path. If it already exists,
   compare and merge local changes instead of overwriting them blindly.
4. Merge the desired instructions from `AGENTS.md` into the destination global
   `AGENTS.md`. Preserve unrelated account preferences. Adjust the fallback
   skill path in the orchestration section if the destination uses another
   location. Do not copy a source account's absolute paths.
5. In a new Codex CLI or desktop app session, ask Codex to load
   `$oss-orchestrator` and summarize its scope and manager/worker roles.
   This checks discovery, not actual worktree creation or worker execution.

The repository does not change live settings automatically. Model selection
and reasoning effort must still be checked in the actual execution environment.

## Migrate an existing installation

The maintained source is `skills/oss-orchestrator/`; the frontmatter name and
invocation are `oss-orchestrator` and `$oss-orchestrator`. For an installation
using `~/.codex/skills/open-source-orchestrator/` (or the corresponding configured
Codex home), compare the old installation with the maintained source and any
existing `oss-orchestrator` destination first. Back up outside skill discovery
paths, then merge local changes and preserve the entire references folder.
Do not overwrite either installation blindly or create a second maintained source.

After verifying the merged destination, retire the old
`open-source-orchestrator` installation from discovery so only `oss-orchestrator`
remains. Merge the updated references and fallback path into the destination
`AGENTS.md`, preserving unrelated preferences. Use a fresh Codex CLI or desktop
session to verify `$oss-orchestrator` discovery and loading. Repository edits do
not migrate live installations automatically.

## Management policy

The orchestration workflow applies to Codex CLI and the Codex desktop app for
open-source issue and PR work. IDE extensions and other hosts do not activate
it automatically. The separately referenced Development Branch Workflow keeps
its existing scope.

Use GPT-6.1 Sol/medium at Standard speed as the provisional general manager
configuration. Optimize total included subscription allowance consumption or
billed credits per successfully verified task, including manager, workers,
automatic review, retries, rework, and final verification. This policy is not a
claim of measured savings. Raw tokens and API-price estimates are separate
metrics, and credit rates do not directly determine included subscription usage.

Use Luna for bounded, checkable work and Sol/medium for general implementation,
investigation, and review. Evaluate GPT-6.1 Terra for scoped fixes. Reserve Astra
for demanding judgment and high-risk semantic review; raise capability or effort
when complexity or observed quality warrants it. Standard is the speed default;
Fast/Ultrafast are explicit latency tradeoffs whose current usage multipliers
must be checked before quoting them. Small tasks may run in one session; scale
delegation to useful parallelism and required independent verification.

The skill defines representative comparison tasks and quality gates before
trials. Compare models at the same supported effort with fixed inputs, revision,
tools, instructions, environment, speed, and acceptance criteria; then vary
effort with the model fixed. Evaluate delegation and prompt changes separately. Record
actual runtime settings, verification, retries/rework, elapsed time, and the
usage measurement source. Disclose missing telemetry or shared-activity
attribution gaps. Compare repeated representative tasks before claiming an
optimized default; do not invent benchmark or savings claims.

This replaces the Astra/high migration baseline and fixed staged comparison in
[issue #10](https://github.com/ruddyscent/codex-config/issues/10), superseded by
[issue #21](https://github.com/ruddyscent/codex-config/issues/21). Quality gates,
independent review, and authorization boundaries remain intact. The skill was
renamed to `oss-orchestrator` in
[issue #20](https://github.com/ruddyscent/codex-config/issues/20); this naming
change preserves the model and delegation policy.

High-risk PRs still receive a separate Astra semantic/contract reviewer at high
reasoning or above, an independent counterexample reviewer, and focused execution
checks. The manager's configuration follows the coordination task rather than
a blanket Astra/high requirement. Reviewers must report exact revisions,
coverage, evidence, and missing verification; material gaps prevent an
unqualified approval. Use `xhigh` only with evaluation evidence and compare
`max` with `xhigh` before adoption.

Policy sources, reviewed November 7, 2026:
[OpenAI model selection](https://developers.openai.com/api/docs/guides/model-selection),
[Codex model guidance](https://learn.chatgpt.com/docs/models), and
[usage and pricing](https://learn.chatgpt.com/docs/pricing). Recheck current
availability and product-specific usage rules when evaluating the policy.

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
