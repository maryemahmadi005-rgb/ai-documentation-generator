# Module : src/data-directory/lib

3 fichier(s), 6 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : dataDirectory, filenameToKey, getDataByDir, getDeepDataByDir, getDirents, getSmartSplit
- **Dépendances** : ./filename-to-key, @/frame/components/context/MainContext, @/frame/lib/load-yaml, @/languages/lib/correct-translation-content, @/languages/lib/languages-server, @/observability/logger, @gr2m/gray-matter, assert, fs, lodash-es, path, walk-sync

## Détail des fichiers

### `data-directory.ts`

Module TypeScript. Nombre de lignes: 77.

**Fonctions** : dataDirectory
**Dépendances** : assert, fs, path, walk-sync, @/frame/lib/load-yaml, lodash-es, ./filename-to-key, @gr2m/gray-matter

### `filename-to-key.ts`

Module TypeScript. Nombre de lignes: 22.

**Fonctions** : filenameToKey
**Dépendances** : path, lodash-es

### `get-data.ts`

Module TypeScript. Nombre de lignes: 372. Elements detectés: function getDeepDataByDir, function getDirents

**Fonctions** : getDeepDataByDir, getDirents, getDataByDir, getSmartSplit
**Dépendances** : fs, path, @/frame/lib/load-yaml, @gr2m/gray-matter, lodash-es, @/languages/lib/languages-server, @/languages/lib/correct-translation-content, @/observability/logger, @/frame/components/context/MainContext
