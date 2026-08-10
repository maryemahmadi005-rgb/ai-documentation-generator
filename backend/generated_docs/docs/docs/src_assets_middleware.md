# Module : src/assets/middleware

3 fichier(s), 6 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : assetPreprocessing, deconstructImageURL, dynamicAssets, isChecksummed, makeURL, setStaticAssetCaching
- **Dépendances** : @/frame/middleware/cache-control, @/frame/middleware/set-fastly-surrogate-key, @/observability/logger, @/types, express, fs/promises, sharp

## Détail des fichiers

### `asset-preprocessing.ts`

Module TypeScript. Nombre de lignes: 42.

**Fonctions** : assetPreprocessing
**Dépendances** : express, @/types

### `dynamic-assets.ts`

Module TypeScript. Nombre de lignes: 183.

**Fonctions** : makeURL, dynamicAssets, deconstructImageURL
**Dépendances** : fs/promises, express, sharp, @/types, @/frame/middleware/cache-control, @/observability/logger

### `static-asset-caching.ts`

Module TypeScript. Nombre de lignes: 25. Elements detectés: function isChecksummed

**Fonctions** : setStaticAssetCaching, isChecksummed
**Dépendances** : express, @/types, @/frame/middleware/set-fastly-surrogate-key
