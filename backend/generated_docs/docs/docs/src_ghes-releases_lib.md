# Module : src/ghes-releases/lib

4 fichier(s), 11 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : appendNoteLines, buildReleaseIssueListArgs, buildReleaseNotesYaml, extractSkipReason, extractYaml, flushNote, isExcludedReleaseIssue, loadExistingEntries, loadExistingEntriesFromString, parseIssueState, parseNoteEntries
- **Dépendances** : fs, js-yaml

## Détail des fichiers

### `deprecation-steps.md`

### `enterprise-dates.json`

Fichier JSON. Nombre de lignes: 314.

### `parse-release-notes.ts`

Module TypeScript. Nombre de lignes: 309.

**Fonctions** : extractYaml, extractSkipReason, parseNoteEntries, loadExistingEntries, loadExistingEntriesFromString, flushNote, appendNoteLines, buildReleaseNotesYaml
**Dépendances** : fs, js-yaml

### `release-issues.ts`

Module TypeScript. Nombre de lignes: 45.

**Fonctions** : parseIssueState, buildReleaseIssueListArgs, isExcludedReleaseIssue
