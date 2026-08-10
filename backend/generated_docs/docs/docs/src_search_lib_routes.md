# Module : src/search/lib/routes

3 fichier(s), 3 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : aiSearchAutocompleteRoute, combinedSearchRoute, generalSearchRoute
- **Dépendances** : ../get-elasticsearch-results/general-search, @/frame/middleware/cache-control, @/frame/middleware/set-fastly-surrogate-key, @/search/lib/get-elasticsearch-results/ai-search-autocomplete, @/search/lib/get-elasticsearch-results/general-search, @/search/lib/helpers/external-search-analytics, @/search/lib/search-request-params/get-search-from-request-params, @/search/middleware/search-routes, @/search/types, express

## Détail des fichiers

### `ai-search-autocomplete-route.ts`

Module TypeScript. Nombre de lignes: 42.

**Fonctions** : aiSearchAutocompleteRoute
**Dépendances** : express, @/frame/middleware/cache-control, @/search/lib/get-elasticsearch-results/ai-search-autocomplete, @/search/lib/search-request-params/get-search-from-request-params, @/search/middleware/search-routes

### `combined-search-route.ts`

Module TypeScript. Nombre de lignes: 117.

**Fonctions** : combinedSearchRoute
**Dépendances** : @/search/lib/search-request-params/get-search-from-request-params, @/search/lib/get-elasticsearch-results/ai-search-autocomplete, @/frame/middleware/cache-control, @/frame/middleware/set-fastly-surrogate-key, @/search/middleware/search-routes, @/search/lib/helpers/external-search-analytics, express, @/search/types, ../get-elasticsearch-results/general-search

### `general-search-route.ts`

Module TypeScript. Nombre de lignes: 41.

**Fonctions** : generalSearchRoute
**Dépendances** : express, @/frame/middleware/cache-control, @/frame/middleware/set-fastly-surrogate-key, @/search/lib/search-request-params/get-search-from-request-params, @/search/lib/get-elasticsearch-results/general-search, @/search/middleware/search-routes, @/search/lib/helpers/external-search-analytics
