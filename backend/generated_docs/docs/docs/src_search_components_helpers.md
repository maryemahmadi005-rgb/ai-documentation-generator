# Module : src/search/components/helpers

3 fichier(s), 13 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : executeAISearch, executeCombinedSearch, executeGeneralSearch, extractMarkdownLinks, extractProductFromDocsUrl, fixCodeBlocks, fixEmphasis, fixImages, fixIncompleteMarkdown, fixInlineCode, fixLinks, fixTables, generateAISearchLinksJson
- **Dépendances** : @/events/components/event-groups, @/events/components/events, @/events/types, @/search/lib/sanitize-search-query, @/search/types, @/versions/components/useVersion, next/router

## Détail des fichiers

### `ai-search-links-json.ts`

Module TypeScript. Nombre de lignes: 85. Elements detectés: function extractMarkdownLinks, function extractProductFromDocsUrl

**Fonctions** : generateAISearchLinksJson, extractMarkdownLinks, extractProductFromDocsUrl

### `execute-search-actions.ts`

Module TypeScript. Nombre de lignes: 96.

**Fonctions** : executeGeneralSearch, executeAISearch, executeCombinedSearch
**Dépendances** : @/events/types, @/search/types, @/versions/components/useVersion, next/router, @/events/components/events, @/events/components/event-groups, @/search/lib/sanitize-search-query

### `fix-incomplete-markdown.ts`

Module TypeScript. Nombre de lignes: 133. Elements detectés: function fixCodeBlocks, function fixInlineCode, function fixLinks

**Fonctions** : fixIncompleteMarkdown, fixCodeBlocks, fixInlineCode, fixLinks, fixImages, fixEmphasis, fixTables
