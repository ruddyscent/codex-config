# herdr Pane Operations

Read this reference only when the management session is Codex CLI running
inside a herdr pane. herdr usage alone does not establish that the agent is CLI.

- When the management session runs in herdr, run each concurrent worker in a
  separate pane. Track each pane's task and state. After a worker finishes,
  reassign its idle pane to follow-up work before creating another pane, with
  an explicit handoff of scope, context, working directory, and model settings.
  Reuse the pane independently of the agent conversation: continue the existing
  conversation for related follow-up work, but start a fresh worker session
  in that pane for unrelated work. Do not interrupt active work or carry stale
  task assumptions into a new assignment.
- Keep completed panes idle and available for reuse; stop unneeded workers
  without closing reusable panes.
