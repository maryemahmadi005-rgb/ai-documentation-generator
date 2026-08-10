# Module : src/shielding/middleware

8 fichier(s), 9 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : getCurrentBuildID, handleInvalidNextPaths, handleInvalidPaths, handleInvalidQuerystringValues, handleInvalidQuerystrings, handleMalformedUrls, handleOldNextDataPaths, isJunkPath
- **Dépendances** : ./handle-invalid-headers, ./handle-invalid-nextjs-paths, ./handle-invalid-paths, ./handle-invalid-query-string-values, ./handle-invalid-query-strings, ./handle-malformed-urls, ./handle-old-next-data-paths, @/frame/middleware/cache-control, @/observability/lib/statsd, @/observability/logger, @/tools/lib/all-platforms, @/tools/lib/all-tools

## Détail des fichiers

### `handle-invalid-headers.ts`

Module TypeScript. Nombre de lignes: 25.

**Fonctions** : handleInvalidNextPaths
**Dépendances** : express, @/types

### `handle-invalid-nextjs-paths.ts`

Module TypeScript. Nombre de lignes: 28.

**Fonctions** : handleInvalidNextPaths
**Dépendances** : express, @/observability/lib/statsd, @/frame/middleware/cache-control, @/types

### `handle-invalid-paths.ts`

Module TypeScript. Nombre de lignes: 80. Elements detectés: function isJunkPath

**Fonctions** : isJunkPath, handleInvalidPaths
**Dépendances** : express, @/frame/middleware/cache-control, @/types

### `handle-invalid-query-string-values.ts`

Module TypeScript. Nombre de lignes: 78.

**Fonctions** : handleInvalidQuerystringValues
**Dépendances** : express, @/observability/logger, @/types, @/observability/lib/statsd, @/tools/lib/all-tools, @/tools/lib/all-platforms, @/frame/middleware/cache-control

### `handle-invalid-query-strings.ts`

Module TypeScript. Nombre de lignes: 145.

**Fonctions** : handleInvalidQuerystrings
**Dépendances** : express, @/observability/logger, @/observability/lib/statsd, @/frame/middleware/cache-control, @/types

### `handle-malformed-urls.ts`

Module TypeScript. Nombre de lignes: 27.

**Fonctions** : handleMalformedUrls
**Dépendances** : express, @/frame/middleware/cache-control, @/types

### `handle-old-next-data-paths.ts`

Module TypeScript. Nombre de lignes: 48. Elements detectés: function getCurrentBuildID

**Fonctions** : handleOldNextDataPaths, getCurrentBuildID
**Dépendances** : fs, express, @/types, @/frame/middleware/cache-control

### `index.ts`

Module TypeScript. Nombre de lignes: 17.

**Dépendances** : express, ./handle-malformed-urls, ./handle-invalid-query-strings, ./handle-invalid-paths, ./handle-old-next-data-paths, ./handle-invalid-query-string-values, ./handle-invalid-nextjs-paths, ./handle-invalid-headers
