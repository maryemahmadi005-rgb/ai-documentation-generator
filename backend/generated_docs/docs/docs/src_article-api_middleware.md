# Module : src/article-api/middleware

5 fichier(s), 21 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : apiVersionValidationMiddleware, computeBreadcrumbsFromReq, computeCacheableFromReq, createContextualizedRenderingRequest, getArticleBody, getBreadcrumbsForPage, getCacheablePageInfo, getMetadata, getPageInfo, getPageInfoFromCache, getProductPageInfo, incrementArticleLookup, incrementPagelistLookup, makeRenderingReq, next
- **Dépendances** : ../types, ./article-body, ./article-pageinfo, ./validation, @/archives/lib/is-archived-version, @/article-api/lib/normalize-markdown, @/article-api/transformers, @/article-api/types, @/data-directory/middleware/data-tables, @/frame/lib/path-utils, @/frame/lib/read-json-file, @/frame/middleware/cache-control
- **Endpoints API** : /, /:lang/:productVersion, /:someParam, /body, /languages, /meta, /versions

## Détail des fichiers

### `article-body.ts`

Module TypeScript. Nombre de lignes: 64.

**Fonctions** : createContextualizedRenderingRequest, getArticleBody
**Dépendances** : express, @/types, @/article-api/types, @/frame/middleware/context/context, @/versions/middleware/features, @/frame/middleware/context/glossaries, @/data-directory/middleware/data-tables, @/article-api/transformers, @/article-api/lib/normalize-markdown, @/versions/lib/all-versions

### `article-pageinfo.ts`

Module TypeScript. Nombre de lignes: 200.

**Fonctions** : makeRenderingReq, next, computeCacheableFromReq, computeBreadcrumbsFromReq, getCacheablePageInfo, getBreadcrumbsForPage, getPageInfo, getProductPageInfo, getPageInfoFromCache, getMetadata
**Dépendances** : express, ../types, @/types, @/versions/middleware/short-versions, @/frame/middleware/context/context, @/versions/middleware/features, @/frame/middleware/context/breadcrumbs, @/frame/middleware/context/current-product-tree, @/frame/lib/read-json-file

### `article.ts`

Module TypeScript. Nombre de lignes: 197.

**Fonctions** : pageInfo, incrementArticleLookup, recordBodySize
**Dépendances** : express, @/frame/middleware/cache-control, @/observability/middleware/catch-middleware-error, ../types, ./article-body, ./article-pageinfo, @/observability/lib/statsd
**API** : /, /body, /meta

### `pagelist.ts`

Module TypeScript. Nombre de lignes: 174.

**Fonctions** : versionMatcher, incrementPagelistLookup
**Dépendances** : express, @/types, @/frame/middleware/cache-control, @/frame/lib/path-utils, @/languages/middleware/detect-language, ./validation, @/observability/middleware/catch-middleware-error, @/observability/lib/statsd, @/versions/lib/all-versions, @/versions/lib/enterprise-server-releases, @/languages/lib/languages
**API** : /versions, /languages, /, /:someParam, /:lang/:productVersion

### `validation.ts`

Module TypeScript. Nombre de lignes: 145.

**Fonctions** : pagelistValidationMiddleware, pathValidationMiddleware, pageValidationMiddleware, apiVersionValidationMiddleware
**Dépendances** : ../types, express, @/types, @/archives/lib/is-archived-version, @/redirects/lib/get-redirect, @/frame/lib/path-utils, @/versions/lib/non-enterprise-default-version, @/versions/lib/all-versions
