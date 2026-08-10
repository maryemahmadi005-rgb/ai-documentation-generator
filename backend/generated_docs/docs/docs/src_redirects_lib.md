# Module : src/redirects/lib

6 fichier(s), 13 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : __resetGraphqlCategoryCacheForTests, applyGraphqlCategoryRedirect, buildPrefix, getExceptionRedirects, getRedirect, githubAERedirect, loadCategoryMap, parseLegacyUrl, permalinkRedirects, precompileRedirects, splitPathByLanguage, tryReplacements, versionUrlToDataDir
- **Dépendances** : ./exception-redirects, @/frame/lib/path-utils, @/frame/lib/read-json-file, @/languages/lib/languages-server, @/types, @/versions/lib/all-versions, @/versions/lib/enterprise-server-releases, @/versions/lib/non-enterprise-default-version, fs, path

## Détail des fichiers

### `exception-redirects.ts`

Module TypeScript. Nombre de lignes: 24.

**Fonctions** : getExceptionRedirects
**Dépendances** : fs

### `external-sites.json`

Fichier JSON. Nombre de lignes: 21.

### `get-redirect.ts`

Module TypeScript. Nombre de lignes: 303.

**Fonctions** : splitPathByLanguage, getRedirect, githubAERedirect, tryReplacements
**Dépendances** : @/languages/lib/languages-server, @/versions/lib/non-enterprise-default-version, @/versions/lib/all-versions, @/frame/lib/path-utils, @/types

### `graphql-category-redirect.ts`

Module TypeScript. Nombre de lignes: 136. Elements detectés: function loadCategoryMap, function versionUrlToDataDir, function parseLegacyUrl

**Fonctions** : loadCategoryMap, versionUrlToDataDir, parseLegacyUrl, buildPrefix, applyGraphqlCategoryRedirect, __resetGraphqlCategoryCacheForTests
**Dépendances** : fs, path, @/languages/lib/languages-server, @/versions/lib/enterprise-server-releases

### `permalinks.ts`

Module TypeScript. Nombre de lignes: 48.

**Fonctions** : permalinkRedirects
**Dépendances** : @/versions/lib/non-enterprise-default-version, @/frame/lib/path-utils, @/types

### `precompile.ts`

Module TypeScript. Nombre de lignes: 58.

**Fonctions** : precompileRedirects
**Dépendances** : @/frame/lib/read-json-file, ./exception-redirects, @/versions/lib/enterprise-server-releases, @/types
