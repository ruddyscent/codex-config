# Evidence-Based PR Review

Read this reference for PR reviews. The manager assigns the steps below to
workers; workers do not recursively delegate. Use the skill's stronger staffing
and independence requirements for high-risk changes.

## Context and coverage

- Read the issue, requirements, diff, repository guidance, and relevant existing
  discussions. Treat the author's explanation as a hypothesis to verify.
  Apply the skill's Issue and PR Evidence on Resume procedure to PR comments,
  reviews, inline threads, and replies as well as issue comments. For independent
  discovery, keep prior findings and verdicts with the manager until initial
  assessments are recorded; reconcile the discussion history afterward.
- Assign coverage of changed behavior and inspect unchanged surrounding code,
  callers, consumers, and analogous implementations. Account for every changed
  region; a checklist label alone is not evidence that it was reviewed.
- Check design and contracts as well as implementation: inputs, outputs,
  ownership, lifecycle, invariants, and communication between components.
  Investigate local conventions, but do not assume existing patterns are correct
  or that deviations are defects without a concrete consequence.
- For validators, collectors, or replay/checkpoint changes, derive the required
  state and comparison rules from the producers, consumers, and controlling
  contract. Compare that inventory with what the implementation actually checks;
  passing comparisons cannot detect state omitted from the comparison entirely.
  Distinguish exact identity or clock requirements from permitted numerical
  tolerances before proposing a defect or a stricter test. Treat the manager's
  acceptance matrix as reviewable context, not proof of complete coverage.
- List relevant user-visible changes, including return values, defaults, errors,
  accepted/rejected inputs, side effects, and caller compatibility. Distinguish
  intentional changes with a migration plan from accidental regressions.
- Select project-specific checks only where the diff or affected consumers make
  them relevant. Scale parallel workers to independent risk areas rather than
  using a fixed worker count or loading every checklist into every worker.

## Discovery, consolidation, and fact-checking

- Independent discovery searches for missed defects. For high-risk reviews,
  keep initial assessments separate as required by the skill before comparing
  findings. Candidate verification below is a different step: it tests an
  explicit claim and therefore may receive that claim and its evidence.
- Record candidates with revision, location, trigger, violated contract, impact,
  supporting evidence, and uncertainty. Connect findings in unchanged code to
  the specific changed behavior that exposes them.
- Consolidate candidates before verification. Combine descriptions of the same
  root cause or a single corrective change, retaining their distinct impacts.
  Do not collapse independent defects just because they share a line. Repetition
  by multiple reviewers is not independent proof of correctness.
- Assign each surviving defect claim to a separate verifier who did not originate
  it. Give the verifier the claim, relevant source, revisions, and evidence, and
  ask it to challenge assumptions and inspect callers and surrounding code.
  Batch related claims for one verifier when this preserves independence and
  avoids duplicate context loading; do not create one agent per raw candidate.
- Record each verdict as supported, rejected, needs revision, or unresolved,
  with reasons. Remove rejected findings and re-check materially revised claims.
  Label unresolved claims as questions or hypotheses, not confirmed blockers.
- Verify behavioral claims with focused head/base checks where feasible. Keep
  the high-risk execution requirements intact. Distinguish the author's reports,
  CI evidence, local reproduction, and static reasoning. Investigate relevant CI
  failures; avoid duplicating routine lint or formatting output as review findings.

## Reporting

- Report each finding once, with actionable location, consequence, supporting
  evidence, severity, and confidence. Separate defects from optional improvements
  and open questions; not every observation is a must-fix.
- Include a concise coverage/verification summary and exact revisions even when
  there are no findings. State missing checks and material limitations. Do not
  equate "no findings" with proven correctness or hide gaps to keep output short.
- Reconcile disagreements through evidence, not votes, and follow the skill's
  completion and approval rules. Posting a review still requires authorization.

## Sources and adaptation

This procedure synthesizes ideas from PyTorch's
[PR review skill](https://github.com/pytorch/pytorch/blob/main/.claude/skills/pr-review/SKILL.md)
and [compatibility guidance](https://github.com/pytorch/pytorch/blob/main/.claude/skills/pr-review/bc-guidelines.md),
reviewed on 2026-09-06. It is not a verbatim copy or a claim that every PyTorch
rule applies to other repositories. Keep the host, model, authorization, and
verification policies of this skill when adapting project review guidance.
