# Module : src/languages/tests

9 fichier(s), 6 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : failingCallable, fallbackCallable, fix, fixAt, fixWithStrip, getReleaseNotesVersionCombinations
- **Dépendances** : @/content-render/unified/rewrite-local-links, @/frame/lib/constants, @/frame/lib/page, @/frame/middleware/block-robots, @/languages/lib/correct-translation-content, @/languages/lib/languages-server, @/languages/scripts/count-translation-corruptions, @/tests/helpers/conditional-runs, @/tests/helpers/e2etest, @/versions/lib/all-versions, domhandler, perf_hooks

## Détail des fichiers

### `api-search.ts`

Module TypeScript. Nombre de lignes: 36.

**Dépendances** : vitest, @/tests/helpers/conditional-runs, @/tests/helpers/e2etest

### `correct-translation-content.ts`

Module TypeScript. Nombre de lignes: 2141. Elements detectés: function fix

**Fonctions** : fix, fixAt, fixWithStrip
**Dépendances** : vitest, perf_hooks, @/languages/lib/correct-translation-content

### `count-translation-corruptions.ts`

Module TypeScript. Nombre de lignes: 31.

**Dépendances** : vitest, @/versions/lib/all-versions, @/languages/scripts/count-translation-corruptions

### `files.ts`

Module TypeScript. Nombre de lignes: 13.

**Dépendances** : @/languages/lib/languages-server, vitest

### `frame.ts`

Module TypeScript. Nombre de lignes: 107.

**Fonctions** : getReleaseNotesVersionCombinations
**Dépendances** : vitest, @/languages/lib/languages-server, @/frame/middleware/block-robots, domhandler, @/tests/helpers/e2etest, @/frame/lib/page

### `glossary.ts`

Module TypeScript. Nombre de lignes: 12.

**Dépendances** : vitest, @/languages/lib/languages-server, @/tests/helpers/e2etest

### `redirects.ts`

Module TypeScript. Nombre de lignes: 44.

**Dépendances** : vitest, @/languages/lib/languages-server, @/tests/helpers/e2etest, @/frame/lib/constants

### `search.ts`

Module TypeScript. Nombre de lignes: 12.

**Dépendances** : vitest, @/languages/lib/languages-server, @/tests/helpers/e2etest

### `translation-error-comments.ts`

Module TypeScript. Nombre de lignes: 342.

**Fonctions** : failingCallable, fallbackCallable
**Dépendances** : vitest, @/content-render/unified/rewrite-local-links, @/frame/lib/page
