# Module : src/versions/middleware

3 fichier(s), 6 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : detectVersion, features, getFeaturesByVersion, getUserVersionFromCookie, isValidVersion, shortVersions
- **Dépendances** : @/data-directory/lib/get-data, @/frame/lib/constants, @/observability/logger/lib/logger-context, @/types, @/versions/lib/all-versions, @/versions/lib/get-applicable-versions, express, path

## Détail des fichiers

### `detect-version.ts`

Module TypeScript. Nombre de lignes: 22. Elements detectés: function isValidVersion

**Fonctions** : isValidVersion, getUserVersionFromCookie, detectVersion
**Dépendances** : express, @/frame/lib/constants, @/versions/lib/all-versions, @/observability/logger/lib/logger-context, @/types

### `features.ts`

Module TypeScript. Nombre de lignes: 49.

**Fonctions** : features, getFeaturesByVersion
**Dépendances** : path, express, @/types, @/frame/lib/constants, @/versions/lib/get-applicable-versions, @/data-directory/lib/get-data

### `short-versions.ts`

Module TypeScript. Nombre de lignes: 29.

**Fonctions** : shortVersions
**Dépendances** : @/types, express
