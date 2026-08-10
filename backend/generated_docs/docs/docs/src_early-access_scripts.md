# Module : src/early-access/scripts

5 fichier(s), 5 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : main, moveImage, moveReusable, moveVariable, sleep
- **Dépendances** : @/frame/lib/patterns, @/frame/lib/read-frontmatter, @/redirects/scripts/helpers/add-redirect-to-frontmatter, @/workflows/walk-files, @actions/core, @actions/github, child_process, commander, fs, js-yaml, lodash-es, path

## Détail des fichiers

### `merge-early-access.sh`

### `migrate-early-access-product.ts`

Module TypeScript. Nombre de lignes: 244.

**Fonctions** : moveVariable, moveReusable, moveImage
**Dépendances** : fs, path, js-yaml, lodash-es, commander, child_process, @/frame/lib/read-frontmatter, @/frame/lib/patterns, @/redirects/scripts/helpers/add-redirect-to-frontmatter, @/workflows/walk-files

### `symlink-from-local-repo.ts`

Module TypeScript. Nombre de lignes: 96.

**Dépendances** : rimraf, fs, path, commander

### `update-data-and-image-paths.ts`

Module TypeScript. Nombre de lignes: 114.

**Dépendances** : fs, path, commander, @/workflows/walk-files, lodash-es, @/frame/lib/patterns

### `what-docs-early-access-branch.ts`

Module TypeScript. Nombre de lignes: 48.

**Fonctions** : sleep, main
**Dépendances** : @actions/github, @actions/core
