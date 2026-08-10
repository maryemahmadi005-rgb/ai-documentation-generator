# Module : src/article-api/tests

24 fichier(s), 6 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : createContext, createMockPage, getCached, makeURL
- **Dépendances** : ../lib/summarize-schema, @/article-api/lib/get-link-data, @/article-api/lib/load-template, @/article-api/lib/normalize-markdown, @/article-api/lib/resolve-path, @/article-api/lib/summarize-schema, @/article-api/transformers/secret-scanning-transformer, @/frame/middleware/set-fastly-surrogate-key, @/secret-scanning/lib/get-secret-scanning-data, @/tests/helpers/e2etest, @/types, @/versions/lib/all-versions

## Détail des fichiers

### `article-body.ts`

Module TypeScript. Nombre de lignes: 76.

**Dépendances** : vitest, @/tests/helpers/e2etest

### `audit-logs-transformer.ts`

Module TypeScript. Nombre de lignes: 96.

**Dépendances** : vitest, @/tests/helpers/e2etest

### `bespoke-landing-transformer.ts`

Module TypeScript. Nombre de lignes: 26.

**Dépendances** : vitest, @/tests/helpers/e2etest

### `category-landing-transformer.ts`

Module TypeScript. Nombre de lignes: 14.

**Dépendances** : vitest, @/tests/helpers/e2etest

### `codeql-cli-transformer.ts`

Module TypeScript. Nombre de lignes: 39.

**Dépendances** : vitest, @/tests/helpers/e2etest

### `discovery-landing-transformer.ts`

Module TypeScript. Nombre de lignes: 70.

**Dépendances** : vitest, @/tests/helpers/e2etest

### `get-link-data.ts`

Module TypeScript. Nombre de lignes: 113. Elements detectés: function createMockPage, function createContext

**Fonctions** : createMockPage, createContext
**Dépendances** : vitest, @/article-api/lib/get-link-data, @/types

### `github-apps-transformer.ts`

Module TypeScript. Nombre de lignes: 211.

**Dépendances** : vitest, @/tests/helpers/e2etest

### `graphql-transformer.ts`

Module TypeScript. Nombre de lignes: 275.

**Fonctions** : getCached
**Dépendances** : vitest, @/tests/helpers/e2etest

### `journey-landing-transformer.ts`

Module TypeScript. Nombre de lignes: 16.

**Dépendances** : vitest, @/tests/helpers/e2etest

### `load-template.ts`

Module TypeScript. Nombre de lignes: 17.

**Dépendances** : vitest, @/article-api/lib/load-template

### `normalize-markdown.ts`

Module TypeScript. Nombre de lignes: 37.

**Dépendances** : vitest, @/article-api/lib/normalize-markdown

### `pageinfo.ts`

Module TypeScript. Nombre de lignes: 268.

**Dépendances** : vitest, @/tests/helpers/e2etest, @/frame/middleware/set-fastly-surrogate-key, @/versions/lib/enterprise-server-releases

### `pagelist.ts`

Module TypeScript. Nombre de lignes: 118.

**Dépendances** : vitest, @/tests/helpers/e2etest, @/versions/lib/all-versions, @/versions/lib/non-enterprise-default-version

### `release-notes-transformer.ts`

Module TypeScript. Nombre de lignes: 164.

**Dépendances** : vitest, @/types

### `resolve-path.ts`

Module TypeScript. Nombre de lignes: 110. Elements detectés: function createMockPage, function createContext

**Fonctions** : createMockPage, createContext
**Dépendances** : vitest, @/article-api/lib/resolve-path, @/types

### `rest-transformer.ts`

Module TypeScript. Nombre de lignes: 238.

**Dépendances** : vitest, @/tests/helpers/e2etest

### `secret-scanning-transformer.test.ts`

Module TypeScript. Nombre de lignes: 63.

**Dépendances** : vitest, @/article-api/transformers/secret-scanning-transformer, @/versions/middleware/short-versions, @/versions/lib/all-versions, @/versions/lib/enterprise-server-releases, @/secret-scanning/lib/get-secret-scanning-data, @/types

### `secret-scanning-transformer.ts`

Module TypeScript. Nombre de lignes: 48.

**Dépendances** : vitest, @/tests/helpers/e2etest

### `strip-html-comments.ts`

Module TypeScript. Nombre de lignes: 75.

**Dépendances** : vitest

### `summarize-schema.test.ts`

Module TypeScript. Nombre de lignes: 269.

**Dépendances** : vitest, ../lib/summarize-schema

### `summarize-schema.ts`

Module TypeScript. Nombre de lignes: 160.

**Dépendances** : vitest, @/article-api/lib/summarize-schema

### `toc-transformer.ts`

Module TypeScript. Nombre de lignes: 42.

**Dépendances** : vitest, @/tests/helpers/e2etest

### `webhooks-transformer.ts`

Module TypeScript. Nombre de lignes: 139. Elements detectés: function makeURL

**Fonctions** : makeURL
**Dépendances** : vitest, @/tests/helpers/e2etest
