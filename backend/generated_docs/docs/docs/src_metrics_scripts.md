# Module : src/metrics/scripts

2 fichier(s), 7 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : getCleanPath, getPathToQuery, getVersion, main, removeVersionSegment, validatePath
- **Dépendances** : @/frame/lib/read-frontmatter, @/metrics/lib/dates, @/metrics/lib/kusto-client, @/metrics/queries/bounces, @/metrics/queries/users, @/metrics/queries/view-duration, @/metrics/queries/views, @/workflows/walk-files, chalk, commander, fs, ora

## Détail des fichiers

### `docsaudit.ts`

Module TypeScript. Nombre de lignes: 77. Elements detectés: function getPathToQuery

**Fonctions** : main, getPathToQuery
**Dépendances** : fs, path, url, commander, @/workflows/walk-files, @/frame/lib/read-frontmatter, @/metrics/lib/kusto-client, @/metrics/lib/dates, @/metrics/queries/views, @/metrics/queries/users

### `docstat.ts`

Module TypeScript. Nombre de lignes: 484.

**Fonctions** : main, getCleanPath, getVersion, removeVersionSegment, validatePath
**Dépendances** : fs, path, commander, chalk, ora, @/frame/lib/read-frontmatter, @/metrics/lib/kusto-client, @/metrics/lib/dates, @/metrics/queries/views, @/metrics/queries/users, @/metrics/queries/view-duration, @/metrics/queries/bounces
