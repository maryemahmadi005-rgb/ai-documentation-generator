# Module : src/versions/lib

6 fichier(s), 12 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : evaluateVersions, findReleaseNumberIndex, getApplicableVersions, getDocsVersion, getNextReleaseNumber, getOpenApiVersion, getPreviousReleaseNumber, isApiVersioned, isValidNext, processDateForDisplay, removeFPTFromPath, versionSatisfiesRange
- **Dépendances** : ./all-versions, ./enterprise-server-releases, ./non-enterprise-default-version, ./version-satisfies-range, @/data-directory/lib/get-data, @/types, fs, lodash-es, semver, slash

## Détail des fichiers

### `all-versions.ts`

Module TypeScript. Nombre de lignes: 140.

**Fonctions** : isApiVersioned, getDocsVersion, getOpenApiVersion
**Dépendances** : fs, @/types, ./enterprise-server-releases

### `enterprise-server-releases.d.ts`

Module TypeScript. Nombre de lignes: 84.

**Fonctions** : findReleaseNumberIndex, getNextReleaseNumber, getPreviousReleaseNumber

### `enterprise-server-releases.ts`

Module TypeScript. Nombre de lignes: 205.

**Fonctions** : processDateForDisplay, isValidNext
**Dépendances** : fs, semver, ./version-satisfies-range

### `get-applicable-versions.ts`

Module TypeScript. Nombre de lignes: 136. Elements detectés: function getApplicableVersions, function evaluateVersions

**Fonctions** : getApplicableVersions, evaluateVersions
**Dépendances** : lodash-es, ./all-versions, ./version-satisfies-range, ./enterprise-server-releases, @/data-directory/lib/get-data, @/types

### `remove-fpt-from-path.ts`

Module TypeScript. Nombre de lignes: 8.

**Fonctions** : removeFPTFromPath
**Dépendances** : slash, ./non-enterprise-default-version

### `version-satisfies-range.ts`

Module TypeScript. Nombre de lignes: 24.

**Fonctions** : versionSatisfiesRange
**Dépendances** : semver
