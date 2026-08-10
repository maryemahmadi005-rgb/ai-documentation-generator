# Module : src/assets/scripts

4 fichier(s), 7 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : checkFile, checkSVGContent, getTotalDiskSize, isExceptionPath, main
- **Dépendances** : @/languages/lib/languages-server, @/observability/lib/to-error, @/observability/logger, @/workflows/walk-files, @actions/core, @actions/github, chalk, cheerio, commander, file-type, fs, fs/promises

## Détail des fichiers

### `deleted-assets-pr-comment.ts`

Module TypeScript. Nombre de lignes: 68.

**Fonctions** : main
**Dépendances** : @actions/github, @actions/core

### `find-orphaned-assets.ts`

Module TypeScript. Nombre de lignes: 221. Elements detectés: function isExceptionPath

**Fonctions** : isExceptionPath, main, getTotalDiskSize
**Dépendances** : fs, path, commander, walk-sync, @/workflows/walk-files, @/languages/lib/languages-server

### `list-image-sizes.ts`

Module TypeScript. Nombre de lignes: 39.

**Dépendances** : url, path, walk-sync, sharp, @/observability/logger, @/observability/lib/to-error

### `validate-asset-images.ts`

Module TypeScript. Nombre de lignes: 142.

**Fonctions** : main, checkFile, checkSVGContent
**Dépendances** : fs/promises, path, commander, chalk, cheerio, file-type, walk-sync, is-svg
