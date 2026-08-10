# Module : src/fixtures/tests

25 fichier(s), 6 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : equalStringArray, makeURL, maxScrollOf, processSpotlight, scrollLeftOf, srcsetOf
- **Dépendances** : ../../frame/lib/constants, ../helpers/turn-off-experiments, @/content-render/unified/rewrite-asset-img-tags, @/data-directory/lib/get-data, @/frame/lib/constants, @/tests/helpers/e2etest, @/versions/lib/all-versions, @/versions/lib/enterprise-server-releases, @/versions/lib/non-enterprise-default-version, @axe-core/playwright, @playwright/test, cheerio

## Détail des fichiers

### `annotations.ts`

Module TypeScript. Nombre de lignes: 49.

**Dépendances** : vitest, cheerio, @/tests/helpers/e2etest

### `api-article-body.ts`

Module TypeScript. Nombre de lignes: 163.

**Fonctions** : makeURL
**Dépendances** : vitest, @/tests/helpers/e2etest

### `bad-urls.ts`

Module TypeScript. Nombre de lignes: 14.

**Dépendances** : vitest, @/tests/helpers/e2etest

### `breadcrumbs.ts`

Module TypeScript. Nombre de lignes: 75.

**Dépendances** : vitest, domhandler, @/tests/helpers/e2etest

### `categories-and-subcategory.ts`

Module TypeScript. Nombre de lignes: 51.

**Dépendances** : vitest, cheerio, domhandler, @/tests/helpers/e2etest

### `footer.ts`

Module TypeScript. Nombre de lignes: 41.

**Dépendances** : vitest, cheerio, @/tests/helpers/e2etest, @/versions/lib/non-enterprise-default-version

### `glossary.ts`

Module TypeScript. Nombre de lignes: 51.

**Fonctions** : equalStringArray
**Dépendances** : vitest, cheerio, @/tests/helpers/e2etest

### `head.ts`

Module TypeScript. Nombre de lignes: 14.

**Dépendances** : vitest, cheerio, @/tests/helpers/e2etest

### `homepage.ts`

Module TypeScript. Nombre de lignes: 29.

**Dépendances** : vitest, cheerio, @/tests/helpers/e2etest

### `html-comments.ts`

Module TypeScript. Nombre de lignes: 15.

**Dépendances** : vitest, cheerio, @/tests/helpers/e2etest

### `images.ts`

Module TypeScript. Nombre de lignes: 73. Elements detectés: function srcsetOf

**Fonctions** : srcsetOf
**Dépendances** : vitest, sharp, cheerio, domhandler, @/tests/helpers/e2etest, @/content-render/unified/rewrite-asset-img-tags

### `internal-links.ts`

Module TypeScript. Nombre de lignes: 137.

**Dépendances** : vitest, cheerio, domhandler, @/tests/helpers/e2etest, @/versions/lib/enterprise-server-releases, @/versions/lib/all-versions

### `landing-hero.ts`

Module TypeScript. Nombre de lignes: 9.

**Dépendances** : vitest, cheerio, @/tests/helpers/e2etest

### `liquid.ts`

Module TypeScript. Nombre de lignes: 289.

**Dépendances** : vitest, cheerio, @/data-directory/lib/get-data, @/tests/helpers/e2etest, @/versions/lib/enterprise-server-releases

### `markdown.ts`

Module TypeScript. Nombre de lignes: 38.

**Dépendances** : vitest, cheerio, @/tests/helpers/e2etest

### `minitoc.ts`

Module TypeScript. Nombre de lignes: 32.

**Dépendances** : vitest, cheerio, @/tests/helpers/e2etest

### `page-titles.ts`

Module TypeScript. Nombre de lignes: 30.

**Dépendances** : vitest, cheerio, @/versions/lib/enterprise-server-releases, @/tests/helpers/e2etest

### `permissions-callout.ts`

Module TypeScript. Nombre de lignes: 45.

**Dépendances** : vitest, cheerio, @/tests/helpers/e2etest

### `playwright-a11y.spec.ts`

Module TypeScript. Nombre de lignes: 38.

**Dépendances** : @playwright/test, @axe-core/playwright, ../helpers/turn-off-experiments

### `playwright-rendering.spec.ts`

Module TypeScript. Nombre de lignes: 1415.

**Fonctions** : scrollLeftOf, maxScrollOf
**Dépendances** : dotenv, @playwright/test, ../helpers/turn-off-experiments, ../../frame/lib/constants

### `playwright-secret-scanning.spec.ts`

Module TypeScript. Nombre de lignes: 98.

**Dépendances** : @playwright/test

### `sidebar.ts`

Module TypeScript. Nombre de lignes: 101.

**Dépendances** : vitest, cheerio, @/tests/helpers/e2etest

### `spotlight-processing.ts`

Module TypeScript. Nombre de lignes: 162. Elements detectés: function processSpotlight

**Fonctions** : processSpotlight
**Dépendances** : vitest

### `translations.ts`

Module TypeScript. Nombre de lignes: 151.

**Dépendances** : vitest, cheerio, domhandler, @/frame/lib/constants, @/tests/helpers/e2etest

### `versioning.ts`

Module TypeScript. Nombre de lignes: 91.

**Dépendances** : vitest, cheerio, @/tests/helpers/e2etest, @/versions/lib/enterprise-server-releases
