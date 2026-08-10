# Module : src/frame/tests

28 fichier(s), 1 classe(s), 10 fonction(s).

## Vue d'ensemble

- **Classes principales** : has
- **Fonctions principales** : abortError, allowIndex, expectAggressiveCaching, getMaxAge, getPage, heading, makeRequestResponse, status, timeoutError, validate
- **Dépendances** : ../middleware/resolve-carousels, @/content-render/index, @/frame/lib/create-tree, @/frame/lib/fetch-utils, @/frame/lib/find-page, @/frame/lib/find-page-in-site-tree, @/frame/lib/frontmatter, @/frame/lib/get-mini-toc-items, @/frame/lib/get-remote-json, @/frame/lib/load-yaml, @/frame/lib/page, @/frame/lib/page-data

## Détail des fichiers

### `api.ts`

Module TypeScript. Nombre de lignes: 15.

**Dépendances** : vitest, @/tests/helpers/e2etest

### `block-robots.ts`

Module TypeScript. Nombre de lignes: 72. Elements detectés: function allowIndex

**Fonctions** : allowIndex
**Dépendances** : vitest, @/frame/middleware/block-robots, @/products/lib/all-products, @/versions/lib/enterprise-server-releases

### `content.ts`

Module TypeScript. Nombre de lignes: 46.

**Dépendances** : path, vitest, walk-sync, @/frame/lib/create-tree

### `favicons.ts`

Module TypeScript. Nombre de lignes: 50. Elements detectés: function getMaxAge, function expectAggressiveCaching

**Fonctions** : getMaxAge, expectAggressiveCaching
**Dépendances** : vitest, @/frame/middleware/set-fastly-surrogate-key, @/tests/helpers/e2etest

### `fetch-utils.test.ts`

Module TypeScript. Nombre de lignes: 161. Elements detectés: function timeoutError, function abortError

**Fonctions** : timeoutError, abortError
**Dépendances** : vitest, @/frame/lib/fetch-utils

### `find-page-middleware.ts`

Module TypeScript. Nombre de lignes: 139. Elements detectés: function makeRequestResponse

**Fonctions** : makeRequestResponse, status
**Dépendances** : url, path, http, net, vitest, express, @/frame/lib/page, @/frame/middleware/find-page, @/types

### `find-page.ts`

Module TypeScript. Nombre de lignes: 33.

**Dépendances** : url, path, vitest, @/frame/lib/page, @/frame/lib/find-page, @/types

### `get-remote-json.ts`

Module TypeScript. Nombre de lignes: 97.

**Dépendances** : fs, path, os, rimraf, vitest, nock, @/frame/lib/get-remote-json

### `gitignore.ts`

Module TypeScript. Nombre de lignes: 11.

**Dépendances** : fs/promises, path, vitest

### `llms-txt.ts`

Module TypeScript. Nombre de lignes: 32.

**Dépendances** : vitest, @/tests/helpers/e2etest

### `load-yaml.ts`

Module TypeScript. Nombre de lignes: 12.

**Dépendances** : vitest, @/frame/lib/load-yaml

### `manifest.ts`

Module TypeScript. Nombre de lignes: 66.

**Dépendances** : vitest, sharp, @/frame/middleware/set-fastly-surrogate-key, @/tests/helpers/e2etest

### `mini-toc-items.ts`

Module TypeScript. Nombre de lignes: 127. Elements detectés: function heading

**Fonctions** : heading
**Dépendances** : vitest, @/frame/lib/get-mini-toc-items

### `next.ts`

Module TypeScript. Nombre de lignes: 15.

**Dépendances** : vitest, @/tests/helpers/e2etest

### `non-child-pages-resolution.test.ts`

Module TypeScript. Nombre de lignes: 213.

**Dépendances** : vitest, path, fs

### `page.ts`

Module TypeScript. Nombre de lignes: 431.

**Fonctions** : getPage
**Dépendances** : url, path, cheerio, vitest, @/frame/lib/page, @/versions/lib/all-versions, @/versions/lib/enterprise-server-releases, @/versions/lib/non-enterprise-default-version, @/types

### `pages.ts`

Module TypeScript. Nombre de lignes: 145.

**Classes** : has
**Dépendances** : path, vitest, github-slugger, html-entities, lodash-es, @/frame/lib/page-data, @/languages/lib/languages-server, @/content-render/index, @/frame/lib/patterns, @/versions/lib/remove-fpt-from-path, @/types

### `path-utils.ts`

Module TypeScript. Nombre de lignes: 40.

**Dépendances** : vitest, @/frame/lib/path-utils

### `permalink.ts`

Module TypeScript. Nombre de lignes: 64.

**Dépendances** : vitest, @/frame/lib/permalink, @/versions/lib/enterprise-server-releases, @/versions/lib/non-enterprise-default-version, @/versions/lib/get-applicable-versions

### `read-frontmatter.ts`

Module TypeScript. Nombre de lignes: 137.

**Dépendances** : vitest, @/frame/lib/read-frontmatter, @/frame/lib/frontmatter

### `resolve-carousels.test.ts`

Module TypeScript. Nombre de lignes: 335.

**Dépendances** : vitest, express, @/types, @/frame/lib/find-page, ../middleware/resolve-carousels

### `robots-txt.ts`

Module TypeScript. Nombre de lignes: 36.

**Dépendances** : vitest, @/frame/middleware/set-fastly-surrogate-key, @/tests/helpers/e2etest

### `secure-files.ts`

Module TypeScript. Nombre de lignes: 43.

**Dépendances** : fs/promises, vitest, glob

### `server.ts`

Module TypeScript. Nombre de lignes: 425.

**Dépendances** : csp-parse, vitest, @/versions/lib/enterprise-server-releases, @/tests/helpers/e2etest, @/tests/helpers/conditional-runs, @/frame/lib/page-data

### `site-tree.ts`

Module TypeScript. Nombre de lignes: 64. Elements detectés: function validate

**Fonctions** : validate
**Dépendances** : vitest, @/tests/lib/validate-json-schema, @/tests/helpers/schemas/site-tree-schema, @/versions/lib/enterprise-server-releases, @/frame/lib/page-data, @/versions/lib/non-enterprise-default-version, @/tests/helpers/schemas, @/types, @/frame/lib/find-page-in-site-tree

### `strip-outer-tag.ts`

Module TypeScript. Nombre de lignes: 30.

**Dépendances** : vitest, @/frame/lib/strip-outer-tag

### `toc-links.ts`

Module TypeScript. Nombre de lignes: 44.

**Dépendances** : vitest, @/frame/lib/page-data, @/content-render/index, @/versions/lib/all-versions, @/types

### `url-encoding.ts`

Module TypeScript. Nombre de lignes: 58.

**Dépendances** : vitest, @/tests/helpers/e2etest
