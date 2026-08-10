# Module : src/search/lib/helpers

6 fichier(s), 16 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : formatSecondsToHHMMSS, formatTime, generateHmacSha256, getCSECopilotSource, getElasticsearchClient, getElasticsearchURL, getEpochTime, getHmacWithEpoch, handleExternalSearchAnalytics, isExternalAPIRequest, readableTimeMinAndSec, safeUrlDisplay, sanitizeUserAgent, sleep, stripPort
- **Dépendances** : ../elasticsearch-versions, @/events/lib/hydro, @/events/lib/schema, @/observability/logger, @/search/lib/helpers/strings, @/types, @elastic/elasticsearch, crypto

## Détail des fichiers

### `cse-copilot-docs-versions.ts`

Module TypeScript. Nombre de lignes: 20.

**Fonctions** : getCSECopilotSource
**Dépendances** : ../elasticsearch-versions

### `external-search-analytics.ts`

Module TypeScript. Nombre de lignes: 145. Elements detectés: function sanitizeUserAgent

**Fonctions** : handleExternalSearchAnalytics, sanitizeUserAgent, stripPort, isExternalAPIRequest
**Dépendances** : @/types, @/events/lib/hydro, @/events/lib/schema, @/observability/logger

### `get-client.ts`

Module TypeScript. Nombre de lignes: 36. Elements detectés: function getElasticsearchURL

**Fonctions** : getElasticsearchClient, getElasticsearchURL
**Dépendances** : @elastic/elasticsearch, @/search/lib/helpers/strings, @/observability/logger

### `get-cse-copilot-auth.ts`

Module TypeScript. Nombre de lignes: 21. Elements detectés: function getEpochTime, function generateHmacSha256

**Fonctions** : getHmacWithEpoch, getEpochTime, generateHmacSha256
**Dépendances** : crypto

### `strings.ts`

Module TypeScript. Nombre de lignes: 10.

**Fonctions** : safeUrlDisplay

### `time.ts`

Module TypeScript. Nombre de lignes: 55.

**Fonctions** : sleep, formatTime, utcTimestamp, formatSecondsToHHMMSS, readableTimeMinAndSec
