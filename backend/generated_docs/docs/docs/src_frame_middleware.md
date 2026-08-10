# Module : src/frame/middleware

28 fichier(s), 2 classe(s), 51 fonction(s).

## Vue d'ensemble

- **Classes principales** : AbortError, has
- **Fonctions principales** : abort, archivedCacheControl, assetCacheControl, blockIndex, buildArticlePath, buildInfo, buildMiniTocItems, buildRenderedPage, buildRenderedPageHast, cacheControlFactory, categoriesForSupport, contentTypeCacheControl, defaultCacheControl, fastHead, favicons
- **Dépendances** : ./abort, ./cache-control, ./cookie-parser, ./handle-next-data-path, ./helmet, ./reload-tree, ./set-fastly-surrogate-key, @/archives/lib/is-archived-version, @/article-api/lib/normalize-markdown, @/article-api/middleware/article, @/article-api/middleware/pagelist, @/article-api/transformers
- **Endpoints API** : /, /*path, /_500, /_build, /_req-headers, /cookies

## Détail des fichiers

### `abort.ts`

Module TypeScript. Nombre de lignes: 37. Elements detectés: class AbortError extends Error {

**Classes** : AbortError
**Fonctions** : abort
**Dépendances** : express, @/observability/lib/statsd, @/types

### `api.ts`

Module TypeScript. Nombre de lignes: 67.

**Dépendances** : express, http-proxy-middleware, @/observability/logger, @/events/middleware, @/rest/api/anchor-redirect, @/search/middleware/ai-search, @/search/middleware/ai-search-local-proxy, @/search/middleware/search-routes, @/article-api/middleware/pagelist, @/article-api/middleware/article, @/webhooks/middleware/webhooks, @/types
**API** : /cookies, /, /*path

### `block-robots.ts`

Module TypeScript. Nombre de lignes: 26. Elements detectés: function middleware

**Fonctions** : blockIndex, middleware
**Dépendances** : express, @/products/lib/all-products, @/versions/lib/enterprise-server-releases

### `build-info.ts`

Module TypeScript. Nombre de lignes: 12.

**Fonctions** : buildInfo
**Dépendances** : express, ./cache-control

### `cache-control.ts`

Module TypeScript. Nombre de lignes: 111. Elements detectés: function cacheControlFactory

**Fonctions** : cacheControlFactory, defaultCacheControl, contentTypeCacheControl, languageCacheControl, languageAndVersionCacheControl, assetCacheControl, archivedCacheControl
**Dépendances** : express, @/observability/logger

### `categories-for-support.ts`

Module TypeScript. Nombre de lignes: 65.

**Fonctions** : categoriesForSupport, findArticlesPerCategory
**Dépendances** : express, ./cache-control, @/types

### `cookie-parser.ts`

Module TypeScript. Nombre de lignes: 13.

**Dépendances** : cookie-parser, @/frame/lib/cookie-settings

### `fast-head.ts`

Module TypeScript. Nombre de lignes: 16.

**Fonctions** : fastHead
**Dépendances** : express, @/types, ./cache-control

### `fastly-cache-test.ts`

Module TypeScript. Nombre de lignes: 83.

**Dépendances** : express, crypto
**API** : /*path

### `favicons.ts`

Module TypeScript. Nombre de lignes: 67. Elements detectés: function getBuffer

**Fonctions** : getBuffer, favicons
**Dépendances** : fs, express, @/types, ./set-fastly-surrogate-key, ./cache-control

### `find-page.ts`

Module TypeScript. Nombre de lignes: 114.

**Fonctions** : findPage, rereadByPath
**Dépendances** : path, fs, express, @/frame/lib/constants, @/frame/lib/page, @/languages/lib/languages-server, @/types

### `handle-next-data-path.ts`

Module TypeScript. Nombre de lignes: 34.

**Fonctions** : handleNextDataPath
**Dépendances** : express, @/observability/lib/statsd, @/types

### `healthcheck.ts`

Module TypeScript. Nombre de lignes: 20.

**Fonctions** : healthcheck
**Dépendances** : express, ./cache-control, @/observability/lib/statsd
**API** : /

### `helmet.ts`

Module TypeScript. Nombre de lignes: 118.

**Fonctions** : helmetMiddleware
**Dépendances** : @/archives/lib/is-archived-version, @/languages/lib/languages-server, @/versions/lib/version-satisfies-range, express, helmet, crypto, @/color-schemes/lib/color-mode-script

### `index.ts`

Module TypeScript. Nombre de lignes: 247.

**Fonctions** : index
**Dépendances** : fs, path, express, ./abort, ./helmet, ./cookie-parser, @/observability/middleware/handle-errors, @/observability/middleware/express-metrics, ./handle-next-data-path, @/languages/middleware/detect-language, @/versions/middleware/detect-version, ./reload-tree
**API** : /_build, /_req-headers, /_500, /*path

### `llms-txt.ts`

Module TypeScript. Nombre de lignes: 19.

**Dépendances** : fs/promises, express, @/observability/lib/statsd, @/observability/middleware/catch-middleware-error, @/frame/middleware/cache-control
**API** : /

### `manifest-json.ts`

Module TypeScript. Nombre de lignes: 64.

**Fonctions** : manifestJson
**Dépendances** : express, fs/promises, path, ./cache-control

### `mock-va-portal.ts`

Module TypeScript. Nombre de lignes: 58. Elements detectés: function triggerStart, function triggerStop

**Fonctions** : triggerStart, triggerStop, mockVaPortal
**Dépendances** : express, @/types

### `next.ts`

Module TypeScript. Nombre de lignes: 18. Elements detectés: function renderPageWithNext

**Fonctions** : renderPageWithNext
**Dépendances** : next, express, @/types

### `reload-tree.ts`

Module TypeScript. Nombre de lignes: 66. Elements detectés: function getMtimes

**Fonctions** : reloadTree, getMtimes
**Dépendances** : path, express, @/types, @/languages/lib/languages-server, @/frame/lib/create-tree, @/frame/lib/warm-server, @/frame/lib/page-data, @/redirects/lib/precompile

### `render-page.ts`

Module TypeScript. Nombre de lignes: 192. Elements detectés: function buildMiniTocItems

**Fonctions** : buildRenderedPage, buildRenderedPageHast, buildMiniTocItems, renderPage
**Dépendances** : express, @github/failbot, lodash-es, @/observability/logger, @/frame/lib/get-mini-toc-items, @/frame/lib/patterns, @/observability/lib/failbot, @/observability/lib/statsd, @/types, @/versions/lib/all-versions, @/article-api/transformers, @/article-api/lib/normalize-markdown

### `req-headers.ts`

Module TypeScript. Nombre de lignes: 8.

**Fonctions** : reqHeaders
**Dépendances** : express, ./cache-control

### `resolve-carousels.ts`

Module TypeScript. Nombre de lignes: 149. Elements detectés: function buildArticlePath, function tryResolveArticlePath, function getPageHref

**Classes** : has
**Fonctions** : buildArticlePath, tryResolveArticlePath, getPageHref, resolveCarousels
**Dépendances** : @/types, express, @/frame/lib/find-page, @/content-render/index, @/frame/lib/permalink, @/observability/logger/index

### `robots.ts`

Module TypeScript. Nombre de lignes: 22.

**Fonctions** : robots
**Dépendances** : express, ./cache-control, @/types

### `safe-redirect.ts`

Module TypeScript. Nombre de lignes: 25.

**Fonctions** : safeRedirectUrl, safeRedirect
**Dépendances** : express, @/types

### `set-fastly-surrogate-key.ts`

Module TypeScript. Nombre de lignes: 119.

**Fonctions** : setFastlySurrogateKey, setDefaultFastlySurrogateKey, setLanguageFastlySurrogateKey, makeLanguageSurrogateKey, makeContentSurrogateKeys, makePageSurrogateKey, productSurrogateId, versionSurrogateKey
**Dépendances** : express, @/types

### `trailing-slashes.ts`

Module TypeScript. Nombre de lignes: 22.

**Fonctions** : trailingSlashes
**Dépendances** : express, @/types, ./cache-control

### `url-decode.ts`

Module TypeScript. Nombre de lignes: 25.

**Fonctions** : urlDecode
**Dépendances** : express, @/types
