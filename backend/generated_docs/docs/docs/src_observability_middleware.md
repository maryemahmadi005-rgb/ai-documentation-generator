# Module : src/observability/middleware

4 fichier(s), 6 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : emit, expressMetrics, handleError, logException, shouldLogException, triggerError
- **Dépendances** : ../lib/failbot, @/frame/lib/constants, @/frame/middleware/cache-control, @/frame/middleware/next, @/observability/lib/statsd, @/observability/lib/to-error, @/observability/logger, @/types, express

## Détail des fichiers

### `catch-middleware-error.ts`

Module TypeScript. Nombre de lignes: 18.

**Dépendances** : express

### `express-metrics.ts`

Module TypeScript. Nombre de lignes: 25.

**Fonctions** : expressMetrics, emit
**Dépendances** : express, @/observability/lib/statsd

### `handle-errors.ts`

Module TypeScript. Nombre de lignes: 122. Elements detectés: function shouldLogException

**Fonctions** : shouldLogException, logException, handleError
**Dépendances** : express, ../lib/failbot, @/frame/middleware/next, @/frame/lib/constants, @/frame/middleware/cache-control, @/observability/lib/to-error, @/types, @/observability/logger

### `trigger-error.ts`

Module TypeScript. Nombre de lignes: 17.

**Fonctions** : triggerError
**Dépendances** : express, @/types
