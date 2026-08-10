# Module : src/languages/lib

7 fichier(s), 5 classe(s), 14 fonction(s).

## Vue d'ensemble

- **Classes principales** : EmptyTitleError, LiquidError, UngettableError, for, so
- **Fonctions principales** : carefulGet, carefulGetWrapper, correctTranslatedContentStrings, createTranslationFallbackComment, createTranslationFunctions, getAlertTitles, getCommonFallback, getEnglishHeadings, getHeadings, getRoot, joinDanglingMarkers, pathLanguagePrefixed, renderContentWithFallback, translate
- **Dépendances** : ./languages, ./languages-server, ./languages-server.ts, @/content-render/index, @/content-render/unified/rewrite-local-links, @/data-directory/lib/get-data, @/frame/components/context/MainContext, @/frame/lib/constants, @/frame/lib/find-page, @/frame/lib/page, @/observability/logger, @/types

## Détail des fichiers

### `correct-translation-content.ts`

Module TypeScript. Nombre de lignes: 2438.

**Classes** : so
**Fonctions** : correctTranslatedContentStrings, joinDanglingMarkers

### `get-alert-titles.ts`

Module TypeScript. Nombre de lignes: 36.

**Fonctions** : getAlertTitles
**Dépendances** : fs/promises, path, js-yaml, @/observability/logger, ./languages-server

### `get-english-headings.ts`

Module TypeScript. Nombre de lignes: 66. Elements detectés: function getHeadings

**Fonctions** : getEnglishHeadings, getHeadings
**Dépendances** : mdast-util-from-markdown, mdast-util-to-string, unist-util-visit, unist, @/frame/lib/find-page, @/data-directory/lib/get-data, @/types

### `languages-server.ts`

Module TypeScript. Nombre de lignes: 79. Elements detectés: function getRoot

**Fonctions** : getRoot, pathLanguagePrefixed
**Dépendances** : path, fs, dotenv, @/frame/lib/constants, ./languages

### `languages.ts`

Module TypeScript. Nombre de lignes: 114.

**Dépendances** : ./languages-server.ts

### `render-with-fallback.ts`

Module TypeScript. Nombre de lignes: 182.

**Classes** : EmptyTitleError, for, LiquidError
**Fonctions** : createTranslationFallbackComment, renderContentWithFallback
**Dépendances** : @/content-render/index, @/frame/lib/page, @/content-render/unified/rewrite-local-links, @/types

### `translation-utils.ts`

Module TypeScript. Nombre de lignes: 159. Elements detectés: class UngettableError extends Error {}, function carefulGetWrapper

**Classes** : UngettableError
**Fonctions** : createTranslationFunctions, carefulGetWrapper, translate, getCommonFallback, carefulGet
**Dépendances** : @/frame/components/context/MainContext
