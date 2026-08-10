# Module : src/data-directory/tests

7 fichier(s), 2 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : preprocess, table
- **Dépendances** : @/data-directory/lib/data-directory, @/data-directory/lib/data-schemas/index, @/data-directory/lib/filename-to-key, @/data-directory/scripts/find-orphaned-tables, @/languages/lib/languages-server, @/tests/helpers/data-directory, @/tests/helpers/schemas, @/tests/lib/validate-json-schema, ajv, fs, js-yaml, path

## Détail des fichiers

### `data-schemas.ts`

Module TypeScript. Nombre de lignes: 61.

**Dépendances** : js-yaml, fs, path, walk-sync, vitest, ajv, @/tests/lib/validate-json-schema, @/tests/helpers/schemas, @/data-directory/lib/data-schemas/index

### `filename-to-key.ts`

Module TypeScript. Nombre de lignes: 13.

**Dépendances** : vitest, @/data-directory/lib/filename-to-key

### `find-orphaned-tables.ts`

Module TypeScript. Nombre de lignes: 57. Elements detectés: function table

**Fonctions** : table
**Dépendances** : vitest, @/data-directory/scripts/find-orphaned-tables

### `get-data.ts`

Module TypeScript. Nombre de lignes: 340.

**Dépendances** : fs, path, vitest, @/languages/lib/languages-server, @/tests/helpers/data-directory

### `index.ts`

Module TypeScript. Nombre de lignes: 37. Elements detectés: function preprocess

**Fonctions** : preprocess
**Dépendances** : url, path, vitest, @/data-directory/lib/data-directory

### `orphaned-features.ts`

Module TypeScript. Nombre de lignes: 150.

**Dépendances** : url, path, fs, vitest

### `ui-yml-structure.ts`

Module TypeScript. Nombre de lignes: 20.

**Dépendances** : fs, path, vitest
