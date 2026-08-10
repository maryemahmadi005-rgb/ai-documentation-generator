# Module : src/audit-logs/lib

3 fichier(s), 16 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : categorizeEvents, computeReferenceLinksToMarkdown, filterAndUpdateGhesDataByAllowlistValues, filterByAllowlistValues, getAuditLogEvents, getCategorizedAuditLogEvents, getCategoryNotes, getEntryIndex, getFieldsIndex, isFileNotFoundError, loadSharedFormat, processAndGetEventDescription, reconstructEventsFromSharedFormat, resolveReferenceLinksToMarkdown, resolveReferenceLinksToTitles
- **Dépendances** : ./config.json, @/frame/lib/find-page, @/frame/lib/read-json-file, @/types, @/versions/lib/all-versions, @/versions/lib/enterprise-server-releases, fs, fs/promises, mkdirp, path

## Détail des fichiers

### `config.json`

Fichier JSON. Nombre de lignes: 13.

### `deduplicate.ts`

Module TypeScript. Nombre de lignes: 83. Elements detectés: function getFieldsIndex, function getEntryIndex

**Fonctions** : writeDeduplicatedAuditLogData, getFieldsIndex, getEntryIndex
**Dépendances** : fs, fs/promises, mkdirp, path

### `index.ts`

Module TypeScript. Nombre de lignes: 488. Elements detectés: function isFileNotFoundError, function loadSharedFormat, function reconstructEventsFromSharedFormat

**Fonctions** : isFileNotFoundError, loadSharedFormat, reconstructEventsFromSharedFormat, getCategoryNotes, resolveReferenceLinksToMarkdown, computeReferenceLinksToMarkdown, resolveReferenceLinksToTitles, getAuditLogEvents, getCategorizedAuditLogEvents, filterByAllowlistValues, filterAndUpdateGhesDataByAllowlistValues, categorizeEvents, processAndGetEventDescription
**Dépendances** : path, @/frame/lib/read-json-file, @/versions/lib/all-versions, @/versions/lib/enterprise-server-releases, @/frame/lib/find-page, @/types, ./config.json
