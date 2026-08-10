# Module : src/content-render/scripts

8 fichier(s), 57 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : addToChildren, applyDataUpdates, buildCTAUrl, buildProgrammaticCTA, calculateTarget, changeHomepageLinks, confirmChoice, convertFilePathToDataPath, convertOldCTAUrl, convertUrls, detectContentEdits, determineContentType, determineProcessStatus, editFiles, existsAndIsDirectory
- **Dépendances** : ./reusables-cli/find/potential-uses, ./reusables-cli/find/unused, ./reusables-cli/find/used, @/content-render/index, @/data-directory/lib/data-schemas/ctas, @/frame/lib/frontmatter, @/frame/lib/read-frontmatter, @/frame/lib/read-frontmatter.js, @/types, @/versions/lib/all-versions, @/versions/lib/non-enterprise-default-version, @/workflows/walk-files

## Détail des fichiers

### `add-content-type.ts`

Module TypeScript. Nombre de lignes: 163. Elements detectés: function processFile

**Fonctions** : main, processFile, determineContentType
**Dépendances** : fs, path, commander, @/frame/lib/read-frontmatter, @/workflows/walk-files, @/frame/lib/frontmatter, @/types

### `cta-builder.ts`

Module TypeScript. Nombre de lignes: 560.

**Fonctions** : selectFromOptions, confirmChoice, extractCTAParams, formatValidationErrors, validateCTAParams, buildCTAUrl, convertOldCTAUrl, inferProductFromUrl, inferStyleFromContext, interactiveBuilder, prompt, convertUrls, validateUrl, buildProgrammaticCTA
**Dépendances** : commander, readline, chalk, ajv, @/data-directory/lib/data-schemas/ctas

### `liquid-tags.ts`

Module TypeScript. Nombre de lignes: 775. Elements detectés: function getErrorMessage, function getDataFilePath, function convertFilePathToDataPath

**Fonctions** : getErrorMessage, getDataFilePath, convertFilePathToDataPath, getAllowedTypes, expandReferences, restoreReferences, expandFileContent, detectContentEdits, loadDataValue, restoreFileContent, updateDataFiles, extractDataUpdates, applyDataUpdates, findLiquidReferences, resolveLiquidReference
**Dépendances** : commander, fs, path, js-yaml, chalk

### `move-by-content-type.ts`

Module TypeScript. Nombre de lignes: 544. Elements detectés: function shouldSkipIndexFile, function calculateTarget

**Fonctions** : shouldSkipIndexFile, calculateTarget
**Dépendances** : commander, fs/promises, path, chalk, child_process, @/workflows/walk-files.js, @/frame/lib/read-frontmatter.js, @/frame/lib/frontmatter

### `move-content.ts`

Module TypeScript. Nombre de lignes: 569.

**Fonctions** : main, validateFileInputs, existsAndIsDirectory, splitDirectory, findFilesInFolder, makeHref, moveFolder, undoFolder, getBasename, removeFromChildren, addToChildren, moveFiles, editFiles, undoFiles, changeHomepageLinks
**Dépendances** : fs, path, child_process, commander, chalk, walk-sync, escape-string-regexp, @/frame/lib/frontmatter, @/frame/lib/read-frontmatter

### `reusables-cli.ts`

Module TypeScript. Nombre de lignes: 65.

**Dépendances** : commander, ./reusables-cli/find/used, ./reusables-cli/find/potential-uses, ./reusables-cli/find/unused

### `test-moved-content.ts`

Module TypeScript. Nombre de lignes: 56. Elements detectés: function makeHref

**Fonctions** : main, makeHref
**Dépendances** : node:assert/strict, fs, path, commander, @/frame/lib/read-frontmatter

### `update-filepaths.ts`

Module TypeScript. Nombre de lignes: 230.

**Fonctions** : main, processFile, moveFile, sortFiles, filterFiles, determineProcessStatus
**Dépendances** : fs, path, commander, github-slugger, html-entities, child_process, @/workflows/walk-files, @/frame/lib/read-frontmatter, @/content-render/index, @/versions/lib/non-enterprise-default-version, @/versions/lib/all-versions, @/types
