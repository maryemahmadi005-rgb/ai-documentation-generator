# Module : src/observability/lib

7 fichier(s), 7 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : _resetForTesting, isErrorWithCode, isMetricsEnabled, report, retryingFetch, startRuntimeMetrics, toError
- **Dépendances** : ./failbot, ./lib/failbot, ./statsd, @/frame/lib/fetch-utils, @/observability/lib/to-error, @/observability/logger, @/observability/logger/lib/logger-context, @github/failbot, @opentelemetry/exporter-trace-otlp-proto, @opentelemetry/instrumentation-express, @opentelemetry/instrumentation-http, @opentelemetry/instrumentation-undici

## Détail des fichiers

### `failbot.ts`

Module TypeScript. Nombre de lignes: 58.

**Fonctions** : retryingFetch, report
**Dépendances** : @/frame/lib/fetch-utils, @github/failbot, @/observability/logger/lib/logger-context, ./lib/failbot

### `handle-exceptions.ts`

Module TypeScript. Nombre de lignes: 30.

**Dépendances** : ./failbot, @/observability/lib/to-error, @/observability/logger

### `handle-package-not-found.ts`

Module TypeScript. Nombre de lignes: 42. Elements detectés: function isErrorWithCode

**Fonctions** : isErrorWithCode

### `runtime-metrics.ts`

Module TypeScript. Nombre de lignes: 65. Elements detectés: function isMetricsEnabled

**Fonctions** : isMetricsEnabled, startRuntimeMetrics, _resetForTesting
**Dépendances** : node:v8, node:perf_hooks, ./statsd

### `statsd.ts`

Module TypeScript. Nombre de lignes: 41.

**Dépendances** : hot-shots

### `to-error.ts`

Module TypeScript. Nombre de lignes: 10.

**Fonctions** : toError

### `tracing.ts`

Module TypeScript. Nombre de lignes: 62.

**Dépendances** : @opentelemetry/exporter-trace-otlp-proto, @opentelemetry/instrumentation-express, @opentelemetry/instrumentation-http, @opentelemetry/instrumentation-undici, @opentelemetry/sdk-node, @/observability/logger, @/observability/lib/to-error
