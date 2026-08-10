# Module : src/data-directory/scripts/find-orphaned-features

3 fichier(s), 10 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : checkString, deleteOrphans, escapeRegex, find, findByRegex, formatDelta, getReusableFiles, getVariableFiles, isFloat, searchAndRemove
- **Dépendances** : ./delete, ./find, @/content-linter/lib/helpers/liquid-utils, @/data-directory/lib/get-data, @/frame/lib/warm-server, @/languages/lib/correct-translation-content, @/languages/lib/languages-server, @/types, chalk, commander, fs, liquidjs

## Détail des fichiers

### `delete.ts`

Module TypeScript. Nombre de lignes: 39.

**Fonctions** : deleteOrphans
**Dépendances** : fs, path, chalk, @/languages/lib/languages-server

### `find.ts`

Module TypeScript. Nombre de lignes: 293.

**Fonctions** : find, formatDelta, searchAndRemove, getReusableFiles, getVariableFiles, checkString, findByRegex, escapeRegex, isFloat
**Dépendances** : node:assert, fs, path, chalk, liquidjs, @/types, @/frame/lib/warm-server, @/data-directory/lib/get-data, @/content-linter/lib/helpers/liquid-utils, @/languages/lib/languages-server, @/languages/lib/correct-translation-content

### `index.ts`

Module TypeScript. Nombre de lignes: 23.

**Dépendances** : commander, ./find, ./delete
