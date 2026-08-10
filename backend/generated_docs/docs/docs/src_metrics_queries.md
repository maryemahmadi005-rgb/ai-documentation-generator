# Module : src/metrics/queries

7 fichier(s), 12 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : getBounces, getBouncesQuery, getExitsQueryStatement, getExitsToSupport, getScore, getScoreQuery, getUsers, getUsersQuery, getViewDuration, getViewDurationQuery, getViews, getViewsQuery
- **Dépendances** : @/metrics/lib/dates, @/metrics/lib/kusto-client, @/metrics/queries/constants, azure-kusto-data

## Détail des fichiers

### `bounces.ts`

Module TypeScript. Nombre de lignes: 45.

**Fonctions** : getBounces, getBouncesQuery
**Dépendances** : @/metrics/lib/kusto-client, @/metrics/queries/constants, @/metrics/lib/dates, azure-kusto-data

### `constants.ts`

Module TypeScript. Nombre de lignes: 28.

**Dépendances** : @/metrics/lib/dates

### `exits-to-support.ts`

Module TypeScript. Nombre de lignes: 44.

**Fonctions** : getExitsToSupport, getExitsQueryStatement
**Dépendances** : @/metrics/lib/kusto-client, @/metrics/queries/constants, @/metrics/lib/dates, azure-kusto-data

### `survey-score.ts`

Module TypeScript. Nombre de lignes: 48.

**Fonctions** : getScore, getScoreQuery
**Dépendances** : @/metrics/lib/kusto-client, @/metrics/queries/constants, @/metrics/lib/dates, azure-kusto-data

### `users.ts`

Module TypeScript. Nombre de lignes: 38.

**Fonctions** : getUsers, getUsersQuery
**Dépendances** : @/metrics/lib/kusto-client, @/metrics/queries/constants, @/metrics/lib/dates, azure-kusto-data

### `view-duration.ts`

Module TypeScript. Nombre de lignes: 43.

**Fonctions** : getViewDuration, getViewDurationQuery
**Dépendances** : @/metrics/lib/kusto-client, @/metrics/queries/constants, @/metrics/lib/dates, azure-kusto-data

### `views.ts`

Module TypeScript. Nombre de lignes: 38.

**Fonctions** : getViews, getViewsQuery
**Dépendances** : @/metrics/lib/kusto-client, @/metrics/queries/constants, @/metrics/lib/dates, azure-kusto-data
