# Module : src/content-linter/lib/linting-rules

46 fichier(s), 57 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : GHD018, GHD040, GHD060, checkForDisclaimer, checkForUnwantedWhitespace, countColumns, decorateCondTagItems, dirToContentType, extractHeadings, extractTemplateBlock, findOutdatedTerminologyMatches, findThirdPartyActions, forToken, getApplicableVersionFromLiquidTag, getCleanedValue
- **Dépendances** : ../../types, ../helpers/liquid-utils, ../helpers/utils, @/automated-pipelines/lib/update-markdown, @/content-linter/lib/helpers/utils, @/content-linter/lib/linting-rules/frontmatter-hidden-docs, @/content-linter/lib/linting-rules/image-alt-text-end-punctuation, @/content-linter/lib/linting-rules/image-alt-text-exclude-start-words, @/content-linter/lib/linting-rules/image-alt-text-length, @/content-linter/lib/linting-rules/image-file-kebab-case, @/content-linter/lib/linting-rules/internal-links-no-lang, @/content-linter/lib/linting-rules/internal-links-old-version

## Détail des fichiers

### `code-annotation-comment-spacing.ts`

Module TypeScript. Nombre de lignes: 92.

**Dépendances** : markdownlint-rule-helpers, @/content-linter/types

### `code-annotations.ts`

Module TypeScript. Nombre de lignes: 29.

**Dépendances** : markdownlint-rule-helpers, @/content-linter/lib/helpers/utils, @/content-linter/types

### `ctas-schema.ts`

Module TypeScript. Nombre de lignes: 120.

**Dépendances** : markdownlint-rule-helpers, ajv, @/content-render/scripts/cta-builder, @/data-directory/lib/data-schemas/ctas, ../../types

### `early-access-references.ts`

Module TypeScript. Nombre de lignes: 85.

**Dépendances** : markdownlint-rule-helpers, js-yaml, ../helpers/utils, @/content-linter/types

### `expired-content.ts`

Module TypeScript. Nombre de lignes: 85.

**Dépendances** : markdownlint-rule-helpers, @/content-linter/types

### `frontmatter-children.ts`

Module TypeScript. Nombre de lignes: 83. Elements detectés: function isValidChildPath

**Fonctions** : isValidChildPath
**Dépendances** : fs, path, markdownlint-rule-helpers, ../helpers/utils, @/content-linter/types

### `frontmatter-content-type.ts`

Module TypeScript. Nombre de lignes: 139. Elements detectés: function getQualifyingProducts, function dirToContentType

**Fonctions** : getQualifyingProducts, isKnownDir, dirToContentType, resetCache
**Dépendances** : fs, path, markdownlint-rule-helpers, ../helpers/utils, @/frame/lib/frontmatter, @/content-linter/types

### `frontmatter-curly-quotes.ts`

Module TypeScript. Nombre de lignes: 43.

**Dépendances** : markdownlint-rule-helpers, ../helpers/utils, @/content-linter/types

### `frontmatter-docs-team-metrics.ts`

Module TypeScript. Nombre de lignes: 34.

**Dépendances** : markdownlint-rule-helpers, @/content-linter/types, ../helpers/utils

### `frontmatter-hero-image.ts`

Module TypeScript. Nombre de lignes: 94. Elements detectés: function getValidHeroImages

**Fonctions** : getValidHeroImages
**Dépendances** : fs, path, markdownlint-rule-helpers, ../helpers/utils, @/content-linter/types

### `frontmatter-hidden-docs.ts`

Module TypeScript. Nombre de lignes: 31.

**Dépendances** : markdownlint-rule-helpers, ../../types, ../helpers/utils

### `frontmatter-intro-links.ts`

Module TypeScript. Nombre de lignes: 56. Elements detectés: function getValidIntroLinksKeys

**Fonctions** : getValidIntroLinksKeys
**Dépendances** : markdownlint-rule-helpers, ../helpers/utils, @/data-directory/lib/get-data, @/content-linter/types

### `frontmatter-landing-carousels.ts`

Module TypeScript. Nombre de lignes: 110. Elements detectés: function isValidArticlePath

**Fonctions** : isValidArticlePath
**Dépendances** : fs, path, markdownlint-rule-helpers, ../helpers/utils, @/content-linter/types

### `frontmatter-rest-api-category.ts`

Module TypeScript. Nombre de lignes: 106. Elements detectés: function getValidCategories

**Fonctions** : getValidCategories, resetCache
**Dépendances** : fs, path, @gr2m/gray-matter, markdownlint-rule-helpers, ../helpers/utils, @/content-linter/types

### `frontmatter-schema.ts`

Module TypeScript. Nombre de lignes: 74.

**Fonctions** : query
**Dépendances** : markdownlint-rule-helpers, lodash-es, ../helpers/utils, @/frame/lib/frontmatter, @/frame/lib/read-frontmatter, ../../types

### `frontmatter-versions-whitespace.ts`

Module TypeScript. Nombre de lignes: 85. Elements detectés: function checkForUnwantedWhitespace, function getCleanedValue

**Fonctions** : checkForUnwantedWhitespace, getCleanedValue
**Dépendances** : markdownlint-rule-helpers, @/content-linter/lib/helpers/utils, @/content-linter/types

### `github-owned-action-references.ts`

Module TypeScript. Nombre de lignes: 36.

**Dépendances** : markdownlint-rule-helpers, ../../types, ../helpers/utils

### `hardcoded-data-variable.ts`

Module TypeScript. Nombre de lignes: 39.

**Dépendances** : markdownlint-rule-helpers, ../../types, ../helpers/utils, @/frame/lib/read-frontmatter

### `image-alt-text-end-punctuation.ts`

Module TypeScript. Nombre de lignes: 34.

**Fonctions** : forToken
**Dépendances** : ../../types

### `image-alt-text-exclude-start-words.ts`

Module TypeScript. Nombre de lignes: 37.

**Fonctions** : forToken
**Dépendances** : markdownlint-rule-helpers, ../helpers/utils, ../../types

### `image-alt-text-length.ts`

Module TypeScript. Nombre de lignes: 44.

**Fonctions** : forToken
**Dépendances** : markdownlint-rule-helpers, ../../types, @/content-render/index, @/versions/lib/all-versions, ../helpers/utils

### `image-file-kebab-case.ts`

Module TypeScript. Nombre de lignes: 25.

**Fonctions** : forToken
**Dépendances** : @/content-linter/lib/helpers/utils, @/content-linter/types

### `image-no-gif.ts`

Module TypeScript. Nombre de lignes: 25.

**Fonctions** : forToken
**Dépendances** : markdownlint-rule-helpers, @/content-linter/lib/helpers/utils, @/content-linter/types

### `index.ts`

Module TypeScript. Nombre de lignes: 126.

**Dépendances** : markdownlint-rule-search-replace, @github/markdownlint-github, @/content-linter/lib/linting-rules/image-alt-text-end-punctuation, @/content-linter/lib/linting-rules/image-file-kebab-case, @/content-linter/lib/linting-rules/image-alt-text-length, @/content-linter/lib/linting-rules/internal-links-no-lang, @/content-linter/lib/linting-rules/internal-links-slash, @/content-linter/lib/linting-rules/image-alt-text-exclude-start-words, @/content-linter/lib/linting-rules/link-punctuation, @/content-linter/lib/linting-rules/frontmatter-hidden-docs, @/content-linter/lib/linting-rules/yaml-scheduled-jobs, @/content-linter/lib/linting-rules/internal-links-old-version

### `internal-links-no-lang.ts`

Module TypeScript. Nombre de lignes: 51.

**Dépendances** : markdownlint-rule-helpers, ../helpers/utils, @/languages/lib/languages, ../../types

### `internal-links-old-version.ts`

Module TypeScript. Nombre de lignes: 57.

**Dépendances** : markdownlint-rule-helpers, ../helpers/utils, ../../types

### `internal-links-slash.ts`

Module TypeScript. Nombre de lignes: 48.

**Dépendances** : markdownlint-rule-helpers, ../helpers/utils, ../../types

### `journey-tracks-guide-path-exists.ts`

Module TypeScript. Nombre de lignes: 79. Elements detectés: function isValidGuidePath

**Fonctions** : isValidGuidePath
**Dépendances** : fs, path, markdownlint-rule-helpers, ../helpers/utils, @/content-linter/types

### `journey-tracks-liquid.ts`

Module TypeScript. Nombre de lignes: 105.

**Dépendances** : markdownlint-rule-helpers, ../helpers/utils, @/content-render/index, @/content-linter/types

### `journey-tracks-unique-ids.ts`

Module TypeScript. Nombre de lignes: 64. Elements detectés: function getTrackLineNumber

**Fonctions** : GHD060, getTrackLineNumber
**Dépendances** : markdownlint-rule-helpers, ../helpers/utils, @/content-linter/types

### `link-punctuation.ts`

Module TypeScript. Nombre de lignes: 45.

**Dépendances** : markdownlint-rule-helpers, ../../types, ../helpers/utils

### `link-quotation.ts`

Module TypeScript. Nombre de lignes: 70.

**Dépendances** : markdownlint-rule-helpers, ../helpers/utils, lodash-es, ../../types

### `liquid-data-tags.ts`

Module TypeScript. Nombre de lignes: 129.

**Fonctions** : getData
**Dépendances** : markdownlint-rule-helpers, liquidjs, @/data-directory/lib/get-data, @/content-linter/types

### `liquid-ifversion-versions.ts`

Module TypeScript. Nombre de lignes: 533.

**Fonctions** : setLiquidErrors, getApplicableVersionFromLiquidTag, initTagObject, decorateCondTagItems, updateConditionals, processConditionals
**Dépendances** : markdownlint-rule-helpers, liquidjs, ../helpers/utils, @/versions/lib/get-applicable-versions, @/versions/lib/all-versions, lodash-es, @/automated-pipelines/lib/update-markdown, @/versions/lib/enterprise-server-releases, @/content-linter/types

### `liquid-quoted-conditional-arg.ts`

Module TypeScript. Nombre de lignes: 65.

**Dépendances** : liquidjs, markdownlint-rule-helpers, ../helpers/liquid-utils, ../helpers/utils, ../../types

### `liquid-syntax.ts`

Module TypeScript. Nombre de lignes: 105. Elements detectés: function getErrorMessageInfo

**Fonctions** : GHD018, getErrorMessageInfo
**Dépendances** : markdownlint-rule-helpers, ../helpers/utils, @/content-render/index, @/languages/lib/render-with-fallback, @/content-linter/types

### `liquid-tag-whitespace.ts`

Module TypeScript. Nombre de lignes: 65.

**Dépendances** : liquidjs, ../helpers/liquid-utils, ../helpers/utils, ../../types

### `liquid-versioning.ts`

Module TypeScript. Nombre de lignes: 263. Elements detectés: function isAllVersions, function memoize<T>

**Fonctions** : isAllVersions, validateIfversionConditionals, validateIfversionConditionalsVersions, getVersionsObject, lowestVersion
**Dépendances** : semver, liquidjs, markdownlint-rule-helpers, ../helpers/utils, @/versions/lib/all-versions, @/versions/lib/enterprise-server-releases, @/content-render/liquid/ifversion-supported-operators, @/data-directory/lib/get-data, @/versions/lib/get-applicable-versions, ../helpers/liquid-utils, @/content-linter/types

### `outdated-release-phase-terminology.ts`

Module TypeScript. Nombre de lignes: 133. Elements detectés: function findOutdatedTerminologyMatches

**Fonctions** : findOutdatedTerminologyMatches
**Dépendances** : markdownlint-rule-helpers, @/content-linter/lib/helpers/utils, @/frame/lib/read-frontmatter, @/content-linter/types

### `rai-app-card-structure.ts`

Module TypeScript. Nombre de lignes: 310. Elements detectés: function extractTemplateBlock, function headingToPattern, function headingLabel

**Fonctions** : extractTemplateBlock, headingToPattern, headingLabel, parseTemplate, getTemplate, extractHeadings, validateH2Sections, validateH3Subsections, validateReusables, isFileRaiCard
**Dépendances** : fs, path, markdownlint-rule-helpers, ../helpers/utils, ../../types

### `rai-reusable-usage.ts`

Module TypeScript. Nombre de lignes: 69. Elements detectés: function isFileRai

**Fonctions** : isFileRai
**Dépendances** : markdownlint-rule-helpers, liquidjs, path, ../helpers/utils, ../helpers/liquid-utils, ../../types

### `table-column-integrity.ts`

Module TypeScript. Nombre de lignes: 122. Elements detectés: function countColumns, function isLiquidOnlyRow

**Fonctions** : countColumns, isLiquidOnlyRow
**Dépendances** : markdownlint-rule-helpers, ../helpers/utils, @/frame/lib/read-frontmatter, @/content-linter/types

### `table-liquid-versioning.ts`

Module TypeScript. Nombre de lignes: 78. Elements detectés: function isPreviousLineIndented

**Fonctions** : GHD040, isPreviousLineIndented
**Dépendances** : markdownlint-rule-helpers, @/content-linter/types

### `third-party-action-pinning.ts`

Module TypeScript. Nombre de lignes: 90. Elements detectés: function getWorkflowSteps, function getLineNumber

**Fonctions** : getWorkflowSteps, getLineNumber
**Dépendances** : markdownlint-rule-helpers, js-yaml, @/content-render/index, @/versions/lib/all-versions, @/content-linter/types

### `third-party-actions-reusable.ts`

Module TypeScript. Nombre de lignes: 96. Elements detectés: function findThirdPartyActions, function isExampleOrGitHubAction, function checkForDisclaimer

**Fonctions** : findThirdPartyActions, isExampleOrGitHubAction, checkForDisclaimer
**Dépendances** : markdownlint-rule-helpers, @/content-linter/types

### `yaml-scheduled-jobs.ts`

Module TypeScript. Nombre de lignes: 64. Elements detectés: function getLineNumber

**Fonctions** : getLineNumber
**Dépendances** : js-yaml, markdownlint-rule-helpers, @/content-render/index, @/versions/lib/all-versions, ../../types
