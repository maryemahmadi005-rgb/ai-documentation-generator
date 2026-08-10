# Module : src/content-render/unified

21 fichier(s), 1 classe(s), 75 fonction(s).

## Vue d'ensemble

- **Classes principales** : TitleFromAutotitleError
- **Fonctions principales** : addTableAccessibilityLabels, alerts, annotate, btnIcon, buildPromptData, chunkBy, codeHeader, copilotIcon, createAnnotatedNode, createMarkdownOnlyProcessor, createMinimalProcessor, createProcessor, createWbrElement, extractTextFromNode, fastTextOnly
- **Dépendances** : ../../assets/lib/image-density, ../lib/prompt-id, ./code-header, ./copilot-prompt, @/archives/lib/old-versions-utils, @/content-render/unified/processor, @/content-render/unified/text-only, @/frame/lib/find-page, @/frame/lib/get-mini-toc-items, @/frame/lib/path-utils, @/frame/lib/patterns, @/observability/logger

## Détail des fichiers

### `alerts.ts`

Module TypeScript. Nombre de lignes: 85. Elements detectés: function getAlertKey, function removeAlertSyntax, function removeAlertSyntax

**Fonctions** : alerts, getAlertKey, removeAlertSyntax, getOcticonSVG
**Dépendances** : unist-util-visit, hastscript, @primer/octicons, hast, @/observability/logger

### `annotate.ts`

Module TypeScript. Nombre de lignes: 289.

**Fonctions** : annotate, createAnnotatedNode, validate, getRegexp, hasChar, chunkBy, matchComment, getSubnav, template, mdToHast, processAutotitleInMdast, removeComment, getPreMeta
**Dépendances** : js-yaml, fs, lodash-es, unist-util-visit, unist, hast, hastscript, mdast-util-from-markdown, mdast-util-to-hast, mdast, ./code-header, @/frame/lib/find-page

### `code-header.ts`

Module TypeScript. Nombre de lignes: 116. Elements detectés: function wrapCodeExample

**Fonctions** : codeHeader, wrapCodeExample, header, btnIcon, getPreMeta
**Dépendances** : js-yaml, fs, unist-util-visit, hastscript, @primer/octicons, parse5, hast-util-from-parse5, imurmurhash, ./copilot-prompt, ../lib/prompt-id, hast

### `collect-mini-toc.ts`

Module TypeScript. Nombre de lignes: 67. Elements detectés: function hasClassName, function getClassString

**Fonctions** : hasClassName, getClassString
**Dépendances** : unist-util-visit-parents, hast-util-to-string, unified, hast, @/frame/lib/get-mini-toc-items

### `copilot-prompt.ts`

Module TypeScript. Nombre de lignes: 91. Elements detectés: function buildPromptData, function promptOnly, function promptAndContext

**Fonctions** : getPrompt, buildPromptData, promptOnly, promptAndContext, findMatchingCode, copilotIcon
**Dépendances** : unist-util-find, hastscript, @primer/octicons, parse5, hast-util-from-parse5, ./code-header, @/observability/logger, ../lib/prompt-id, hast

### `heading-links.ts`

Module TypeScript. Nombre de lignes: 29.

**Fonctions** : headingLinks
**Dépendances** : unist-util-visit, hastscript, hast

### `index.ts`

Module TypeScript. Nombre de lignes: 66. Elements detectés: function stripPositions

**Fonctions** : renderUnified, renderUnifiedToHast, stripPositions, renderMarkdown
**Dépendances** : unified, hast, @/content-render/unified/text-only, @/content-render/unified/processor, @/types

### `module-types.d.ts`

Module TypeScript. Nombre de lignes: 24.

**Dépendances** : unified, lowlight

### `parse-info-string.ts`

Module TypeScript. Nombre de lignes: 37. Elements detectés: function strToObj

**Fonctions** : parseInfoString, strToObj
**Dépendances** : unist-util-visit, unist

### `processor.ts`

Module TypeScript. Nombre de lignes: 120.

**Fonctions** : createProcessor, createMarkdownOnlyProcessor, createMinimalProcessor
**Dépendances** : unified, remark-parse, remark-gfm, remark-gemoji-to-emoji, remark-rehype, rehype-raw, rehype-slug, rehype-highlight, lowlight, highlight.js/lib/languages/dockerfile, highlight.js/lib/languages/http, highlight.js/lib/languages/groovy

### `rewrite-asset-img-tags.ts`

Module TypeScript. Nombre de lignes: 80. Elements detectés: function isAssetImg, function injectMaxWidth

**Fonctions** : isAssetImg, rewriteAssetImgTags, injectMaxWidth
**Dépendances** : hast, unist-util-visit, ../../assets/lib/image-density

### `rewrite-asset-urls.ts`

Module TypeScript. Nombre de lignes: 58. Elements detectés: function isAssetOrPublicImg, function getNewSrc

**Fonctions** : isAssetOrPublicImg, rewriteImgSources, getNewSrc
**Dépendances** : fs, hast, unist-util-visit, @/observability/logger

### `rewrite-empty-table-rows.ts`

Module TypeScript. Nombre de lignes: 69.

**Fonctions** : rewriteEmptyTableRows
**Dépendances** : unist-util-visit, hast

### `rewrite-for-rowheaders.ts`

Module TypeScript. Nombre de lignes: 60.

**Fonctions** : rewriteForRowheaders
**Dépendances** : unist-util-visit-parents, hast

### `rewrite-local-links.ts`

Module TypeScript. Nombre de lignes: 273. Elements detectés: function logError

**Classes** : TitleFromAutotitleError
**Fonctions** : logError, rewriteLocalLinks, processTree, processLinkNode, getNewTitleSetter, getNewTitle, getNewHref
**Dépendances** : path, mdast, unist, strip-ansi, unist-util-visit, fastest-levenshtein, @/frame/lib/path-utils, @/archives/lib/old-versions-utils, @/frame/lib/patterns, @/observability/logger, @/versions/lib/enterprise-server-releases, @/versions/lib/non-enterprise-default-version

### `rewrite-table-captions.ts`

Module TypeScript. Nombre de lignes: 120. Elements detectés: function isTableElement, function isHeadingElement, function hasExistingAccessibilityAttributes

**Fonctions** : isTableElement, isHeadingElement, hasExistingAccessibilityAttributes, hasExistingCaption, findPrecedingHeading, extractTextFromNode, addTableAccessibilityLabels
**Dépendances** : unist-util-visit, unist, hast

### `rewrite-thead-th-scope.ts`

Module TypeScript. Nombre de lignes: 32.

**Fonctions** : rewriteTheadThScope
**Dépendances** : unist-util-visit-parents, hast, unified

### `text-only.ts`

Module TypeScript. Nombre de lignes: 21.

**Fonctions** : fastTextOnly
**Dépendances** : html-entities

### `use-english-headings.ts`

Module TypeScript. Nombre de lignes: 31.

**Fonctions** : useEnglishHeadings
**Dépendances** : github-slugger, html-entities, hast-util-to-string, unist-util-visit, hast

### `wrap-code-terms.ts`

Module TypeScript. Nombre de lignes: 80. Elements detectés: function withBreakOpportunities, function createWbrElement, function splitTextNode

**Fonctions** : withBreakOpportunities, createWbrElement, splitTextNode, insertWordBreaks, hasTableAncestor, wrapCodeTerms
**Dépendances** : hast, unist-util-visit-parents, unified

### `wrap-procedural-images.ts`

Module TypeScript. Nombre de lignes: 59. Elements detectés: function isImgElement, function insideOlLi, function visitor

**Fonctions** : isImgElement, insideOlLi, visitor, wrapProceduralImages
**Dépendances** : hast, unist-util-visit-parents
