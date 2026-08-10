# Module : src/graphql/scripts

3 fichier(s), 17 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : cleanMessagesFromChanges, cleanPreviewTitle, createChangelogEntry, ensureYearPage, formatTime, getBranchAsRef, getDataFilepath, getIgnoredChangesSummary, getLastIgnoredChanges, getRemoteRawContent, getVersionName, main, prependDatedEntry, previewAnchor, segmentPreviewChanges
- **Dépendances** : ./utils/bucket-by-category, ./utils/process-previews, ./utils/process-schemas, ./utils/process-upcoming-changes, @/content-render/index, @/versions/lib/all-versions, @/workflows/git-utils, @graphql-inspector/core, @graphql-tools/load, child_process, fs, fs/promises

## Détail des fichiers

### `README.md`

### `build-changelog.ts`

Module TypeScript. Nombre de lignes: 365.

**Fonctions** : prependDatedEntry, ensureYearPage, createChangelogEntry, cleanPreviewTitle, previewAnchor, cleanMessagesFromChanges, segmentPreviewChanges, getLastIgnoredChanges, getIgnoredChangesSummary
**Dépendances** : @graphql-inspector/core, @graphql-tools/load, fs, path, @/content-render/index

### `sync.ts`

Module TypeScript. Nombre de lignes: 277.

**Fonctions** : main, getRemoteRawContent, getDataFilepath, getBranchAsRef, getVersionName, updateFile, updateStaticFile, formatTime
**Dépendances** : fs/promises, fs, path, mkdirp, js-yaml, child_process, @/workflows/git-utils, @/versions/lib/all-versions, ./utils/process-previews, ./utils/process-upcoming-changes, ./utils/process-schemas, ./utils/bucket-by-category
