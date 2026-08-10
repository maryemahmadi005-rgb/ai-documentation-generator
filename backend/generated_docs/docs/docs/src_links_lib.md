# Module : src/links/lib

11 fichier(s), 1 classe(s), 59 fonction(s).

## Vue d'ensemble

- **Classes principales** : RedirectedFragmentValidator
- **Fonctions principales** : buildLineOffsets, buildRenderContext, checkAssetLink, checkInternalLink, computeHeadingIds, createLiquidContext, createRedirectSuggestion, createSummary, definitionMatcher, equalArray, extractDomain, extractLinkText, extractLinksFromMarkdown, extractLinksWithLiquid, findLineNumber
- **Dépendances** : @/archives/lib/is-archived-version, @/content-render/index, @/content-render/unified/processor, @/data-directory/lib/get-data, @/frame/lib/load-yaml, @/frame/lib/page-data, @/frame/lib/patterns, @/frame/lib/read-frontmatter, @/frame/lib/warm-server, @/frame/middleware/context/context, @/frame/middleware/find-page, @/links/lib/extract-links

## Détail des fichiers

### `README.md`

### `cross-page-anchors.ts`

Module TypeScript. Nombre de lignes: 49.

**Fonctions** : validateCrossPageAnchors
**Dépendances** : @/links/lib/link-report

### `excluded-links.ts`

Module TypeScript. Nombre de lignes: 22.

**Dépendances** : js-yaml, fs

### `excluded-links.yml`

### `extract-links.ts`

Module TypeScript. Nombre de lignes: 534. Elements detectés: function buildLineOffsets, function getLineAndColumn, function extractLinkText

**Fonctions** : buildLineOffsets, getLineAndColumn, extractLinkText, extractLinksFromMarkdown, createLiquidContext, getCachedRenderLiquid, renderMarkdownLiquid, extractLinksWithLiquid, renderAndExtractLinks, getRelativePath, normalizeLinkPath, resolveInternalLinkKey, checkInternalLink, checkAssetLink, isAssetLink
**Dépendances** : fs, path, @/observability/logger, @/versions/lib/all-versions, @/versions/lib/enterprise-server-releases, @/data-directory/lib/get-data, @/redirects/lib/get-redirect, @/archives/lib/is-archived-version, @/types

### `heading-anchors.ts`

Module TypeScript. Nombre de lignes: 110. Elements detectés: function stripHtmlTags, function processNonCode

**Fonctions** : headingTextToPlain, stripHtmlTags, processNonCode, computeHeadingIds
**Dépendances** : github-slugger

### `link-report.ts`

Module TypeScript. Nombre de lignes: 474.

**Fonctions** : groupByTarget, createRedirectSuggestion, sortOccurrencesByFile, groupBrokenLinks, extractDomain, groupExternalLinksByDomain, createSummary, generateInternalLinkReport, generateExternalLinkReport, renderGroups, reportToMarkdown, generatePRComment, generateSampleReports

### `page-anchors.ts`

Module TypeScript. Nombre de lignes: 156.

**Fonctions** : versionFromResolvedKey, findLinkLines, resolveLinkKeyForVersion, isAnchorCheckableTarget, getTables, buildRenderContext, getPageHeadingIds
**Dépendances** : @/types, @/versions/lib/all-versions, @/versions/middleware/features, @/data-directory/lib/get-data, @/links/lib/heading-anchors

### `update-internal-links.ts`

Module TypeScript. Nombre de lignes: 640.

**Fonctions** : updateInternalLinks, updateFile, isDefinition, isLink, definitionMatcher, linkMatcher, getNewFrontmatterLinkList, findLineNumber, stripLiquid, equalArray, getNewHref, resolveDestinationPage, singleStartingQuote, isSimpleQuote
**Dépendances** : fs, unist-util-visit, mdast-util-from-markdown, mdast-util-to-markdown, @/frame/lib/load-yaml, mdast, @/types, @/observability/logger, @/frame/lib/read-frontmatter, @/redirects/lib/precompile, @/frame/lib/patterns, @/frame/lib/page-data

### `validate-docs-urls.ts`

Module TypeScript. Nombre de lignes: 130.

**Fonctions** : validateDocsUrl, isEnterpriseCloudRedirectOnly, renderInnerHTML, next, stripLanguagePrefix
**Dépendances** : express, cheerio, @/frame/lib/warm-server, @/content-render/index, @/versions/middleware/short-versions, @/frame/middleware/context/context, @/versions/middleware/features, @/frame/middleware/find-page, @/content-render/unified/processor, @/redirects/lib/get-redirect, @/types

### `validate-redirected-fragment.ts`

Module TypeScript. Nombre de lignes: 121.

**Classes** : RedirectedFragmentValidator
**Dépendances** : @/frame/lib/warm-server, @/versions/lib/all-versions, @/versions/middleware/features, @/links/lib/extract-links, @/links/lib/heading-anchors, @/observability/logger, @/types
