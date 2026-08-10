# Module : src/archives/middleware

3 fichier(s), 9 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : archivedAssetRedirects, archivedEnterpriseVersions, archivedEnterpriseVersionsAssets, cacheAggressively, doGet, getEarlyNotFoundReason, getFallbackRedirect, getProxyPath, splitByLanguage
- **Dépendances** : @/archives/lib/is-archived-version, @/frame/lib/fetch-utils, @/frame/lib/patterns, @/frame/lib/read-json-file, @/frame/middleware/cache-control, @/frame/middleware/set-fastly-surrogate-key, @/languages/lib/languages, @/languages/lib/languages-server, @/observability/lib/statsd, @/observability/logger, @/types, @/versions/lib/version-satisfies-range

## Détail des fichiers

### `archived-asset-redirects.ts`

Module TypeScript. Nombre de lignes: 31.

**Fonctions** : archivedAssetRedirects
**Dépendances** : express, @/types

### `archived-enterprise-versions-assets.ts`

Module TypeScript. Nombre de lignes: 142.

**Fonctions** : archivedEnterpriseVersionsAssets
**Dépendances** : @/frame/lib/fetch-utils, express, @/frame/lib/patterns, @/archives/lib/is-archived-version, @/frame/middleware/set-fastly-surrogate-key, @/frame/middleware/cache-control, @/types, @/observability/logger

### `archived-enterprise-versions.ts`

Module TypeScript. Nombre de lignes: 518.

**Fonctions** : cacheAggressively, archivedEnterpriseVersions, doGet, getProxyPath, getFallbackRedirect, splitByLanguage, getEarlyNotFoundReason
**Dépendances** : express, @/frame/lib/fetch-utils, @/observability/lib/statsd, @/observability/logger, @/frame/lib/patterns, @/versions/lib/version-satisfies-range, @/archives/lib/is-archived-version, @/frame/middleware/set-fastly-surrogate-key, @/frame/lib/read-json-file, @/frame/middleware/cache-control, @/languages/lib/languages-server, @/languages/lib/languages
