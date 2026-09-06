# herdr Pane Operations

Read this reference only when the management session is Codex CLI running
inside a herdr pane. herdr usage alone does not establish that the agent is CLI.

- The first pane need not be the management pane. Follow the skill's single
  manager handoff procedure when assigning a new management pane. A new pane
  alone does not clear context; start a fresh Codex CLI session when needed.
- Give the management pane a stable, unambiguous name. Name worker panes
  `<management-pane-name>-<number>`, starting at 1 for each manager (for example,
  `review-1`, `review-2`). Allocate an unused number without colliding with an
  existing pane. Keep the name and number when reassigning an idle worker pane.
- Include pane names, stable pane identifiers, tasks, states, and assigned models
  in the handoff roster. Preserve the logical manager name during handoff when
  the host permits it; distinguish the former pane so the name is unambiguous.
  If the manager name must change, update worker names to the new prefix while
  preserving their numbers and identities without restarting active workers.
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
