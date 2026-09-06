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
- The management role, mandatory delegation, and default model/effort
  requirements apply only to the designated management session. Worker agents
  must perform their assigned work directly using their assigned settings;
  they must not recursively create management sessions or delegate again
  unless the management session explicitly assigns further delegation.
- Designate exactly one active management session per task. Keep the initial
  session when its settings and context are appropriate; otherwise start a
  fresh management session, in a separate pane when using herdr.
- Before transferring control, hand off the goal, constraints, existing approval
  scope, worktree paths, completed work, pending decisions, worker/pane roster,
  and evidence locations. Confirm the recipient is ready and has the required
  settings. Then stop dispatching from the previous manager and leave it idle
  or end it. Do not interrupt active workers or expand authorization on handoff.
  If the recipient is not ready, retain the existing manager as the sole owner.
- Configure the designated management session before substantive work.
  Default to GPT-5.6 Sol (`gpt-5.6-sol`) with `high` reasoning effort. Verify
  actual runtime settings before substantive work; instructions alone do not
  change a running session. If unavailable, explain the limitation and required
  action instead of silently substituting another model or effort level.
- Use current official OpenAI guidance and runtime availability when periodically
  reassessing the default or selecting an exception. Do not reselect the manager
  model on every turn or automatically choose the strongest model and effort.
- Delegate difficult technical judgments to a suitably capable worker first,
  including Astra when justified. Escalate the manager only when repeated
  decomposition or evidence-assessment failures remain after focused worker
  assistance. Record the observed failure, reason, chosen model and effort,
  and scope of the exception; return to the default when that scope is resolved.
- Treat Sol / medium and cheaper manager models as controlled trials on comparable
  tasks, not automatic replacements. Compare total cost, completion quality,
  missed requirements, and rework before proposing a change to the default.
- Create a dedicated Git worktree for the issue or PR before substantive
  repository work, using the relevant base or PR revision. Reuse that task's
  worktree on follow-up turns. Preserve the original checkout and user changes,
  and follow the applicable development branch and commit workflow below.
- For PR reviews, record the exact base and head commit SHAs and review that
  revision pair. Before reporting completion, check whether either revision
  has changed. If so, delegate review of the affected changes and rerun relevant
  verification, stating which revision pair the final findings cover. If the
  latest PR state cannot be checked, disclose that limitation.
- For PR reviews, read [the common review process](references/review-process.md)
  and delegate its context, consolidation, and fact-checking steps. For PyTorch
  reviews only, also read [PyTorch review context](references/pytorch-review.md).
  These references supplement the high-risk requirements below.
- Before assigning PR reviewers, classify risk from the changed semantics and
  affected consumers, not patch size or the author's stated fix alone. Apply
  the High-Risk PR Review procedure below when changes affect compiler IR,
  aliasing/mutation, concurrency, memory lifetime, public contracts, or multiple
  execution backends where a small change can silently alter results. Do not
  wait for a discovered failure to trigger stronger review.
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
- Require workers to return conclusions, evidence locations, verification
  results, changes, and remaining decisions or risks. Keep full logs and detailed
  investigation in task artifacts; retrieve only the excerpts needed to assess
  a claim. Do not omit failures or uncertainty merely to shorten a handoff.
  Assess this evidence before reporting completion and delegate remaining gaps.
- Keep manager context focused on scope, decisions, ownership, and verification.
  Avoid repeatedly loading full logs or duplicating worker investigations.
  For unrelated work, start a fresh session with a concise handoff; preserve
  useful context for related follow-ups rather than restarting indiscriminately.
- Prefer completion notifications or bounded waits over repeated status checks.
  Poll when a decision or intervention depends on fresh state. Do not infer
  waste from wait counts alone or compromise necessary monitoring to save tokens.
- When evaluating cost, separate manager, worker, and automatic review usage;
  deduplicate session fragments and use per-call usage or cumulative deltas.
  Distinguish uncached input, cached input, output, and reasoning output (which
  is part of output, not an additional charge). Compare total workflow cost and
  rework, not token count alone. Label API-price estimates as estimates rather
  than actual charges or Codex subscription-limit consumption.
- After collecting a worker's results, leave it idle for related follow-up work
  or stop it when no longer needed; do not keep completed workers running or
  polling without a task.
  Before removing any task worktree, check for uncommitted changes and preserve
  required results. Follow the existing authorization rules for deletion; do
  not discard work or remove worktrees merely because a subtask has finished.
- This workflow does not authorize commits, pushes, issue or PR publication,
  merges, or destructive operations beyond the user's existing authorization.

## High-Risk PR Review

- Keep the manager on Sol / high by default. Assign a semantic and contract
  reviewer using GPT-6 Astra (`gpt-6-astra`) with at least `high` reasoning;
  choose a higher supported effort when the complexity warrants it. If that
  capability is unavailable, report the unmet review requirement and required
  action instead of silently substituting a weaker review or claiming completion.
- Assign a separate reviewer to search independently for counterexamples.
  Provide the same base/head revisions, requirements, source, and build context,
  but withhold the first reviewer's findings and verdict until both initial
  assessments are recorded. Use a fresh worker conversation to avoid inherited
  conclusions. Select a model capable of the task; two agents are not independent
  evidence merely because they run in separate panes.
- The semantic reviewer must check the public contract and invariants, trace
  changed values and metadata to their affected consumers, and distinguish
  requirements that different consumers impose. Treat added tests as proposed
  behavior to assess against the contract, not as the definition of correctness.
- The counterexample reviewer must inspect adjacent supported and rejected cases
  and affected execution paths beyond the author's reproducer. Select relevant
  dimensions such as aliasing, mutation target, zero or multiple iterations,
  repeated calls, dynamic/static modes, and alternate wrappers or backends.
  Derive this matrix from the change rather than running every combination.
- Delegate execution of focused checks on the exact head and, for suspected
  regressions, the base under comparable conditions. Verify the original fix
  and meaningful adjacent cases. Distinguish new regressions, pre-existing bugs,
  intentional contract changes, and unverified hypotheses. Do not label code
  reading or the author's test report as independently reproduced evidence.
- Require handoffs to state the reviewed contracts and paths, exact revisions,
  executed checks and results, unexecuted checks and reasons, counterexample
  candidates, and how each candidate was resolved. Preserve these details when
  summarizing; a short "no issues found" verdict is insufficient.
- After independent assessments, reconcile disagreements using concrete evidence
  and targeted verification rather than majority vote. If relevant builds,
  backends, or tests are unavailable, complete the useful static review and mark
  the review incomplete with its specific coverage gaps. Do not issue an
  unqualified approval while material findings or verification gaps remain.
  Stronger models and passing tests reduce uncertainty but do not guarantee
  that the PR is correct. Existing approval/publication authorization still applies.

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
