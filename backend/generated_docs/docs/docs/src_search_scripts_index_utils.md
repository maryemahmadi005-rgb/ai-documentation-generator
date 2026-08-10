# Module : src/search/scripts/index/utils

5 fichier(s), 12 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : addJitter, createIndex, errorTest, escapeHTML, getAISearchAutocompleteSettings, getGeneralSearchSettings, getSnowballLanguage, loadIndexRecords, mainFunction, populateIndex, printSuccess, updateAlias
- **Dépendances** : @/search/lib/helpers/strings, @/search/lib/helpers/time, @/search/scripts/index/types, @/search/scripts/index/utils/constants, @/search/scripts/index/utils/retry-on-error-test, @elastic/elasticsearch, chalk, fs/promises, path

## Détail des fichiers

### `constants.ts`

Module TypeScript. Nombre de lignes: 10.

### `indexing-elasticsearch-utils.ts`

Module TypeScript. Nombre de lignes: 163.

**Fonctions** : createIndex, populateIndex, updateAlias, printSuccess, loadIndexRecords, escapeHTML, getSnowballLanguage
**Dépendances** : chalk, @elastic/elasticsearch, fs/promises, path, @/search/lib/helpers/time, @/search/scripts/index/utils/retry-on-error-test, @/search/lib/helpers/strings, @/search/scripts/index/types

### `mappings.ts`

Module TypeScript. Nombre de lignes: 39.

**Dépendances** : @elastic/elasticsearch

### `retry-on-error-test.ts`

Module TypeScript. Nombre de lignes: 74. Elements detectés: function addJitter

**Fonctions** : mainFunction, errorTest, addJitter
**Dépendances** : @/search/lib/helpers/time

### `settings.ts`

Module TypeScript. Nombre de lignes: 74.

**Fonctions** : getGeneralSearchSettings, getAISearchAutocompleteSettings
**Dépendances** : @/search/scripts/index/utils/constants, @elastic/elasticsearch
