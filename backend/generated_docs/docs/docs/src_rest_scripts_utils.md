# Module : src/rest/scripts/utils

13 fichier(s), 2 classe(s), 32 fonction(s).

## Vue d'ensemble

- **Classes principales** : Operation, serverUrl
- **Fonctions principales** : buildVersionMappings, createOperations, formatRestData, getBodyParams, getChangelogPath, getClientSideRedirects, getCodeSamples, getDataFrontmatter, getGHESVersionFromFilepath, getMarkdownContent, getOneOfChildParams, getOpenApiSchemaFiles, getParameterExamples, getRequestExamples, getResponseExamples
- **Dépendances** : ../../lib/index, ./create-rest-examples, ./get-body-params, ./get-operations, ./normalize-docs-urls, ./openapi-types, ./operation, ./operation-schema, ./render-content, ./update-markdown, @/content-render/index, @/github-apps/scripts/sync

## Détail des fichiers

### `create-rest-examples.ts`

Module TypeScript. Nombre de lignes: 421.

**Fonctions** : getCodeSamples, mergeExamples, getRequestExamples, stripSchemaExamples, getResponseExamples, getParameterExamples
**Dépendances** : ./openapi-types

### `get-body-params.ts`

Module TypeScript. Nombre de lignes: 321.

**Fonctions** : getTopLevelOneOfProperty, handleObjectOnlyOneOf, getBodyParams, getTransformedParam, getOneOfChildParams
**Dépendances** : ./render-content

### `get-openapi-schemas.ts`

Module TypeScript. Nombre de lignes: 77.

**Fonctions** : getSchemas, validateVersionsOptions
**Dépendances** : fs/promises, js-yaml, path, @/versions/lib/all-versions

### `get-operations.ts`

Module TypeScript. Nombre de lignes: 33.

**Fonctions** : processOperations, createOperations
**Dépendances** : @/rest/scripts/utils/operation, ./openapi-types

### `get-redirects.ts`

Module TypeScript. Nombre de lignes: 44.

**Fonctions** : syncRestRedirects, getClientSideRedirects
**Dépendances** : fs/promises

### `normalize-docs-urls.ts`

Module TypeScript. Nombre de lignes: 8.

**Fonctions** : normalizeDocsUrls

### `openapi-types.ts`

Module TypeScript. Nombre de lignes: 74.

**Classes** : serverUrl

### `operation-schema.ts`

Module TypeScript. Nombre de lignes: 62.

### `operation.ts`

Module TypeScript. Nombre de lignes: 217.

**Classes** : Operation
**Dépendances** : http-status-code, lodash-es, url-template, json-schema-merge-allof, ./render-content, ./create-rest-examples, ./operation-schema, @/tests/lib/validate-json-schema, ./get-body-params, ./openapi-types

### `render-content.ts`

Module TypeScript. Nombre de lignes: 12.

**Fonctions** : renderContent
**Dépendances** : @/content-render/index, @/languages/lib/get-alert-titles, ./normalize-docs-urls

### `sync-changelogs.ts`

Module TypeScript. Nombre de lignes: 184. Elements detectés: function buildVersionMappings

**Fonctions** : buildVersionMappings, getChangelogPath, parseVersionSections, syncChangelogs
**Dépendances** : fs/promises, fs, path, @/versions/lib/all-versions

### `sync.ts`

Module TypeScript. Nombre de lignes: 211.

**Fonctions** : syncRestData, removeStaleRestDataFiles, formatRestData, updateRestConfigData, getOpenApiSchemaFiles
**Dépendances** : fs/promises, fs, path, mkdirp, ./update-markdown, @/versions/lib/all-versions, ./get-operations, @/github-apps/scripts/sync, ../../lib/index, ./openapi-types, ./operation

### `update-markdown.ts`

Module TypeScript. Nombre de lignes: 150.

**Fonctions** : updateRestFiles, getGHESVersionFromFilepath, getDataFrontmatter, getMarkdownContent
**Dépendances** : path, walk-sync, fs/promises, @/versions/lib/all-versions, ../../lib/index, @/versions/lib/enterprise-server-releases
