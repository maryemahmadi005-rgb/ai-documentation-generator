# Module : src/content-linter/tests

4 fichier(s), 10 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : containsLiquidElseIf, filterFiles, formatArticleError, formatLinkError, getContent, getFilenameByValue, getFrontmatterData, getPath, makeCustomErrorMessage, next
- **Dépendances** : ../lib/diff-files, @/content-render/index, @/data-directory/lib/get-data, @/frame/lib/page-data, @/frame/lib/patterns, @/frame/lib/read-frontmatter, @/frame/middleware/context/context, @/languages/lib/languages-server, @/redirects/lib/precompile, @/tests/helpers/check-url, @/versions/lib/get-applicable-versions, express

## Détail des fichiers

### `category-pages.ts`

Module TypeScript. Nombre de lignes: 214. Elements detectés: function getFrontmatterData

**Fonctions** : getFrontmatterData, next, getPath, formatArticleError
**Dépendances** : path, fs, express, walk-sync, lodash-es, github-slugger, html-entities, vitest, @/frame/lib/read-frontmatter, @/content-render/index, @/versions/lib/get-applicable-versions, @/frame/middleware/context/context

### `lint-files.ts`

Module TypeScript. Nombre de lignes: 386.

**Fonctions** : formatLinkError, getContent, filterFiles
**Dépendances** : url, path, js-yaml, fs/promises, slash, walk-sync, lodash-es, vitest, @/languages/lib/languages-server, ../lib/diff-files

### `lint-frontmatter-links.ts`

Module TypeScript. Nombre de lignes: 86. Elements detectés: function makeCustomErrorMessage

**Fonctions** : containsLiquidElseIf, makeCustomErrorMessage
**Dépendances** : vitest, @/frame/lib/page-data, @/redirects/lib/precompile, @/tests/helpers/check-url

### `site-data-references.ts`

Module TypeScript. Nombre de lignes: 54. Elements detectés: function getFilenameByValue

**Fonctions** : getFilenameByValue
**Dépendances** : path, lodash-es, vitest, @/frame/lib/patterns, @/data-directory/lib/get-data
