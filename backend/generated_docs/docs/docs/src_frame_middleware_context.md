# Module : src/frame/middleware/context

8 fichier(s), 19 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : breadcrumbs, contextualize, currentProductTree, excludeHidden, filterHidden, genericToc, getBreadcrumbs, getCurrentProductTreeTitles, getTocItems, glossaries, glossariesList, isHomepage, isNewLandingPage, isParentOrEqualArray, layoutContext
- **Dépendances** : @/content-render/index, @/data-directory/lib/get-data, @/frame/lib/find-page-in-site-tree, @/frame/lib/warm-server, @/languages/lib/correct-translation-content, @/languages/lib/languages-server, @/languages/lib/render-with-fallback, @/observability/logger/lib/logger-context, @/products/lib/all-products, @/products/lib/get-product-groups, @/products/lib/product-names, @/types

## Détail des fichiers

### `breadcrumbs.ts`

Module TypeScript. Nombre de lignes: 89. Elements detectés: function getBreadcrumbs, function traverseTreeTitles, function isParentOrEqualArray

**Fonctions** : breadcrumbs, getBreadcrumbs, traverseTreeTitles, isParentOrEqualArray
**Dépendances** : express, @/types

### `context.ts`

Module TypeScript. Nombre de lignes: 111.

**Fonctions** : contextualize
**Dépendances** : express, @/types, @/languages/lib/languages-server, @/versions/lib/enterprise-server-releases, @/versions/lib/all-versions, @/products/lib/all-products, @/products/lib/product-names, @/frame/lib/warm-server, @/versions/lib/non-enterprise-default-version, @/data-directory/lib/get-data, @/observability/logger/lib/logger-context

### `current-product-tree.ts`

Module TypeScript. Nombre de lignes: 154.

**Fonctions** : currentProductTree, getCurrentProductTreeTitles, excludeHidden, sidebarTree
**Dépendances** : path, express, @/types, @/content-render/index, @/frame/lib/find-page-in-site-tree, @/versions/lib/remove-fpt-from-path, @/languages/lib/render-with-fallback

### `generic-toc.ts`

Module TypeScript. Nombre de lignes: 157. Elements detectés: function isNewLandingPage

**Fonctions** : isNewLandingPage, genericToc, getTocItems, filterHidden
**Dépendances** : express, @/types, @/frame/lib/find-page-in-site-tree

### `glossaries.ts`

Module TypeScript. Nombre de lignes: 79.

**Fonctions** : glossaries, glossariesList
**Dépendances** : express, @/types, @/data-directory/lib/get-data, @/content-render/index, @/languages/lib/render-with-fallback, @/languages/lib/correct-translation-content

### `layout.ts`

Module TypeScript. Nombre de lignes: 19.

**Fonctions** : layoutContext
**Dépendances** : express, @/types

### `product-groups.ts`

Module TypeScript. Nombre de lignes: 45.

**Fonctions** : isHomepage, productGroups
**Dépendances** : express, @/types, @/products/lib/get-product-groups, @/frame/lib/warm-server, @/languages/lib/languages-server, @/versions/lib/all-versions

### `render-product-name.ts`

Module TypeScript. Nombre de lignes: 25.

**Fonctions** : renderProductName
**Dépendances** : express, @/types, @/content-render/index
