# Module : src/products/lib

3 fichier(s), 5 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : createOcticonToNameMap, getLocalizedGroupNames, getPage, getProductGroups, mapEnglishToLocalizedNames
- **Dépendances** : @/frame/lib/constants, @/frame/lib/read-frontmatter, @/languages/lib/languages-server, @/languages/lib/render-with-fallback, @/products/lib/all-products, @/types, @/versions/lib/enterprise-server-releases, @/versions/lib/get-applicable-versions, @/versions/lib/remove-fpt-from-path, fs, fs/promises, path

## Détail des fichiers

### `all-products.ts`

Module TypeScript. Nombre de lignes: 75.

**Dépendances** : fs, path, @/frame/lib/read-frontmatter, @/versions/lib/get-applicable-versions, @/versions/lib/remove-fpt-from-path, @/frame/lib/constants

### `get-product-groups.ts`

Module TypeScript. Nombre de lignes: 153.

**Fonctions** : getPage, getLocalizedGroupNames, createOcticonToNameMap, mapEnglishToLocalizedNames, getProductGroups
**Dépendances** : path, fs/promises, @/types, @/products/lib/all-products, @/languages/lib/render-with-fallback, @/versions/lib/remove-fpt-from-path, @/frame/lib/read-frontmatter, @/languages/lib/languages-server

### `product-names.ts`

Module TypeScript. Nombre de lignes: 9.

**Dépendances** : @/types, @/versions/lib/enterprise-server-releases
