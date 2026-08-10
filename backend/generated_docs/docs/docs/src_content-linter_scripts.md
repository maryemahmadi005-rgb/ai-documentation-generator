# Module : src/content-linter/scripts

6 fichier(s), 30 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : chalkFunColors, checkString, cleanPaths, formatResult, getChangedFiles, getCountBySeverity, getErrorCountByFile, getFilesToLint, getFormattedResults, getMarkdownLintConfig, getPages, getReusableFiles, getSearchReplaceRules, getSeverity, getVariables
- **Dépendances** : ../lib/default-markdownlint-options, ../lib/helpers/get-rules, ../style/github-docs, ../types, @/content-linter/lib/helpers/liquid-utils, @/content-linter/lib/helpers/rule-utils, @/frame/lib/page-data, @/frame/lib/read-frontmatter, @/workflows/get-env-inputs, @/workflows/github, @/workflows/issue-report, @/workflows/walk-files

## Détail des fichiers

### `disable-rules.ts`

Module TypeScript. Nombre de lignes: 69.

**Dépendances** : fs, child_process

### `find-unsed-variables.ts`

Module TypeScript. Nombre de lignes: 143. Elements detectés: function getVariables

**Fonctions** : main, getVariables, getPages, getReusableFiles, checkString
**Dépendances** : fs, js-yaml, commander, @/frame/lib/page-data, liquidjs, @/frame/lib/read-frontmatter, @/content-linter/lib/helpers/liquid-utils, @/workflows/walk-files

### `generate-docs.ts`

Module TypeScript. Nombre de lignes: 77. Elements detectés: function main, function getSearchReplaceRules

**Fonctions** : main, getSearchReplaceRules
**Dépendances** : fs, ../types, ../lib/helpers/get-rules

### `lint-content.ts`

Module TypeScript. Nombre de lignes: 781.

**Fonctions** : main, pluralize, getFilesToLint, cleanPaths, isInDir, reportSummaryByRule, getFormattedResults, getWarningCountByFile, getErrorCountByFile, getCountBySeverity, formatResult, getChangedFiles, listRules, getMarkdownLintConfig, getSeverity
**Dépendances** : fs, path, child_process, commander, markdownlint, markdownlint-rule-helpers, boxen, ora, @/workflows/walk-files, ../lib/helpers/get-rules, ../style/github-docs, ../lib/default-markdownlint-options

### `lint-report.ts`

Module TypeScript. Nombre de lignes: 132. Elements detectés: function shouldIncludeInReport

**Fonctions** : shouldIncludeInReport, main
**Dépendances** : commander, fs, @actions/core, @/workflows/github, @/workflows/get-env-inputs, @/workflows/issue-report, @/content-linter/lib/helpers/rule-utils

### `pretty-print-results.ts`

Module TypeScript. Nombre de lignes: 172. Elements detectés: function isNumber, function shorten, function label

**Fonctions** : isNumber, shorten, prettyPrintResults, label, chalkFunColors, indentWrappedString
**Dépendances** : chalk
