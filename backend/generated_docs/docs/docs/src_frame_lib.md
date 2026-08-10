# Module : src/frame/lib

23 fichier(s), 6 classe(s), 53 fonction(s).

## Vue d'ensemble

- **Classes principales** : FrontmatterErrorsError, FrontmatterParsingError, Page, Permalink, creates, has
- **Fonctions principales** : addToCollection, assertUniqueChildren, buildMiniTocFromCollected, buildNestedToc, calculateDefaultDelay, checkNodeVersion, compressStringToCache, createApp, createMapFromArray, createTree, decompressFromCache, equalArray, equalSets, fetchStream, fetchWithRetry
- **Dépendances** : ./create-tree, ./encode-bracketed-parentheses, ./fetch-utils, ./frontmatter, ./page, ./page-data, ./patterns, ./permalink, ./read-file-contents, @/content-render/index, @/data-directory/lib/get-data, @/frame/lib/find-page

## Détail des fichiers

### `app.ts`

Module TypeScript. Nombre de lignes: 8. Elements detectés: function createApp

**Fonctions** : createApp
**Dépendances** : express, @/frame/middleware

### `check-node-version.ts`

Module TypeScript. Nombre de lignes: 18.

**Fonctions** : checkNodeVersion
**Dépendances** : fs, semver, @/observability/logger

### `constants.ts`

Module TypeScript. Nombre de lignes: 46.

### `cookie-settings.ts`

Module TypeScript. Nombre de lignes: 10.

**Dépendances** : cookie

### `create-tree.ts`

Module TypeScript. Nombre de lignes: 185.

**Classes** : has
**Fonctions** : createTree, equalArray, getMtime, assertUniqueChildren
**Dépendances** : path, fs/promises, ./page, @/types, @/observability/logger

### `fetch-utils.ts`

Module TypeScript. Nombre de lignes: 215. Elements detectés: function calculateDefaultDelay, function sleep, function getHost

**Fonctions** : calculateDefaultDelay, sleep, getHost, fetchWithTimeout, fetchWithRetry, fetchStream
**Dépendances** : @/observability/lib/statsd

### `find-page-in-site-tree.ts`

Module TypeScript. Nombre de lignes: 51.

**Fonctions** : findPageInSiteTree
**Dépendances** : @/types, ./patterns

### `find-page.ts`

Module TypeScript. Nombre de lignes: 25.

**Fonctions** : findPage
**Dépendances** : @/frame/lib/patterns, @/redirects/lib/get-redirect, @/types

### `frontmatter.ts`

Module TypeScript. Nombre de lignes: 480.

**Fonctions** : frontmatter
**Dépendances** : ajv, @/frame/lib/read-frontmatter, @/versions/lib/all-versions, @/tools/lib/all-tools, @/data-directory/lib/get-data

### `get-link-data.ts`

Module TypeScript. Nombre de lignes: 93.

**Fonctions** : getLinkData, processLink
**Dépendances** : path, @/frame/lib/find-page, @/versions/lib/non-enterprise-default-version, @/versions/lib/remove-fpt-from-path, @/content-render/index, @/languages/lib/render-with-fallback, @/types

### `get-mini-toc-items.ts`

Module TypeScript. Nombre de lignes: 129. Elements detectés: function buildNestedToc, function minimalMiniToc

**Fonctions** : buildMiniTocFromCollected, buildNestedToc, minimalMiniToc, getAutomatedPageMiniTocItems
**Dépendances** : @/content-render/index, @/types

### `get-remote-json.ts`

Module TypeScript. Nombre de lignes: 128. Elements detectés: function compressStringToCache, function decompressFromCache

**Fonctions** : compressStringToCache, decompressFromCache, getRemoteJSON
**Dépendances** : path, fs, crypto, zlib, ./fetch-utils, @/observability/lib/statsd

### `load-yaml.ts`

Module TypeScript. Nombre de lignes: 24.

**Fonctions** : loadYaml
**Dépendances** : js-yaml

### `page-data.ts`

Module TypeScript. Nombre de lignes: 431. Elements detectés: class FrontmatterParsingError extends Error {, function setCategoryApplicableVersions

**Classes** : FrontmatterParsingError
**Fonctions** : loadUnversionedTree, setCategoryApplicableVersions, equalSets, translateTree, loadSiteTree, versionPages, loadPageList, addToCollection, createMapFromArray, loadPageMap
**Dépendances** : path, @/observability/logger, @/languages/lib/languages-server, @/languages/lib/languages, @/types, @/versions/lib/all-versions, ./create-tree, @/versions/lib/non-enterprise-default-version, ./read-file-contents, ./page, ./permalink, ./frontmatter

### `page.ts`

Module TypeScript. Nombre de lignes: 373. Elements detectés: class Page {

**Classes** : FrontmatterErrorsError, Page
**Dépendances** : assert, path, fs/promises, @/frame/lib/strip-outer-tag, @/versions/lib/get-applicable-versions, @/redirects/lib/permalinks, @/languages/lib/get-english-headings, @/languages/lib/get-alert-titles, ./permalink, @/content-render/index, @/products/lib/all-products, slash

### `path-utils.ts`

Module TypeScript. Nombre de lignes: 139.

**Fonctions** : getLangFromPath, getPathWithLanguage, getPathWithoutLanguage, getPathWithoutVersion, getVersionStringFromPath, getVersionObjectFromPath, getProductStringFromPath, getCategoryStringFromPath
**Dépendances** : slash, path, ./patterns, @/versions/lib/enterprise-server-releases, @/products/lib/all-products, @/versions/lib/all-versions, @/versions/lib/non-enterprise-default-version

### `patterns.ts`

Module TypeScript. Nombre de lignes: 73.

### `permalink.ts`

Module TypeScript. Nombre de lignes: 85. Elements detectés: function intern, class Permalink {

**Classes** : creates, Permalink
**Fonctions** : intern
**Dépendances** : assert, path, ./patterns, @/versions/lib/remove-fpt-from-path

### `read-file-contents.ts`

Module TypeScript. Nombre de lignes: 18.

**Fonctions** : fmfromf
**Dépendances** : fs/promises, ./encode-bracketed-parentheses, ./frontmatter

### `read-frontmatter.ts`

Module TypeScript. Nombre de lignes: 87. Elements detectés: function readFrontmatter

**Fonctions** : readFrontmatter
**Dépendances** : @gr2m/gray-matter, ajv, @/tests/lib/validate-json-schema

### `read-json-file.ts`

Module TypeScript. Nombre de lignes: 78.

**Fonctions** : readJsonFile, readCompressedJsonFile, readCompressedJsonFileFallback, readCompressedJsonFileFallbackLazily
**Dépendances** : fs, zlib, @/observability/logger

### `strip-outer-tag.ts`

Module TypeScript. Nombre de lignes: 27.

**Fonctions** : stripOuterTag

### `warm-server.ts`

Module TypeScript. Nombre de lignes: 94.

**Fonctions** : warmServer, warmServerWrapper
**Dépendances** : @/observability/lib/statsd, ./page-data, @/redirects/lib/precompile, @/observability/logger
