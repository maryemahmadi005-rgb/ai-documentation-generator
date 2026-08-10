# Module : src/content-linter/tests/unit

47 fichier(s), 7 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : getFormattedDate, isExcluded, isPathExcluded, md, shouldIncludeInReport, test, validCard
- **Dépendances** : ../../lib/helpers/rule-utils, ../../lib/init-test, ../../lib/linting-rules/code-annotation-comment-spacing, ../../lib/linting-rules/code-annotations, ../../lib/linting-rules/ctas-schema, ../../lib/linting-rules/frontmatter-curly-quotes, ../../lib/linting-rules/frontmatter-docs-team-metrics, ../../lib/linting-rules/frontmatter-hero-image, ../../lib/linting-rules/frontmatter-hidden-docs, ../../lib/linting-rules/frontmatter-intro-links, ../../lib/linting-rules/frontmatter-schema, ../../lib/linting-rules/github-owned-action-references

## Détail des fichiers

### `code-annotation-comment-spacing.ts`

Module TypeScript. Nombre de lignes: 239.

**Fonctions** : test
**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/code-annotation-comment-spacing, express

### `code-annotations.ts`

Module TypeScript. Nombre de lignes: 30.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/code-annotations

### `ctas-schema.ts`

Module TypeScript. Nombre de lignes: 151.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/ctas-schema

### `early-access-references.ts`

Module TypeScript. Nombre de lignes: 50.

**Dépendances** : vitest, ../../lib/init-test

### `expired-content.ts`

Module TypeScript. Nombre de lignes: 141.

**Fonctions** : getFormattedDate
**Dépendances** : vitest, ../../lib/init-test

### `frontmatter-children.ts`

Module TypeScript. Nombre de lignes: 43.

**Dépendances** : vitest, @/content-linter/lib/init-test, @/content-linter/lib/linting-rules/frontmatter-children

### `frontmatter-content-type.ts`

Module TypeScript. Nombre de lignes: 180. Elements detectés: function md

**Fonctions** : md
**Dépendances** : vitest, @/content-linter/lib/init-test

### `frontmatter-curly-quotes.ts`

Module TypeScript. Nombre de lignes: 86.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/frontmatter-curly-quotes

### `frontmatter-docs-team-metrics.ts`

Module TypeScript. Nombre de lignes: 34.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/frontmatter-docs-team-metrics

### `frontmatter-hero-image.ts`

Module TypeScript. Nombre de lignes: 130.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/frontmatter-hero-image

### `frontmatter-hidden-docs.ts`

Module TypeScript. Nombre de lignes: 30.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/frontmatter-hidden-docs

### `frontmatter-intro-links.ts`

Module TypeScript. Nombre de lignes: 114.

**Dépendances** : path, vitest, ../../lib/init-test, ../../lib/linting-rules/frontmatter-intro-links

### `frontmatter-landing-carousels.ts`

Module TypeScript. Nombre de lignes: 134.

**Dépendances** : vitest, @/content-linter/lib/init-test, @/content-linter/lib/linting-rules/frontmatter-landing-carousels

### `frontmatter-rest-api-category.ts`

Module TypeScript. Nombre de lignes: 73.

**Dépendances** : vitest, ../../lib/init-test

### `frontmatter-schema.ts`

Module TypeScript. Nombre de lignes: 93.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/frontmatter-schema

### `frontmatter-search-replace.ts`

Module TypeScript. Nombre de lignes: 102.

**Dépendances** : vitest, markdownlint, markdownlint-rule-search-replace, ../../style/github-docs

### `frontmatter-versions-whitespace.ts`

Module TypeScript. Nombre de lignes: 251.

**Dépendances** : vitest, @/content-linter/lib/init-test, @/content-linter/lib/linting-rules/frontmatter-versions-whitespace

### `github-owned-action-references.ts`

Module TypeScript. Nombre de lignes: 22.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/github-owned-action-references

### `hardcoded-data-variable.ts`

Module TypeScript. Nombre de lignes: 23.

**Dépendances** : vitest, @/content-linter/lib/init-test, @/content-linter/lib/linting-rules/hardcoded-data-variable

### `image-alt-text-end-punctuation.ts`

Module TypeScript. Nombre de lignes: 65.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/image-alt-text-end-punctuation

### `image-alt-text-exclude-start-words.ts`

Module TypeScript. Nombre de lignes: 45.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/image-alt-text-exclude-start-words

### `image-alt-text-length.ts`

Module TypeScript. Nombre de lignes: 42.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/image-alt-text-length, ../../types

### `image-file-kebab-case.ts`

Module TypeScript. Nombre de lignes: 27.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/image-file-kebab-case

### `image-no-gif.ts`

Module TypeScript. Nombre de lignes: 31.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/image-no-gif

### `internal-links-no-lang.ts`

Module TypeScript. Nombre de lignes: 37.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/internal-links-no-lang, ../../types

### `internal-links-old-version.ts`

Module TypeScript. Nombre de lignes: 31.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/internal-links-old-version, ../../types

### `internal-links-slash.ts`

Module TypeScript. Nombre de lignes: 46.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/internal-links-slash

### `journey-tracks.ts`

Module TypeScript. Nombre de lignes: 138.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/journey-tracks-liquid, ../../lib/linting-rules/journey-tracks-guide-path-exists, ../../lib/linting-rules/journey-tracks-unique-ids

### `link-punctuation.ts`

Module TypeScript. Nombre de lignes: 50.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/link-punctuation

### `link-quotation.ts`

Module TypeScript. Nombre de lignes: 34.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/link-quotation, ../../types

### `lint-report-exclusions.ts`

Module TypeScript. Nombre de lignes: 151. Elements detectés: function isPathExcluded, function shouldIncludeInReport

**Fonctions** : isPathExcluded, shouldIncludeInReport, isExcluded
**Dépendances** : vitest, ../../lib/helpers/rule-utils

### `liquid-data-tags.ts`

Module TypeScript. Nombre de lignes: 70.

**Dépendances** : path, vitest, ../../lib/init-test, @/content-linter/types

### `liquid-ifversion-versions.ts`

Module TypeScript. Nombre de lignes: 281.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/liquid-versioning, ../../lib/linting-rules/liquid-ifversion-versions, @/versions/lib/enterprise-server-releases

### `liquid-quoted-conditional-args.ts`

Module TypeScript. Nombre de lignes: 124.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/liquid-quoted-conditional-arg

### `liquid-syntax.ts`

Module TypeScript. Nombre de lignes: 82.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/liquid-syntax

### `liquid-tag-whitespace.ts`

Module TypeScript. Nombre de lignes: 62.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/liquid-tag-whitespace

### `liquid-versioning.ts`

Module TypeScript. Nombre de lignes: 108.

**Dépendances** : path, vitest, ../../lib/init-test, ../../lib/linting-rules/liquid-versioning, @/versions/lib/enterprise-server-releases

### `outdated-release-phase-terminology.ts`

Module TypeScript. Nombre de lignes: 143.

**Dépendances** : vitest, @/content-linter/lib/init-test, @/content-linter/lib/linting-rules/outdated-release-phase-terminology

### `rai-app-card-structure.ts`

Module TypeScript. Nombre de lignes: 177. Elements detectés: function validCard

**Fonctions** : validCard
**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/rai-app-card-structure

### `rai-resuable-usage.ts`

Module TypeScript. Nombre de lignes: 92.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/rai-reusable-usage

### `rule-filtering.ts`

Module TypeScript. Nombre de lignes: 53.

**Dépendances** : vitest, ../../scripts/lint-content

### `search-replace.ts`

Module TypeScript. Nombre de lignes: 183.

**Dépendances** : vitest, markdownlint-rule-search-replace, ../../lib/init-test, ../../style/github-docs

### `table-column-integrity-simple.ts`

Module TypeScript. Nombre de lignes: 254.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/table-column-integrity

### `table-liquid-versioning.ts`

Module TypeScript. Nombre de lignes: 18.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/table-liquid-versioning

### `third-party-action-pinning.ts`

Module TypeScript. Nombre de lignes: 108.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/third-party-action-pinning

### `third-party-actions-reusable.ts`

Module TypeScript. Nombre de lignes: 342.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/third-party-actions-reusable

### `yaml-scheduled-jobs.ts`

Module TypeScript. Nombre de lignes: 96.

**Dépendances** : vitest, ../../lib/init-test, ../../lib/linting-rules/yaml-scheduled-jobs
