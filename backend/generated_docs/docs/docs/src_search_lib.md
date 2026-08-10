# Module : src/search/lib

5 fichier(s), 5 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : aiSearchProxy, getAllVersionsKeyFromIndexVersion, getElasticSearchIndex, getPlanVersionFromIndexVersion, sanitizeSearchQuery
- **Dépendances** : @/frame/lib/fetch-utils, @/languages/lib/languages-server, @/observability/lib/statsd, @/observability/logger, @/search/lib/ai-search-constants, @/search/lib/elasticsearch-versions, @/search/lib/helpers/cse-copilot-docs-versions, @/search/lib/helpers/external-search-analytics, @/search/lib/helpers/get-cse-copilot-auth, @/search/lib/helpers/time, @/search/types, @/types

## Détail des fichiers

### `ai-search-constants.ts`

Module TypeScript. Nombre de lignes: 9.

### `ai-search-proxy.ts`

Module TypeScript. Nombre de lignes: 183.

**Fonctions** : aiSearchProxy
**Dépendances** : express, @/observability/logger, @/observability/lib/statsd, @/frame/lib/fetch-utils, @/search/lib/helpers/get-cse-copilot-auth, @/search/lib/helpers/cse-copilot-docs-versions, @/types, @/search/lib/helpers/external-search-analytics, @/search/lib/ai-search-constants

### `elasticsearch-indexes.ts`

Module TypeScript. Nombre de lignes: 76.

**Fonctions** : getElasticSearchIndex
**Dépendances** : @/languages/lib/languages-server, @/search/lib/helpers/time, @/search/lib/elasticsearch-versions, @/search/types

### `elasticsearch-versions.ts`

Module TypeScript. Nombre de lignes: 102.

**Fonctions** : getPlanVersionFromIndexVersion, getAllVersionsKeyFromIndexVersion
**Dépendances** : @/versions/lib/all-versions

### `sanitize-search-query.ts`

Module TypeScript. Nombre de lignes: 48.

**Fonctions** : sanitizeSearchQuery
