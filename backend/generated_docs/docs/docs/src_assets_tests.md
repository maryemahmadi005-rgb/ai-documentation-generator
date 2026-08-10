# Module : src/assets/tests

2 fichier(s), 4 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : getNextStaticAsset, mockRequest, mockResponse, next
- **Dépendances** : @/archives/middleware/archived-enterprise-versions-assets, @/frame/middleware/set-fastly-surrogate-key, @/tests/helpers/caching-headers, @/tests/helpers/e2etest, @/types, express, file-type, fs, nock, path, sharp, vitest

## Détail des fichiers

### `dynamic-assets.ts`

Module TypeScript. Nombre de lignes: 97.

**Dépendances** : vitest, sharp, file-type, @/frame/middleware/set-fastly-surrogate-key, @/tests/helpers/e2etest

### `static-assets.ts`

Module TypeScript. Nombre de lignes: 361. Elements detectés: function getNextStaticAsset, function mockRequest

**Fonctions** : getNextStaticAsset, mockRequest, mockResponse, next
**Dépendances** : fs, path, vitest, nock, express, @/tests/helpers/e2etest, @/tests/helpers/caching-headers, @/frame/middleware/set-fastly-surrogate-key, @/archives/middleware/archived-enterprise-versions-assets, @/types
