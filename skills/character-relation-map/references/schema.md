# Data Schema

## Character

Required:

- `id`: stable machine-readable identifier
- `name`: canonical display name
- `confidence`: `CONFIRMED`, `PROBABLE`, `TENTATIVE`, or `FALSE_POSITIVE`

Recommended:

- `original_name`
- `aliases`
- `role`
- `group`
- `description`
- `first_appearance`
- `last_appearance`
- `appearance`: optional portrait constraints
  - `verified_traits`: list of `{trait, value, source}` records
  - `user_specified_traits`: list of `{trait, value}` records; distinguish artistic
    direction from independently verified facts
  - `unknown_traits`: list of relevant traits lacking evidence; do not silently
    promote artistic guesses to verified facts
- `portrait`
- `sources`

## Relationship

Required:

- `from`
- `to`
- `type`
- `label`
- `confidence`

Optional:

- `direction`: `directed` or `mutual`
- `period`
- `notes`
- `sources`

## Stable IDs

IDs should remain stable even if the display name changes. Prefer lowercase ASCII with underscores, for example:

- `okhee`
- `nam_jungho`
- `kim_hanchol`
- `yamada_genzo`

This allows portrait assets and relationships to remain correctly attached after name corrections.
