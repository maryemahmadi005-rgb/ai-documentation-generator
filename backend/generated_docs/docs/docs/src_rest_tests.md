# Module : src/rest/tests

13 fichier(s), 7 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : createChangelog, enoent, findOperation, formatErrors, getApplicableVersionFromFile, getCategorySubcategory, getFlatListOfOperations
- **Dépendances** : ../../versions/lib/get-applicable-versions, ../components/get-rest-code-samples, ../components/types, ../lib/config, ../lib/index, ../scripts/test-open-api-schema, ../scripts/utils/sync, ../scripts/utils/update-markdown, @/frame/components/context/MainContext, @/frame/lib/frontmatter, @/frame/lib/read-frontmatter, @/frame/middleware/set-fastly-surrogate-key

## Détail des fichiers

### `api.ts`

Module TypeScript. Nombre de lignes: 59.

**Dépendances** : fs, vitest, @/tests/helpers/e2etest, @/frame/middleware/set-fastly-surrogate-key

### `cli-examples.ts`

Module TypeScript. Nombre de lignes: 158.

**Dépendances** : vitest, ../components/get-rest-code-samples, @/rest/components/types, @/frame/components/context/MainContext

### `code-example-logic.ts`

Module TypeScript. Nombre de lignes: 133.

**Dépendances** : vitest

### `create-rest-examples.ts`

Module TypeScript. Nombre de lignes: 88.

**Dépendances** : vitest

### `get-rest-code-samples-2.ts`

Module TypeScript. Nombre de lignes: 527.

**Dépendances** : vitest, ../components/get-rest-code-samples, ../components/types, @/frame/components/context/MainContext, @octokit/auth-oauth-app

### `get-rest-code-samples.ts`

Module TypeScript. Nombre de lignes: 280.

**Dépendances** : vitest, ../components/get-rest-code-samples, ../components/types, @/frame/components/context/MainContext

### `get-schema-files.ts`

Module TypeScript. Nombre de lignes: 28.

**Dépendances** : vitest, ../scripts/utils/sync, @/versions/lib/all-versions

### `lib-index.ts`

Module TypeScript. Nombre de lignes: 240. Elements detectés: function enoent

**Fonctions** : enoent
**Dépendances** : vitest

### `openapi-schema.ts`

Module TypeScript. Nombre de lignes: 197. Elements detectés: function getApplicableVersionFromFile, function getCategorySubcategory

**Fonctions** : getFlatListOfOperations, getApplicableVersionFromFile, getCategorySubcategory, findOperation
**Dépendances** : fs, vitest, walk-sync, lodash-es, @/versions/lib/all-versions, ../lib/index, @/frame/lib/read-frontmatter, @/frame/lib/frontmatter, ../../versions/lib/get-applicable-versions, ../scripts/test-open-api-schema, ../lib/config, @/rest/components/types

### `remove-stale-data-files.ts`

Module TypeScript. Nombre de lignes: 69.

**Dépendances** : vitest, fs/promises, fs, path, os, ../scripts/utils/sync

### `rendering.ts`

Module TypeScript. Nombre de lignes: 167.

**Fonctions** : formatErrors
**Dépendances** : vitest, github-slugger, @/tests/helpers/e2etest, @/versions/lib/all-versions, ../scripts/test-open-api-schema, @/rest/lib/index

### `sync-changelogs.ts`

Module TypeScript. Nombre de lignes: 330.

**Fonctions** : createChangelog
**Dépendances** : vitest, fs/promises, path, os

### `update-markdown.ts`

Module TypeScript. Nombre de lignes: 50.

**Dépendances** : vitest, ../scripts/utils/update-markdown
