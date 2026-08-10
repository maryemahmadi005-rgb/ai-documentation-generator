# Module : src/data-directory/scripts

2 fichier(s), 4 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : getOrphanedTables, getTableFiles, main
- **Dépendances** : @/languages/lib/languages-server, @/workflows/walk-files, @actions/core, @actions/github, commander, fs, path, url, walk-sync

## Détail des fichiers

### `deleted-features-pr-comment.ts`

Module TypeScript. Nombre de lignes: 80.

**Fonctions** : main
**Dépendances** : @actions/github, @actions/core, commander

### `find-orphaned-tables.ts`

Module TypeScript. Nombre de lignes: 179. Elements detectés: function getTableFiles

**Fonctions** : getTableFiles, getOrphanedTables, main
**Dépendances** : fs, path, url, commander, walk-sync, @/workflows/walk-files, @/languages/lib/languages-server
