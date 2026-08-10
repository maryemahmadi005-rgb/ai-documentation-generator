# Module : src/content-render/tests

16 fichier(s), 11 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : contextualize, getChangedContentFiles, getContentFiles, getDeletedContentFiles, getRenamedOldContentFiles, logPersonAge, logPersonsAge, nl, runScript, table, test
- **Dépendances** : @/content-render/index, @/content-render/lib/prompt-id, @/content-render/unified/index, @/content-render/unified/rewrite-local-links, @/content-render/unified/text-only, @/frame/lib/get-mini-toc-items, @/frame/lib/page, @/frame/lib/page-data, @/languages/lib/languages-server, @/tests/helpers/data-directory, @/tests/helpers/e2etest, @/types

## Détail des fichiers

### `annotate.ts`

Module TypeScript. Nombre de lignes: 142.

**Dépendances** : vitest, cheerio, @/content-render/index, @/types

### `collect-mini-toc.ts`

Module TypeScript. Nombre de lignes: 63.

**Dépendances** : vitest, @/content-render/index, @/frame/lib/get-mini-toc-items, @/types

### `copilot-code-blocks.ts`

Module TypeScript. Nombre de lignes: 172. Elements detectés: function logPersonsAge, function logPersonsAge

**Fonctions** : logPersonsAge, test
**Dépendances** : vitest, @/content-render/index

### `data.ts`

Module TypeScript. Nombre de lignes: 59.

**Dépendances** : vitest, @/frame/lib/page, @/languages/lib/languages-server, @/versions/lib/non-enterprise-default-version, @/tests/helpers/data-directory

### `link-error-line-numbers.ts`

Module TypeScript. Nombre de lignes: 131.

**Dépendances** : vitest, @/content-render/index, @/content-render/unified/rewrite-local-links, @/types

### `liquid-helpers.ts`

Module TypeScript. Nombre de lignes: 56.

**Dépendances** : vitest, @/content-render/index, @/languages/lib/languages-server, @/tests/helpers/data-directory, @/types

### `liquid-tags.ts`

Module TypeScript. Nombre de lignes: 77.

**Fonctions** : runScript
**Dépendances** : vitest, fs/promises, path, child_process

### `liquid.ts`

Module TypeScript. Nombre de lignes: 168.

**Fonctions** : contextualize
**Dépendances** : vitest, express, @/content-render/index, @/versions/middleware/short-versions, @/versions/middleware/features, @/versions/lib/all-versions, @/versions/lib/enterprise-server-releases, @/types

### `octicon.ts`

Module TypeScript. Nombre de lignes: 64.

**Dépendances** : vitest, @/content-render/index

### `prompt-id.ts`

Module TypeScript. Nombre de lignes: 85.

**Fonctions** : logPersonAge
**Dépendances** : vitest, @/content-render/lib/prompt-id

### `prompt.ts`

Module TypeScript. Nombre de lignes: 18.

**Dépendances** : vitest, @/content-render/index

### `render-changed-and-deleted-files.ts`

Module TypeScript. Nombre de lignes: 148. Elements detectés: function getChangedContentFiles, function getDeletedContentFiles, function getRenamedOldContentFiles

**Fonctions** : getChangedContentFiles, getDeletedContentFiles, getRenamedOldContentFiles, getContentFiles
**Dépendances** : path, vitest, @/tests/helpers/e2etest, @/frame/lib/page-data

### `render-content.ts`

Module TypeScript. Nombre de lignes: 270.

**Fonctions** : table
**Dépendances** : cheerio, vitest, @/content-render/index, os

### `render-to-hast.ts`

Module TypeScript. Nombre de lignes: 104.

**Dépendances** : vitest, @/content-render/index, @/content-render/unified/index, @/types

### `table-accessibility-labels.ts`

Module TypeScript. Nombre de lignes: 163.

**Fonctions** : nl
**Dépendances** : cheerio, vitest, @/content-render/index, os

### `text-only.ts`

Module TypeScript. Nombre de lignes: 29.

**Dépendances** : vitest, @/content-render/unified/text-only
