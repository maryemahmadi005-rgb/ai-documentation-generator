# Module : src/search/scripts/scrape/lib

5 fichier(s), 16 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : articleApiResponseToRecord, astToPlainText, buildRecordsFromApi, countArrayValues, extractFromMarkdown, extractHeadingsFromMarkdown, fetchArticleAsRecord, findIndexablePages, formatSeconds, getPopularPages, isErrorResponse, markdownToPlainText, parseMarkdown, scrapeIntoIndexJson, validateRecords
- **Dépendances** : @/frame/lib/page-data, @/languages/lib/languages-server, @/search/lib/elasticsearch-indexes, @/search/lib/elasticsearch-versions, @/search/scripts/scrape/lib/build-records-from-api, @/search/scripts/scrape/lib/find-indexable-pages, @/search/scripts/scrape/lib/search-index-records, @/search/scripts/scrape/types, bottleneck, boxen, chalk, dotenv

## Détail des fichiers

### `build-records-from-api.ts`

Module TypeScript. Nombre de lignes: 435.

**Fonctions** : parseMarkdown, astToPlainText, extractFromMarkdown, extractHeadingsFromMarkdown, markdownToPlainText, articleApiResponseToRecord, isErrorResponse, fetchArticleAsRecord, buildRecordsFromApi
**Dépendances** : bottleneck, chalk, dotenv, boxen, mdast-util-from-markdown, mdast-util-to-string, unist-util-visit, micromark-extension-gfm, mdast-util-gfm, github-slugger, unist, @/languages/lib/languages-server

### `find-indexable-pages.ts`

Module TypeScript. Nombre de lignes: 16.

**Fonctions** : findIndexablePages
**Dépendances** : @/frame/lib/page-data, @/search/scripts/scrape/types

### `popular-pages.ts`

Module TypeScript. Nombre de lignes: 58.

**Fonctions** : getPopularPages
**Dépendances** : path, fs, fs/promises, @/search/lib/elasticsearch-versions, @/search/scripts/scrape/types

### `scrape-into-index-json.ts`

Module TypeScript. Nombre de lignes: 135.

**Fonctions** : scrapeIntoIndexJson, formatSeconds
**Dépendances** : chalk, @/languages/lib/languages-server, @/search/scripts/scrape/lib/build-records-from-api, @/search/scripts/scrape/lib/find-indexable-pages, @/search/scripts/scrape/lib/search-index-records, @/search/lib/elasticsearch-indexes, @/search/scripts/scrape/types

### `search-index-records.ts`

Module TypeScript. Nombre de lignes: 89. Elements detectés: function validateRecords, function countArrayValues

**Fonctions** : writeIndexRecords, validateRecords, countArrayValues
**Dépendances** : path, fs, fs/promises, chalk, lodash-es, @/search/scripts/scrape/types
