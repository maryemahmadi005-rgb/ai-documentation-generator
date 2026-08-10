# Module : src/github-apps/scripts

3 fichier(s), 15 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : addAppData, calculateAdditionalPermissions, getDisplayPermissions, getDisplayTitle, getEntryIndex, getProgAccessData, getProgActorContentFromDisk, getProgActorResourceContent, isActorExcluded, sentenceCase, shouldFilterMetadataPermission, sortObjectByTitle, syncGitHubAppsData, validateAppData, writeDeduplicatedAppsFormat
- **Dépendances** : ./enabled-list-schema, ./permission-list-schema, @/tests/lib/validate-json-schema, @/workflows/git-utils, fs, fs/promises, github-slugger, js-yaml, mkdirp, path, walk-sync

## Détail des fichiers

### `enabled-list-schema.ts`

Module TypeScript. Nombre de lignes: 41.

### `permission-list-schema.ts`

Module TypeScript. Nombre de lignes: 64.

### `sync.ts`

Module TypeScript. Nombre de lignes: 626.

**Fonctions** : syncGitHubAppsData, writeDeduplicatedAppsFormat, getEntryIndex, getProgAccessData, getDisplayPermissions, sortObjectByTitle, getDisplayTitle, sentenceCase, calculateAdditionalPermissions, shouldFilterMetadataPermission, isActorExcluded, addAppData, validateAppData, getProgActorResourceContent, getProgActorContentFromDisk
**Dépendances** : fs, mkdirp, fs/promises, path, github-slugger, js-yaml, walk-sync, @/workflows/git-utils, ./permission-list-schema, ./enabled-list-schema, @/tests/lib/validate-json-schema
