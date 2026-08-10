# Module : src/graphql/tests

6 fichier(s), 6 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : categoriesFor, readIndex, snapshotReferenceDir, steadyPresence, writeCategoryFile, writeIndex
- **Dépendances** : ../lib/categories, ../lib/index, ../lib/validator, ../scripts/utils/process-schemas, @/automated-pipelines/lib/update-markdown, @/frame/lib/page-data, @/frame/lib/read-json-file, @/tests/helpers/e2etest, @/tests/helpers/schemas, @/tests/lib/validate-json-schema, @/types, @/versions/lib/all-versions

## Détail des fichiers

### `build-changelog.ts`

Module TypeScript. Nombre de lignes: 323.

**Dépendances** : fs/promises, vitest, js-yaml, mockdate, @/frame/lib/read-json-file

### `derive-categories.ts`

Module TypeScript. Nombre de lignes: 136.

**Fonctions** : categoriesFor
**Dépendances** : vitest, ../scripts/utils/process-schemas

### `get-schema-files.ts`

Module TypeScript. Nombre de lignes: 55.

**Dépendances** : fs, vitest, @/versions/lib/all-versions, ../lib/categories

### `server-rendering.ts`

Module TypeScript. Nombre de lignes: 65.

**Dépendances** : vitest, @/tests/helpers/e2etest, @/frame/lib/page-data, @/types

### `sync-category-content.ts`

Module TypeScript. Nombre de lignes: 148. Elements detectés: function steadyPresence

**Fonctions** : steadyPresence, writeCategoryFile, writeIndex, readIndex, snapshotReferenceDir
**Dépendances** : os, fs/promises, fs, path, vitest, @gr2m/gray-matter, @/automated-pipelines/lib/update-markdown

### `validate-schema.ts`

Module TypeScript. Nombre de lignes: 86.

**Dépendances** : vitest, @/tests/lib/validate-json-schema, @/frame/lib/read-json-file, ../lib/validator, @/tests/helpers/schemas, @/versions/lib/all-versions, ../lib/categories, ../lib/index
