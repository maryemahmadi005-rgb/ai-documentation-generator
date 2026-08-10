# Module : src/article-api/lib

8 fichier(s), 18 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : collapseBlankLines, extractManualContent, flattenTocItems, getAllTocItems, getLinkData, hasMarkdownLinks, loadTemplate, normalizeRenderedMarkdown, recurse, renderCompositionVariants, renderPropFast, renderProperties, renderTypeConstraints, resolvePath, shouldReference
- **Dépendances** : ./resolve-path, @/article-api/transformers/types, @/content-render/index, @/content-render/liquid/index, @/frame/lib/find-page, @/types, @/versions/lib/all-versions, @gr2m/gray-matter, fs, path, url

## Détail des fichiers

### `get-all-toc-items.ts`

Module TypeScript. Nombre de lignes: 151. Elements detectés: function recurse

**Fonctions** : getAllTocItems, flattenTocItems, recurse, hasMarkdownLinks, renderPropFast
**Dépendances** : @/types, @/article-api/transformers/types, ./resolve-path, @/content-render/liquid/index

### `get-link-data.ts`

Module TypeScript. Nombre de lignes: 44.

**Fonctions** : getLinkData
**Dépendances** : @/types, @/article-api/transformers/types

### `graphql-helpers.ts`

Module TypeScript. Nombre de lignes: 25.

**Fonctions** : extractManualContent
**Dépendances** : @/types, @/content-render/index, @gr2m/gray-matter

### `load-template.ts`

Module TypeScript. Nombre de lignes: 29.

**Fonctions** : loadTemplate
**Dépendances** : fs, path, url

### `normalize-markdown.ts`

Module TypeScript. Nombre de lignes: 23.

**Fonctions** : collapseBlankLines, normalizeRenderedMarkdown

### `resolve-path.ts`

Module TypeScript. Nombre de lignes: 55.

**Fonctions** : resolvePath
**Dépendances** : @/frame/lib/find-page, @/versions/lib/all-versions, @/types

### `strip-html-comments.ts`

Module TypeScript. Nombre de lignes: 28.

**Fonctions** : stripHtmlComments, stripHtmlCommentsAndNormalizeWhitespace

### `summarize-schema.ts`

Module TypeScript. Nombre de lignes: 238. Elements detectés: function renderTypeConstraints, function shouldReference, function renderCompositionVariants

**Fonctions** : renderTypeConstraints, shouldReference, renderCompositionVariants, renderProperties, summarizeSchema
