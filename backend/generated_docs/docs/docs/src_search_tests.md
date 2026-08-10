# Module : src/search/tests

14 fichier(s), 7 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : buildRequest, buildResponse, describe, getSearchEndpointWithParams, incrementedMetrics, mockUpstream
- **Dépendances** : @/frame/lib/fetch-utils, @/observability/lib/statsd, @/search/components/helpers/ai-search-links-json, @/search/components/helpers/fix-incomplete-markdown, @/search/lib/ai-search-constants, @/search/lib/ai-search-proxy, @/search/lib/sanitize-search-query, @/search/types, @/tests/helpers/conditional-runs, @/tests/helpers/e2etest, @/tests/mocks/start-mock-server, @/types

## Détail des fichiers

### `aggregate-search-index-failures.ts`

Module TypeScript. Nombre de lignes: 155.

**Dépendances** : vitest

### `ai-search-links-json.ts`

Module TypeScript. Nombre de lignes: 132.

**Dépendances** : vitest, @/search/components/helpers/ai-search-links-json

### `ai-search-local-proxy.ts`

Module TypeScript. Nombre de lignes: 88.

**Dépendances** : vitest, @/tests/helpers/e2etest

### `ai-search-proxy.ts`

Module TypeScript. Nombre de lignes: 125. Elements detectés: function buildResponse, function buildRequest, function mockUpstream

**Fonctions** : incrementedMetrics, buildResponse, buildRequest, mockUpstream
**Dépendances** : vitest, @/observability/lib/statsd, @/frame/lib/fetch-utils, @/search/lib/ai-search-proxy, @/search/lib/ai-search-constants, @/types

### `apache-arrow-stub.ts`

Module TypeScript. Nombre de lignes: 33.

**Dépendances** : vitest, child_process, @elastic/elasticsearch

### `api-ai-search-autocomplete.ts`

Module TypeScript. Nombre de lignes: 139.

**Fonctions** : getSearchEndpointWithParams
**Dépendances** : vitest, @/tests/helpers/conditional-runs, @/tests/helpers/e2etest, @/search/types

### `api-ai-search.ts`

Module TypeScript. Nombre de lignes: 173.

**Dépendances** : vitest, @/tests/helpers/e2etest, @/tests/mocks/start-mock-server, @/search/lib/ai-search-constants

### `api-combined-search.ts`

Module TypeScript. Nombre de lignes: 141.

**Fonctions** : getSearchEndpointWithParams
**Dépendances** : vitest, @/tests/helpers/conditional-runs, @/tests/helpers/e2etest, @/search/types

### `api-search.ts`

Module TypeScript. Nombre de lignes: 409.

**Dépendances** : vitest, @/tests/helpers/conditional-runs, @/tests/helpers/e2etest, @/search/types

### `build-records-from-api.ts`

Module TypeScript. Nombre de lignes: 526.

**Dépendances** : vitest, @/frame/lib/fetch-utils

### `fix-incomplete-markdown.ts`

Module TypeScript. Nombre de lignes: 127.

**Fonctions** : describe
**Dépendances** : vitest, @/search/components/helpers/fix-incomplete-markdown

### `rendering.ts`

Module TypeScript. Nombre de lignes: 134.

**Dépendances** : vitest, @/tests/helpers/conditional-runs, @/tests/helpers/e2etest

### `sanitize-search-query.ts`

Module TypeScript. Nombre de lignes: 182.

**Dépendances** : vitest, @/search/lib/sanitize-search-query

### `search.ts`

Module TypeScript. Nombre de lignes: 33.

**Dépendances** : vitest, @/tests/helpers/e2etest
