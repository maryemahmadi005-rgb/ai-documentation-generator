# Module : src/ghes-releases/scripts

7 fichier(s), 39 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : addRepoLabels, buildCommentBody, buildMarker, createDeprecationIssue, createIssue, createReleaseIssue, extractChangelogPrUrl, extractSourceNotes, fetchChangelogPrBody, fetchReleaseIssues, findChangelogPr, findCopilotCli, getFeatureVersionsObject, getNextReleaseNumber, getNumberDaysUntilMilestone
- **Dépendances** : @/data-directory/lib/data-directory, @/types, @/versions/lib/all-versions, @/versions/lib/enterprise-server-releases, @/workflows/git-utils, @/workflows/github, @gr2m/gray-matter, child_process, commander, fs, fs/promises, js-yaml

## Détail des fichiers

### `README.md`

### `create-enterprise-issue.ts`

Module TypeScript. Nombre de lignes: 374.

**Fonctions** : run, createDeprecationIssue, createReleaseIssue, createIssue, updateIssue, addRepoLabels, getReleaseTemplates, getReleaseTemplateContext, getRenderedTemplate, getNumberDaysUntilMilestone, getNextReleaseNumber, isExistingIssue, getReleaseDates
**Dépendances** : fs, path, liquidjs, walk-sync, @gr2m/gray-matter, @/versions/lib/enterprise-server-releases, @/workflows/git-utils, @/workflows/github

### `generate-release-notes.ts`

Module TypeScript. Nombre de lignes: 793. Elements detectés: function loadFeatureHeadings, function gh, function fetchReleaseIssues

**Fonctions** : loadFeatureHeadings, gh, fetchReleaseIssues, extractChangelogPrUrl, fetchChangelogPrBody, searchChangelogPr, findChangelogPr, findCopilotCli, parseTitleTag, runAgent, sleep, runAgentWithRetry, writeCurrentOutput
**Dépendances** : commander, child_process, fs, os, path, ora, js-yaml

### `notify-release-pms.ts`

Module TypeScript. Nombre de lignes: 339. Elements detectés: function ghRead, function ghWrite

**Fonctions** : ghRead, ghWrite, parseSourceNotes, extractSourceNotes, buildCommentBody, buildMarker
**Dépendances** : commander, child_process, fs, path, ora

### `release-banner.ts`

Module TypeScript. Nombre de lignes: 66.

**Fonctions** : main
**Dépendances** : fs/promises, commander, @/versions/lib/all-versions

### `update-enterprise-dates.ts`

Module TypeScript. Nombre de lignes: 68.

**Fonctions** : main
**Dépendances** : url, path, fs/promises, @/workflows/git-utils

### `version-utils.ts`

Module TypeScript. Nombre de lignes: 58.

**Fonctions** : isGhesReleaseDeprecated, isInAllGhes, isFeatureDeprecated, isAllVersions, getFeatureVersionsObject
**Dépendances** : semver, @/versions/lib/enterprise-server-releases, @/data-directory/lib/data-directory, @/types
