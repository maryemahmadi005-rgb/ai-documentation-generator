# Module : src/search/middleware

4 fichier(s), 4 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : contextualizeGeneralSearch, filterRequestHeaders, getProxySearch, handleGetSearchResultsError
- **Dépendances** : ../lib/ai-search-proxy, @/frame/lib/fetch-utils, @/frame/lib/path-utils, @/frame/middleware/cache-control, @/observability/lib/failbot, @/observability/lib/statsd, @/observability/logger, @/observability/middleware/catch-middleware-error, @/search/lib/get-elasticsearch-results/general-search, @/search/lib/routes/ai-search-autocomplete-route, @/search/lib/routes/combined-search-route, @/search/lib/routes/general-search-route
- **Endpoints API** : /, /ai-search-autocomplete, /ai-search-autocomplete/v1, /ai-search/v1, /combined-search, /combined-search/v1, /legacy, /v1

## Détail des fichiers

### `ai-search-local-proxy.ts`

Module TypeScript. Nombre de lignes: 96. Elements detectés: function filterRequestHeaders

**Fonctions** : filterRequestHeaders
**Dépendances** : express, @/frame/lib/fetch-utils, node:stream, @/observability/logger
**API** : /ai-search/v1

### `ai-search.ts`

Module TypeScript. Nombre de lignes: 17.

**Dépendances** : express, @/observability/middleware/catch-middleware-error, ../lib/ai-search-proxy, @/frame/middleware/cache-control
**API** : /v1, /

### `general-search-middleware.ts`

Module TypeScript. Nombre de lignes: 166.

**Fonctions** : contextualizeGeneralSearch, getProxySearch
**Dépendances** : @/frame/lib/fetch-utils, express, @/observability/logger, @elastic/elasticsearch, @/observability/lib/statsd, @/frame/lib/path-utils, @/search/lib/get-elasticsearch-results/general-search, @/search/lib/search-request-params/get-search-from-request-params, @/search/lib/search-request-params/types

### `search-routes.ts`

Module TypeScript. Nombre de lignes: 73.

**Fonctions** : handleGetSearchResultsError
**Dépendances** : express, @/observability/lib/failbot, @/observability/middleware/catch-middleware-error, @/search/lib/routes/general-search-route, @/search/lib/routes/ai-search-autocomplete-route, @/search/lib/routes/combined-search-route, @/observability/logger
**API** : /legacy, /v1, /ai-search-autocomplete/v1, /combined-search/v1, /, /ai-search-autocomplete, /combined-search
