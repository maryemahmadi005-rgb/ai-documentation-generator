# Module : src/graphql/scripts/utils

7 fichier(s), 29 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : addPeriod, bucketSchemaByCategory, buildCategoryHref, buildCategoryLookup, buildSourceContent, captureCategoryRedirects, categoryUrlPath, getArguments, getDeprecationReason, getDeprecationStatus, getDescription, getDocsCategory, getFullLink, getId, getKind
- **Dépendances** : ./schema-helpers, @/content-render/index, @/graphql/lib/categories, @gr2m/gray-matter, change-case, fs/promises, github-slugger, graphql, graphql/language, js-yaml, lodash-es, mkdirp

## Détail des fichiers

### `bucket-by-category.ts`

Module TypeScript. Nombre de lignes: 140. Elements detectés: function buildCategoryLookup, function rewriteHref, function rewriteHrefsInPlace

**Fonctions** : buildCategoryLookup, rewriteHref, rewriteHrefsInPlace, bucketSchemaByCategory, writeCategoryFiles
**Dépendances** : fs/promises, path, mkdirp

### `data-filenames.json`

Fichier JSON. Nombre de lignes: 17.

### `process-previews.ts`

Module TypeScript. Nombre de lignes: 47.

**Fonctions** : processPreviews
**Dépendances** : change-case, github-slugger

### `process-schemas.ts`

Module TypeScript. Nombre de lignes: 976.

**Fonctions** : processSchemas
**Dépendances** : lodash-es, graphql, ./schema-helpers, @/graphql/lib/categories, fs/promises, path

### `process-upcoming-changes.ts`

Module TypeScript. Nombre de lignes: 23.

**Fonctions** : processUpcomingChanges
**Dépendances** : js-yaml, lodash-es, @/content-render/index

### `schema-helpers.ts`

Module TypeScript. Nombre de lignes: 238. Elements detectés: function addPeriod, function getDeprecationStatus

**Fonctions** : addPeriod, getArguments, buildCategoryHref, getDeprecationReason, getDeprecationStatus, getDescription, getFullLink, getDocsCategory, getId, getKind, getPreview, getType, getTypeKind, removeMarkers
**Dépendances** : @/content-render/index, fs/promises, graphql/language, path, @/graphql/lib/categories

### `sync-category-content.ts`

Module TypeScript. Nombre de lignes: 161. Elements detectés: function isPresentInAnyVersion, function normalizeRedirects

**Fonctions** : categoryUrlPath, isPresentInAnyVersion, captureCategoryRedirects, normalizeRedirects, buildSourceContent, reconcileIndexRedirects, syncCategoryContentFiles
**Dépendances** : fs/promises, path, walk-sync, @gr2m/gray-matter, lodash-es, @/graphql/lib/categories
