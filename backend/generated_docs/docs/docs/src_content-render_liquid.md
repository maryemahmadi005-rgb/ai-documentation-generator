# Module : src/content-render/liquid

12 fichier(s), 4 classe(s), 7 fonction(s).

## Vue d'ensemble

- **Classes principales** : DataReferenceError, Ifversion, IndentedDataReferenceError, supports
- **Fonctions principales** : cleanUpExtraEmptyLines, cleanUpListEmptyLines, handleBlockquote, handleIndent, parseBlockTemplates, processLiquidPost, renderLiquid
- **Dépendances** : ../lib/prompt-id, ./codetabs, ./data, ./engine, ./error-handling, ./ifversion, ./indented-data-reference, ./octicon, ./post, ./prompt, ./spotlight, ./tool

## Détail des fichiers

### `codetabs.ts`

Module TypeScript. Nombre de lignes: 106. Elements detectés: function parseBlockTemplates

**Fonctions** : parseBlockTemplates
**Dépendances** : html-entities, liquidjs, @/content-render/lib/code-languages

### `data.ts`

Module TypeScript. Nombre de lignes: 101. Elements detectés: function handleIndent, function handleBlockquote

**Fonctions** : handleIndent, handleBlockquote
**Dépendances** : liquidjs, ./error-handling, @/data-directory/lib/get-data, @/observability/logger

### `engine.ts`

Module TypeScript. Nombre de lignes: 59.

**Dépendances** : liquidjs, github-slugger, ./data, ./octicon, ./ifversion, ./tool, ./spotlight, ./prompt, ./codetabs, ./indented-data-reference

### `error-handling.ts`

Module TypeScript. Nombre de lignes: 9.

**Classes** : DataReferenceError, IndentedDataReferenceError

### `ifversion.ts`

Module TypeScript. Nombre de lignes: 194.

**Classes** : Ifversion
**Dépendances** : @/versions/lib/version-satisfies-range, @/observability/logger

### `indented-data-reference.ts`

Module TypeScript. Nombre de lignes: 59.

**Classes** : supports
**Dépendances** : assert, liquidjs, ./error-handling, @/data-directory/lib/get-data, @/observability/logger

### `index.ts`

Module TypeScript. Nombre de lignes: 10.

**Fonctions** : renderLiquid
**Dépendances** : ./post, ./engine, @/types

### `octicon.ts`

Module TypeScript. Nombre de lignes: 61.

**Dépendances** : liquidjs, @primer/octicons

### `post.ts`

Module TypeScript. Nombre de lignes: 27. Elements detectés: function cleanUpListEmptyLines, function cleanUpExtraEmptyLines

**Fonctions** : processLiquidPost, cleanUpListEmptyLines, cleanUpExtraEmptyLines

### `prompt.ts`

Module TypeScript. Nombre de lignes: 44.

**Dépendances** : @primer/octicons, liquidjs, ../lib/prompt-id

### `spotlight.ts`

Module TypeScript. Nombre de lignes: 54.

### `tool.ts`

Module TypeScript. Nombre de lignes: 71.

**Dépendances** : @/tools/lib/all-tools, @/tools/lib/all-platforms
