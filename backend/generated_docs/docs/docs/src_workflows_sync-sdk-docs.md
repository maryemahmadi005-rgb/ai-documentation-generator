# Module : src/workflows/sync-sdk-docs

2 fichier(s), 19 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : addFrontmatter, convertReadmesToIndex, createMissingIndexFiles, filePathToUrlPath, fixBareCodeFences, fixBlanksAroundFences, fixCodeFenceLanguages, generateAltText, generateImageName, getAllMarkdownFiles, getChildren, normalizeOrderedLists, processFile, rewriteDocsGitHubLinks, rewriteInternalLinks
- **Dépendances** : @gr2m/gray-matter, node:child_process, node:fs, node:path, node:util

## Détail des fichiers

### `convert-mermaid.ts`

Module TypeScript. Nombre de lignes: 177. Elements detectés: function getAllMarkdownFiles, function generateImageName, function generateAltText

**Fonctions** : getAllMarkdownFiles, generateImageName, generateAltText, processFile
**Dépendances** : node:fs, node:path, node:util, node:child_process

### `normalize-sdk-docs.ts`

Module TypeScript. Nombre de lignes: 784. Elements detectés: function getAllMarkdownFiles, function convertReadmesToIndex, function walk

**Fonctions** : getAllMarkdownFiles, convertReadmesToIndex, walk, slugToTitle, getChildren, filePathToUrlPath, addFrontmatter, rewriteInternalLinks, rewriteRepoRelativeLinks, rewriteDocsGitHubLinks, createMissingIndexFiles, fixCodeFenceLanguages, normalizeOrderedLists, fixBareCodeFences, fixBlanksAroundFences
**Dépendances** : node:fs, node:path, node:util, @gr2m/gray-matter
