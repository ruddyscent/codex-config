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

## Pane Layout

- Preserve the management pane's full available height for reasoning output
  and user interaction. Keep it on the left and place workers on the right.
  Inspect the existing layout before creating panes; reuse a suitable worker
  area rather than splitting the management pane again.
- When starting from a single management pane, create the first worker with
  `herdr pane split --pane MANAGER_ID --direction right --ratio 0.65 --no-focus`,
  replacing `MANAGER_ID` with its stable pane ID. The ratio keeps approximately
  65% of the width for the manager; adjust the width to the terminal size and
  user preference while preserving the manager's height.
- Create additional workers by splitting panes within the right-hand worker
  area using `--direction down` and an appropriate `--ratio`. Never split the
  management pane downward to make room for workers. Target explicit worker
  pane IDs so a change in focus cannot split the wrong pane.
- Use `--no-focus` when creating worker panes to preserve the user's current
  focus. Verify the resulting layout after changes. Preserve this arrangement
  during pane reuse and manager handoff without restarting active sessions;
  an explicit user layout request takes precedence.
