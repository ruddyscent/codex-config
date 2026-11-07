# PyTorch Review Context

Read this reference only when reviewing pytorch/pytorch or a confirmed fork
whose changes use PyTorch's infrastructure and conventions.

- At the selected review revision, inspect applicable repository instructions,
  `CONTRIBUTING.md`, and the relevant guidance in:
  - `.claude/skills/pr-review/SKILL.md`
  - `.claude/skills/pr-review/review-checklist.md`
  - `.claude/skills/pr-review/bc-guidelines.md`
- Record which revision supplies those documents. If unavailable there, report
  the gap and identify the revision of any fallback; do not silently mix current
  main guidance with an older PR. Read only relevant checklist sections.
- Use the documents as project review context. Do not inherit Claude invocation
  modes, fixed agent counts, blanket must-fix severity, or instructions to omit
  relevant CI failures. Repository-specific technical requirements remain subject
  to the actual code and contract; they do not replace this skill's CLI boundary,
  manager settings, independent review, or authorization rules.
- Route checks by affected subsystem. Operator changes may require dispatch,
  TensorIterator, OpInfo, or autograd investigation; compiler changes may require
  functionalization, IR consumers, and affected wrappers/backends. Investigate
  only applicable infrastructure and verify its current implementation.
- Verify compatibility and supported platform/Python versions at that revision.
  Do not embed changing version tables or project policy copies in this skill.
- Follow the common review process to consolidate and independently verify
  candidates. Project checklists supplement, rather than replace, contract
  analysis, counterexample discovery, and focused execution checks.

Upstream entry point:
[PyTorch pr-review](https://github.com/pytorch/pytorch/tree/main/.claude/skills/pr-review).
