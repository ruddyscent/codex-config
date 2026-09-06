---
name: open-source-orchestrator
description: Use only in Codex CLI to coordinate open-source issue handling and pull request reviews through delegated workers, isolated worktrees, and task-appropriate model settings. Use for the primary management session on those tasks; not for general coding, workflow advice, or editing this skill. Assigned workers execute their tasks directly without recursively applying management requirements.
---

# Open-Source Issue and PR Orchestration

- Apply the orchestration workflow only in Codex CLI when handling issues or
  reviewing pull requests in open-source projects. Verify the execution host
  from explicit runtime context; access to shell tools is not proof of CLI use.
  Do not activate orchestration in the Codex desktop app, IDE extensions, or
  other hosts. If the host cannot be determined, explain the uncertainty and
  do not activate orchestration automatically.
- This host restriction applies to orchestration, not to a separately referenced
  Development Branch Workflow section. Reading that section outside Codex CLI
  must not activate the manager, delegation, or model-selection requirements.
- The management role, mandatory delegation, and highest-model/maximum-effort
  requirements apply only to the original user-facing session. Worker agents
  must perform their assigned work directly using their assigned settings;
  they must not recursively create management sessions or delegate again
  unless the management session explicitly assigns further delegation.
- Keep the primary session as the management session throughout the task.
  It must use the most capable OpenAI model available in the current account
  and host for this work, with the highest reasoning effort that model and
  runtime support. Verify the actual settings before substantive work; do not
  assume that these instructions change the running session's configuration.
  If the required settings cannot be applied, explain the limitation and the
  exact user action needed instead of silently using lower settings.
- Resolve model choices using current OpenAI model guidance and the runtime's
  available models and supported reasoning levels. Do not hard-code a model
  name or assume that the same effort labels are supported everywhere.
- Create a dedicated Git worktree for the issue or PR before substantive
  repository work, using the relevant base or PR revision. Reuse that task's
  worktree on follow-up turns. Preserve the original checkout and user changes,
  and follow the applicable development branch and commit workflow below.
- For PR reviews, record the exact base and head commit SHAs and review that
  revision pair. Before reporting completion, check whether either revision
  has changed. If so, delegate review of the affected changes and rerun relevant
  verification, stating which revision pair the final findings cover. If the
  latest PR state cannot be checked, disclose that limitation.
- The management session owns scoping, decomposition, delegation, coordination,
  assessment of returned evidence, and the final response. Delegate detailed
  investigation, implementation, review, and test execution to worker agents
  rather than doing that work directly or duplicating their investigations.
  Lightweight setup and inspection needed to delegate effectively are allowed.
- Create concrete, bounded subtasks with the necessary context, worktree path,
  ownership, expected output, and verification requirements. Run independent
  subtasks in parallel within runtime limits when doing so materially reduces
  elapsed time or provides valuable independent verification; sequence dependent
  tasks. Bundle small related tasks to reduce context-transfer overhead and
  duplicate investigation. Avoid parallel work solely because it is possible.
  Avoid concurrent writes to the same files, using separate worktrees for workers
  when isolation is needed. Delegate integration and conflict resolution.
- When running in herdr, read and follow [herdr pane operations](references/herdr.md)
  before assigning workers. Load that reference only for herdr sessions.
- Outside herdr, use the available native subagent mechanism. If required
  worker or pane controls are unavailable, report the blocker and required
  action rather than silently replacing delegation with direct execution.
- Choose each worker's model and reasoning effort according to task difficulty,
  uncertainty, risk, and current OpenAI guidance. Use the least costly settings
  likely to meet the quality requirements: lighter settings for bounded routine
  work, and stronger models and more reasoning for complex diagnosis, design,
  or subtle review. Escalate when results or verification show that the initial
  choice is insufficient. Workers need not inherit the management settings.
- Require workers to return concise findings, relevant file references, changes,
  verification results, and unresolved risks. Assess this evidence before
  reporting completion and delegate further work when gaps remain.
- After collecting a worker's results, leave it idle for related follow-up work
  or stop it when no longer needed; do not keep completed workers running or
  polling without a task.
  Before removing any task worktree, check for uncommitted changes and preserve
  required results. Follow the existing authorization rules for deletion; do
  not discard work or remove worktrees merely because a subtask has finished.
- This workflow does not authorize commits, pushes, issue or PR publication,
  merges, or destructive operations beyond the user's existing authorization.

## Development Branch Workflow

- If a repository-level `AGENTS.md` or other applicable project instruction
  defines a development or commit workflow, follow the project instruction
  instead of this global workflow and do not apply the conflicting parts of
  this section.
- For projects hosted on GitHub, if a commit is authorized while the current
  branch is `master`, create a relevant GitHub issue before committing.
- Create a dedicated working branch from `master` and check it out in the
  task worktree before the commit. Preserve the original checkout. Register
  that branch as the issue's development branch, using GitHub's linked
  development branch mechanism when available.
- Complete these steps in order: create the issue, create and link the working
  branch, check out the working branch in the task worktree, and then commit.
- Do not commit the task changes directly to `master`.
