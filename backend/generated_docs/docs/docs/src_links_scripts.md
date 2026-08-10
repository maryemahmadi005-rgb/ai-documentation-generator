# Module : src/links/scripts

8 fichier(s), 41 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : checkAnchorsFromHeadings, checkDomainUrls, checkFile, checkFileAnchors, checkGithubRepoUrl, checkPage, checkUrl, checkVersion, commentOnPR, countByTree, debugTimeEnd, debugTimeStart, endsWithAny, equalArray, equalObject
- **Dépendances** : @/frame/lib/fetch-utils, @/frame/lib/read-frontmatter, @/frame/lib/warm-server, @/languages/lib/languages-server, @/links/lib/excluded-links, @/links/lib/extract-links, @/links/lib/heading-anchors, @/links/lib/update-internal-links, @/links/scripts/upload-artifact, @/types, @/versions/lib/all-versions, @/workflows/action-context

## Détail des fichiers

### `action-injections.ts`

Module TypeScript. Nombre de lignes: 55.

**Fonctions** : getCoreInject, getUploadArtifactInject
**Dépendances** : fs, path, chalk, @/workflows/github

### `check-github-github-links.ts`

Module TypeScript. Nombre de lignes: 236.

**Fonctions** : main, endsWithAny, getIndicesOf, regexIndexOf
**Dépendances** : fs/promises, @/frame/lib/fetch-utils, commander, @/workflows/git-utils

### `check-links-external.ts`

Module TypeScript. Nombre de lignes: 586. Elements detectés: function isExcludedLink, function normalizeUrl, function isDocsGithubUrl

**Fonctions** : isExcludedLink, normalizeUrl, isDocsGithubUrl, sleep, checkUrl, fetchWithTimeout, isGithubRepoRootUrl, checkGithubRepoUrl, extractAllExternalLinks, main, checkDomainUrls, runWorker
**Dépendances** : commander, chalk, fs, glob, lowdb/node, @/links/lib/extract-links, @/links/scripts/upload-artifact, @/workflows/issue-report, @/workflows/github, @/links/lib/excluded-links, @actions/core

### `check-links-internal.ts`

Module TypeScript. Nombre de lignes: 551. Elements detectés: function isExcludedLink, function getFrontmatterLineOffset

**Fonctions** : isExcludedLink, getFrontmatterLineOffset, getLinksFromMarkdown, checkAnchorsFromHeadings, checkPage, checkVersion, worker, main
**Dépendances** : fs, os, commander, chalk, @/frame/lib/warm-server, @/versions/lib/all-versions, @/languages/lib/languages-server, @/links/scripts/upload-artifact, @/workflows/issue-report, @/workflows/github, @/links/lib/excluded-links, @/links/lib/heading-anchors

### `check-links-pr.ts`

Module TypeScript. Nombre de lignes: 491.

**Fonctions** : checkFile, checkFileAnchors, getChangedFiles, filterContentFiles, commentOnPR, main
**Dépendances** : commander, chalk, @/frame/lib/warm-server, @/links/scripts/upload-artifact, @/workflows/github, @/workflows/action-context, @/types, fs, path

### `debug-time-taken.ts`

Module TypeScript. Nombre de lignes: 30.

**Fonctions** : debugTimeStart, debugTimeEnd

### `update-internal-links.ts`

Module TypeScript. Nombre de lignes: 341.

**Fonctions** : main, printObjectDifference, equalObject, isObject, equalArray, countByTree
**Dépendances** : fs, path, commander, chalk, js-yaml, @/links/lib/update-internal-links, @/frame/lib/read-frontmatter, @/workflows/walk-files

### `upload-artifact.ts`

Module TypeScript. Nombre de lignes: 14.

**Fonctions** : uploadArtifact
**Dépendances** : fs
