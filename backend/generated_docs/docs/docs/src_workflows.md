# Module : src/workflows

30 fichier(s), 108 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : addItemToProject, addItemsToProject, boolEnvVar, buildUrl, calculateDueDate, checkContentType, clamp, commentOnDeployBatch, contentFilesToPageKeys, countRules, createIssueComment, createReportIssue, discoverWriterTools, ensureProductionComment, extractMetadata
- **Dépendances** : ../../.github/actions/labeler/labeler, ./action-context, ./git-utils, ./github, ./lib/in-liquid, ./secondary-ratelimit-retry, @/content-render/index, @/data-directory/lib/get-data, @/frame/lib/constants, @/frame/lib/fetch-utils, @/frame/lib/load-yaml, @/frame/lib/page-data

## Détail des fichiers

### `README.md`

### `action-context.ts`

Module TypeScript. Nombre de lignes: 26.

**Fonctions** : getActionContext
**Dépendances** : fs

### `benchmark-pages.ts`

Module TypeScript. Nombre de lignes: 225. Elements detectés: function normalizeErrorBody, function buildUrl, function sample<T>

**Fonctions** : normalizeErrorBody, timed, getPageList, buildUrl, worker, percentile, main
**Dépendances** : node:util

### `check-content-type.ts`

Module TypeScript. Nombre de lignes: 16.

**Fonctions** : main
**Dépendances** : @actions/core, @/workflows/fm-utils

### `content-changes-table-comment-cli.ts`

Module TypeScript. Nombre de lignes: 30.

**Dépendances** : commander, @/workflows/content-changes-table-comment

### `content-changes-table-comment.ts`

Module TypeScript. Nombre de lignes: 244.

**Fonctions** : main, makeBlobUrl, makeRow, getAllContentFiles
**Dépendances** : node:fs, node:path, @actions/github, @actions/core, walk-sync, ./git-utils, @/workflows/github, @/versions/lib/get-applicable-versions, @/versions/lib/non-enterprise-default-version, @/versions/lib/all-versions, @/frame/lib/read-frontmatter, ./lib/in-liquid

### `delete-orphan-translation-files.ts`

Module TypeScript. Nombre de lignes: 112. Elements detectés: function main, function getContentAndDataFiles

**Fonctions** : main, getContentAndDataFiles, formatFileSize
**Dépendances** : fs, path, commander, @/workflows/walk-files, @/frame/lib/constants

### `enable-automerge.ts`

Module TypeScript. Nombre de lignes: 46.

**Fonctions** : main
**Dépendances** : @actions/github

### `find-past-built-pr.ts`

Module TypeScript. Nombre de lignes: 142.

**Fonctions** : extractPrNumber, findBatchPrNumbers, ensureProductionComment, commentOnDeployBatch, main, getBuiltSHA
**Dépendances** : @octokit/rest, ./github, ./action-context, ./secondary-ratelimit-retry

### `fm-utils.ts`

Module TypeScript. Nombre de lignes: 16.

**Fonctions** : checkContentType
**Dépendances** : fs, @gr2m/gray-matter

### `fr-add-docs-reviewers-requests.ts`

Module TypeScript. Nombre de lignes: 247.

**Fonctions** : getAllOpenPRs, run
**Dépendances** : @octokit/graphql

### `generate-llms-txt.ts`

Module TypeScript. Nombre de lignes: 206. Elements detectés: function normalize

**Fonctions** : loadConfig, fetchRollup, renderLiquid, pageExists, normalize, getPageTitle, getPageIntro, formatPageLine, titleCase, generate, parseArgs, main
**Dépendances** : fs, @/frame/lib/load-yaml, @/frame/lib/page-data, @/content-render/index, @/data-directory/lib/get-data, @/versions/lib/all-versions, @/types

### `get-env-inputs.ts`

Module TypeScript. Nombre de lignes: 36.

**Fonctions** : getEnvInputs, boolEnvVar

### `git-utils.ts`

Module TypeScript. Nombre de lignes: 249.

**Fonctions** : getCommitSha, hasMatchingRef, getTreeSha, getTree, getContentsForBlob, getContents, getContentAndData, getContent, listPulls, createIssueComment, getPathsWithMatchingStrings, searchCode, getDirectoryContents
**Dépendances** : crypto, fs/promises, @/workflows/github, @/workflows/secondary-ratelimit-retry

### `github.ts`

Module TypeScript. Nombre de lignes: 40.

**Fonctions** : github, retryingGithub, isRequestError
**Dépendances** : dotenv, @octokit/rest, @octokit/plugin-retry

### `issue-report.ts`

Module TypeScript. Nombre de lignes: 135.

**Fonctions** : createReportIssue, linkReports
**Dépendances** : @octokit/rest, @actions/core

### `labeler.ts`

Module TypeScript. Nombre de lignes: 52.

**Dépendances** : commander, ../../.github/actions/labeler/labeler, @/links/scripts/action-injections, @/workflows/github

### `local-repo-sync.sh`

### `measure-instruction-budget.ts`

Module TypeScript. Nombre de lignes: 208. Elements detectés: function main

**Fonctions** : main, countRules, matchesPath, globToRegExp, printReport
**Dépendances** : fs, path, commander, gpt-tokenizer/encoding/o200k_base, @/frame/lib/read-frontmatter

### `prevent-pushes-to-main.ts`

Module TypeScript. Nombre de lignes: 19.

**Dépendances** : child_process

### `projects.ts`

Module TypeScript. Nombre de lignes: 433.

**Fonctions** : findFieldID, findSingleSelectID, addItemsToProject, addItemToProject, isDocsTeamMember, isGitHubOrgMember, formatDateForProject, calculateDueDate, generateUpdateProjectV2ItemFieldMutation, generateMutationToUpdateField, getFeature, getSize
**Dépendances** : @octokit/graphql

### `purge-fastly-changed-content.ts`

Module TypeScript. Nombre de lignes: 300. Elements detectés: function sleep, function serverRetryHintMs

**Fonctions** : sleep, rateLimitDelayMs, clamp, serverRetryHintMs, resolvePreviousProductionSha, getChangedContentFiles, contentFilesToPageKeys, hardPurgeKeyBatch, hardPurgeSurrogateKeys, main
**Dépendances** : @octokit/rest, @/frame/lib/fetch-utils, @/frame/middleware/set-fastly-surrogate-key, ./github, ./action-context

### `purge-fastly.ts`

Module TypeScript. Nombre de lignes: 205. Elements detectés: function languageSurrogateKeys, function languagesFromString

**Fonctions** : main, languageSurrogateKeys, languagesFromString, purgeKeys, runPurge, fastlyPurge
**Dépendances** : commander, @/frame/lib/fetch-utils, @/languages/lib/languages-server, @/frame/middleware/set-fastly-surrogate-key

### `ready-for-docs-review.ts`

Module TypeScript. Nombre de lignes: 264. Elements detectés: function getCopilotAuthorInfo, function getAuthorFieldValue

**Fonctions** : getCopilotAuthorInfo, getAuthorFieldValue, run
**Dépendances** : @octokit/graphql

### `secondary-ratelimit-retry.ts`

Module TypeScript. Nombre de lignes: 40.

**Fonctions** : sleep
**Dépendances** : @/workflows/github

### `unallowed-contribution-filters.yml`

### `unallowed-contributions.ts`

Module TypeScript. Nombre de lignes: 55.

**Fonctions** : main
**Dépendances** : @actions/core, fs, js-yaml, lodash-es, @/workflows/fm-utils, @/workflows/github

### `wait-for-build.ts`

Module TypeScript. Nombre de lignes: 70.

**Fonctions** : waitForBuild
**Dépendances** : node:child_process, node:path, node:url, @/frame/lib/fetch-utils

### `walk-files.ts`

Module TypeScript. Nombre de lignes: 40.

**Fonctions** : walkFiles, readFiles, filterFiles, withFiles, writeFiles
**Dépendances** : walk-sync, fs

### `writers-help-metadata.ts`

Module TypeScript. Nombre de lignes: 182. Elements detectés: function extractMetadata

**Fonctions** : discoverWriterTools, extractMetadata, getCategory, findScriptName, prioritizeOrder, main
**Dépendances** : fs, glob, path, url
