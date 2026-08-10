# Module : src/tests/helpers

7 fichier(s), 3 classe(s), 8 fonction(s).

## Vue d'ensemble

- **Classes principales** : DataDirectory, exists, takes
- **Fonctions principales** : checkCachingHeaders, checkURL, getDOM, getDOMCached, getScriptData, head, post, stripLiquid
- **Dépendances** : @/frame/lib/fetch-utils, @/frame/lib/path-utils, @/frame/middleware/set-fastly-surrogate-key, @/redirects/lib/get-redirect, @/types, ajv, cheerio, fs, js-yaml, lodash-es, os, path

## Détail des fichiers

### `caching-headers.ts`

Module TypeScript. Nombre de lignes: 32.

**Fonctions** : checkCachingHeaders
**Dépendances** : vitest, @/frame/middleware/set-fastly-surrogate-key

### `check-url.ts`

Module TypeScript. Nombre de lignes: 46. Elements detectés: function stripLiquid

**Fonctions** : stripLiquid, checkURL
**Dépendances** : @/redirects/lib/get-redirect, @/frame/lib/path-utils, @/types

### `conditional-runs.ts`

Module TypeScript. Nombre de lignes: 16.

**Dépendances** : vitest

### `data-directory.ts`

Module TypeScript. Nombre de lignes: 93.

**Classes** : exists, takes, DataDirectory
**Dépendances** : fs, os, path, js-yaml

### `e2etest.ts`

Module TypeScript. Nombre de lignes: 185.

**Fonctions** : head, post, getDOMCached, getDOM
**Dépendances** : cheerio, @/frame/lib/fetch-utils, lodash-es

### `schemas.ts`

Module TypeScript. Nombre de lignes: 41.

**Dépendances** : ajv

### `script-data.ts`

Module TypeScript. Nombre de lignes: 19. Elements detectés: function getScriptData

**Fonctions** : getScriptData
**Dépendances** : cheerio
