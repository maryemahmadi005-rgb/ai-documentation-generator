# Module : src/audit-logs/scripts

2 fichier(s), 5 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : filter, filterAndUpdateGhes, loadAuditLogDataFromDisk, main
- **Dépendances** : ../lib/deduplicate, ../lib/index, ../types, @/frame/lib/page-data, @/redirects/lib/precompile, @/versions/lib/enterprise-server-releases, @/workflows/git-utils, fs, fs/promises, mkdirp, path

## Détail des fichiers

### `rebuild-dedup.ts`

Module TypeScript. Nombre de lignes: 51. Elements detectés: function loadAuditLogDataFromDisk

**Fonctions** : loadAuditLogDataFromDisk, main
**Dépendances** : fs, path, ../lib/deduplicate, ../types

### `sync.ts`

Module TypeScript. Nombre de lignes: 193.

**Fonctions** : main, filter, filterAndUpdateGhes
**Dépendances** : fs, fs/promises, mkdirp, path, ../lib/index, ../lib/deduplicate, @/workflows/git-utils, @/versions/lib/enterprise-server-releases, @/frame/lib/page-data, @/redirects/lib/precompile, ../types
