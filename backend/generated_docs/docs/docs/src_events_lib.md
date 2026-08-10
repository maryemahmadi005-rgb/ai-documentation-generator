# Module : src/events/lib

5 fichier(s), 19 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : _publish, analyzeComment, formatErrors, getCussWords, getDocumentType, getGuessedLanguage, getLanguageInstance, isAllUppercase, isContainingEmail, isEmailOnly, isLikelyCussWords, isMaybeCussWords, isMostlyEmoji, isNotLanguage, isNumbersOnly
- **Dépendances** : @/content-render/lib/code-languages, @/frame/lib/constants, @/frame/lib/fetch-utils, @/frame/lib/frontmatter, @/languages/lib/languages-server, @/observability/lib/failbot, @/observability/lib/statsd, @/observability/logger, @/products/lib/all-products, @/tools/lib/all-tools, @/versions/lib/all-versions, ajv

## Détail des fichiers

### `analyze-comment.ts`

Module TypeScript. Nombre de lignes: 214.

**Fonctions** : getLanguageInstance, getGuessedLanguage, analyzeComment, isEmailOnly, isContainingEmail, isURL, isNumbersOnly, isAllUppercase, isTooShort, isSingleWord, isNotLanguage, isMostlyEmoji, getCussWords, isLikelyCussWords, isMaybeCussWords
**Dépendances** : fs, js-yaml, cuss, cuss/pt, cuss/fr, cuss/es

### `get-document-type.ts`

Module TypeScript. Nombre de lignes: 31.

**Fonctions** : getDocumentType

### `hydro.ts`

Module TypeScript. Nombre de lignes: 89.

**Fonctions** : _publish
**Dépendances** : crypto, @/frame/lib/fetch-utils, lodash-es, @/observability/lib/statsd, @/observability/lib/failbot, @/frame/lib/constants, @/observability/logger

### `middleware-errors.ts`

Module TypeScript. Nombre de lignes: 35. Elements detectés: function makeString

**Fonctions** : formatErrors, makeString
**Dépendances** : lodash-es, crypto, ajv

### `schema.ts`

Module TypeScript. Nombre de lignes: 721.

**Dépendances** : @/languages/lib/languages-server, @/versions/lib/all-versions, @/products/lib/all-products, @/tools/lib/all-tools, @/content-render/lib/code-languages, @/frame/lib/frontmatter
