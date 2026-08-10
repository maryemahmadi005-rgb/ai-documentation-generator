# Module : src/rest/scripts

4 fichier(s), 15 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : check, createCheckContentDirectory, createCheckObj, createOpenAPISchemasCheck, difference, getAutomatedMarkdownFiles, getBundledFiles, getBundlerOptions, getDiffOpenAPIContentRest, getDifferences, getOnlyApiVersions, isApiVersioned, main, normalizeDataVersionNames, validateInputParameters
- **Dépendances** : ../lib/config, ../lib/index, ./utils/get-openapi-schemas, ./utils/get-operations, ./utils/sync, @/frame/lib/read-frontmatter, @/versions/lib/all-versions, @/versions/lib/enterprise-server-releases, @/versions/lib/get-applicable-versions, @/workflows/walk-files, child_process, commander

## Détail des fichiers

### `README.md`

### `openapi-check.ts`

Module TypeScript. Nombre de lignes: 50.

**Fonctions** : check
**Dépendances** : fs, path, glob, commander, ./utils/get-operations

### `test-open-api-schema.ts`

Module TypeScript. Nombre de lignes: 145. Elements detectés: function isApiVersioned, function getOnlyApiVersions

**Fonctions** : getDiffOpenAPIContentRest, createOpenAPISchemasCheck, createCheckContentDirectory, isApiVersioned, getOnlyApiVersions, createCheckObj, getDifferences, difference, getAutomatedMarkdownFiles
**Dépendances** : fs, path, lodash, @/frame/lib/read-frontmatter, @/versions/lib/get-applicable-versions, @/versions/lib/all-versions, ../lib/index, ../lib/config, @/versions/lib/enterprise-server-releases, @/workflows/walk-files

### `update-files.ts`

Module TypeScript. Nombre de lignes: 253.

**Fonctions** : main, getBundledFiles, getBundlerOptions, validateInputParameters, normalizeDataVersionNames
**Dépendances** : fs/promises, path, commander, child_process, rimraf, mkdirp, url, walk-sync, fs, ./utils/sync, ./utils/get-openapi-schemas, @/versions/lib/all-versions
