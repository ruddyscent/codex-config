---
name: character-relation-map
description: Research, verify, and visualize character relationships in novels, films, television series, games, and plays. Use when asked to create a character relationship map, cast relationship diagram, or 인물관계도 with source-grounded characters and deterministic SVG labels.
---

# Character Relationship Map

## Purpose

Research, verify, structure, and visualize character relationships in narrative works such as novels, films, television series, games, and plays.

Accuracy of names, descriptions, and relationships takes precedence over visual richness.

## Non-negotiable rule

NEVER ask an image-generation model to render the final relationship map, character names, biographies, relationship labels, or arrows.

Image generation may be used only for visual assets such as character portraits or decorative backgrounds.

All semantic information MUST be rendered deterministically in SVG or another text-controlled vector format. PDF output should be derived from the verified structured data, not from generated raster text.

## Workflow

### 1. Discover characters

Search authoritative and useful sources, prioritizing:

- official excerpts or legally available text
- publisher and author material
- Google Books previews/indexes
- author interviews
- reputable literary reviews
- scholarly criticism
- chapter summaries and reading guides
- secondary reviews containing specific plot details

Collect potential named characters and recurring unnamed roles.

Do not assume every proper noun is a character.

### 2. Validate candidates

Classify each candidate as:

- `CONFIRMED`: supported by primary text, official material, or strong independent corroboration
- `PROBABLE`: character existence/role is strongly supported, but some details remain uncertain
- `TENTATIVE`: likely real but dependent on weak or limited secondary evidence
- `FALSE_POSITIVE`: not a character in the narrative

Typical false positives include:

- characters from a play, film, poem, or story performed or mentioned inside the work
- place names
- organizations
- historical references that do not function as characters
- translation artifacts
- names hallucinated by image-generation models

Never silently promote `TENTATIVE` to `CONFIRMED`.

### 3. Build the character registry

For each character, record when available:

- stable ID
- canonical display name
- original/English name
- aliases and alternate transliterations
- narrative role
- concise description
- affiliation/group
- first known appearance
- last known appearance
- related characters
- confidence level
- source notes

Unnamed but clearly relevant figures may be retained with descriptive labels such as `일본인 판사` if their role is supported by sources.

Use `templates/characters.yaml` as the starting structure.

### 4. Build relationships before visualization

Represent every relationship explicitly as an edge in structured data.

Example:

```yaml
relationships:
  - from: jungho
    to: okhee
    type: love
    label: 평생 이어지는 사랑과 인연
    confidence: CONFIRMED

  - from: okhee
    to: hanchol
    type: romance
    label: 연인
    confidence: CONFIRMED
```

Do not infer a relationship between two characters merely because both connect to a third character.

For example:

```text
정호 → 옥희 ↔ 한철
```

must NOT become:

```text
정호 ↔ 한철 = 연인
```

This rule is especially important for love triangles, family trees, political networks, and rival factions.

Use `templates/relationships.yaml` as the starting structure.

### 5. Generate portraits separately

When portraits are requested, generate them independently from the semantic diagram.

Before generation, record an `appearance` entry for each depicted character:
verified traits, user-specified traits, and unknown traits, with source notes for
verified claims. Include relevant age, build, hair, clothing, expression, and
setting. Distinguish user-directed artistic choices from facts supported by the
work; leave unknown traits unspecified rather than presenting stereotypes as
canon. Use the registry to build portrait prompts and retain accepted constraints
across style changes. No extra approval round is needed when the evidence and
user instructions already settle the choices.

Portrait prompts may incorporate verified traits such as:

- approximate age
- occupation
- social class
- nationality
- historical period
- clothing
- temperament
- physical characteristics explicitly supported by the work

For a unified illustrated map, prefer a consistent visual language, for example:

`hand-drawn historical graphic-novel portrait, watercolor and ink`

Portrait generation MUST NOT contain:

- character names
- relationship labels
- arrows
- biographies
- diagram text

Store portrait assets using stable character IDs, for example:

```text
portraits/
├── okhee.png
├── jungho.png
├── hanchol.png
└── yamada_genzo.png
```

The diagram renderer, not the image model, assigns names to portraits.

### 6. Compose deterministic SVG

Build the final map from the structured character and relationship data.

Render programmatically:

- portraits
- character names
- descriptions
- group labels
- relationship arrows
- relationship labels
- confidence markers
- legend
- accuracy/source note

Text should remain actual SVG text whenever practical.

Never use generated raster text for semantic labels.

### 7. Visual grouping

Group characters by narrative meaning rather than merely balancing node counts.

Useful groups include:

- protagonists/core characters
- family
- friends/community
- romantic relationships
- political or ideological groups
- workplace/community
- antagonists
- government/military groups
- historical groups
- minor characters

A character may connect across multiple groups, but should normally have one primary visual home.

### 8. Relationship encoding

Use a consistent visual legend. A suggested default is:

- red: romance/love
- blue: friendship
- green: alliance/cooperation/political mentorship
- gray: family
- orange: conflict/hostility
- purple: patronage/complex attachment
- dashed gray: uncertain, indirect, or weakly sourced relationship

These colors are defaults, not semantic evidence. Never create an edge merely to make the layout look balanced.

### 9. Confidence visualization

Suggested rendering:

- `CONFIRMED`: normal border
- `PROBABLE`: normal border plus a small `상당`/`probable` marker
- `TENTATIVE`: dashed gray border plus `보류`/`tentative`
- `FALSE_POSITIVE`: exclude from the diagram and retain only in research notes if useful

Do not hide uncertainty to improve aesthetics.

### 10. Layout strategy

Optimize layout only after the semantic graph is frozen.

Priorities:

1. correct relationships
2. readable labels
3. minimal line crossings
4. clear narrative grouping
5. visual balance

For large casts, use a landscape canvas. For roughly 20 or more characters, A2 landscape or an equivalently large SVG canvas is usually preferable to A4.

Avoid moving labels independently of their edges in ways that could make the relationship appear to belong to a neighboring line.

### 11. Quality assurance

Before delivery, verify every visible edge.

For each relationship:

```text
A --relationship--> B
```

check:

1. Is A a verified character?
2. Is B a verified character?
3. Is the relationship supported by the collected evidence?
4. Is the direction correct?
5. Is the relationship label attached to the correct edge?
6. Did layout changes alter the apparent meaning?
7. Did an image-generation model introduce any text or semantic relationship?
8. Is uncertainty displayed when evidence is incomplete?

Also verify:

- each portrait matches its registered age, build, hair, clothing, expression,
  and setting constraints; inspect the rendered asset, not just its prompt
- portrait or style corrections preserve accepted traits and the SVG names,
  descriptions, edge endpoints, and labels unless their change was requested
- unresolved appearance details remain distinguishable from verified facts
- aliases have not become duplicate characters
- titles/ranks have not become separate people
- characters from works-within-the-work have been removed
- historical people merely mentioned in dialogue have not been mistaken for cast members
- translated names and transliterations are normalized consistently

### 12. Output

Preferred deliverables:

- editable SVG
- PDF
- optional PNG preview
- optional YAML source data

When possible, retain the structured source files so corrections can be made without manually rebuilding the diagram.

Recommended project structure:

```text
character-relationship-map/
├── SKILL.md
├── characters.yaml
├── relationships.yaml
├── portraits/
├── output/
│   ├── character-map.svg
│   └── character-map.pdf
├── templates/
│   ├── characters.yaml
│   └── relationships.yaml
├── scripts/
│   └── build_map.py
└── references/
    └── schema.md
```

## Search-only mode

When the user cannot provide the source text, clearly distinguish between a complete textual audit and a search-grounded reconstruction.

In search-only mode:

- search more deeply before claiming completeness
- triangulate unusual names across multiple sources
- use primary excerpts whenever available
- distinguish `name exists` from `role/relationship verified`
- explicitly label unresolved characters
- never describe the result as an exhaustive cast list unless the evidence supports that claim

## Accuracy principle

When visual attractiveness conflicts with semantic accuracy, semantic accuracy always wins.

Generated portraits are decorative evidence-neutral assets. Names, descriptions, identities, and relationships come only from the verified structured data.
