# Module : src/release-notes/middleware

2 fichier(s), 2 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : getReleaseNotes, ghesReleaseNotesContext
- **Dépendances** : ./get-release-notes, @/data-directory/lib/get-data, @/languages/lib/render-with-fallback, @/release-notes/lib/release-notes-utils, @/types, @/versions/lib/enterprise-server-releases, express

## Détail des fichiers

### `get-release-notes.ts`

Module TypeScript. Nombre de lignes: 60.

**Fonctions** : getReleaseNotes
**Dépendances** : @/data-directory/lib/get-data, @/types

### `ghes-release-notes.ts`

Module TypeScript. Nombre de lignes: 85.

**Fonctions** : ghesReleaseNotesContext
**Dépendances** : express, @/release-notes/lib/release-notes-utils, @/versions/lib/enterprise-server-releases, @/languages/lib/render-with-fallback, ./get-release-notes, @/types
