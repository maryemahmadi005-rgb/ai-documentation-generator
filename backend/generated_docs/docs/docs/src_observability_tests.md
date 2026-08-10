# Module : src/observability/tests

8 fichier(s), 2 classe(s), 9 fonction(s).

## Vue d'ensemble

- **Classes principales** : CustomClass, instances
- **Fonctions principales** : createError, endOverride, expectDevLog, mockNext, runMiddlewareAndCapture, shouldLogException, stripAnsi
- **Dépendances** : ../lib/failbot, @/observability/lib/statsd, @/observability/lib/to-error, @/observability/logger, @/observability/logger/lib/logger-context, @/observability/logger/lib/to-logfmt, @/observability/logger/middleware/get-automatic-request-logger, express, nock, vitest

## Détail des fichiers

### `failbot.ts`

Module TypeScript. Nombre de lignes: 55.

**Dépendances** : vitest, nock, ../lib/failbot

### `get-automatic-request-logger.ts`

Module TypeScript. Nombre de lignes: 362. Elements detectés: function endOverride

**Fonctions** : endOverride, runMiddlewareAndCapture
**Dépendances** : vitest, @/observability/logger/middleware/get-automatic-request-logger, express

### `handle-errors.ts`

Module TypeScript. Nombre de lignes: 49. Elements detectés: function shouldLogException, function createError

**Fonctions** : shouldLogException, createError
**Dépendances** : vitest

### `logger-integration.ts`

Module TypeScript. Nombre de lignes: 214. Elements detectés: function stripAnsi, function expectDevLog

**Fonctions** : stripAnsi, expectDevLog, mockNext
**Dépendances** : vitest, express, @/observability/logger, @/observability/logger/lib/logger-context

### `logger.ts`

Module TypeScript. Nombre de lignes: 465. Elements detectés: function stripAnsi, function expectDevLog

**Classes** : instances, CustomClass
**Fonctions** : stripAnsi, expectDevLog
**Dépendances** : vitest, @/observability/logger

### `runtime-metrics.ts`

Module TypeScript. Nombre de lignes: 87.

**Dépendances** : vitest, @/observability/lib/statsd

### `to-error.ts`

Module TypeScript. Nombre de lignes: 51.

**Dépendances** : vitest, @/observability/lib/to-error

### `to-logfmt.test.ts`

Module TypeScript. Nombre de lignes: 197.

**Dépendances** : vitest, @/observability/logger/lib/to-logfmt
