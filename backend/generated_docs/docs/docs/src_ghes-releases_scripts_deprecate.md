# Module : src/ghes-releases/scripts/deprecate

8 fichier(s), 1 classe(s), 13 fonction(s).

## Vue d'ensemble

- **Classes principales** : RewriteAssetPathsPlugin
- **Fonctions principales** : collapse, collapseBlankLines, createRedirectsFile, getChangedMarkdownFiles, getParentFilePath, main, removeFileUpdateParent, updateAutomatedConfigFiles, updateAutomatedPipelines, updateContentFiles, updateDataFiles, updateFeatureData, updateReusableData
- **Dépendances** : ../version-utils, @/frame/lib/app, @/frame/lib/page-data, @/frame/lib/read-frontmatter, @/ghes-releases/scripts/deprecate/collapse-blank-lines, @/ghes-releases/scripts/deprecate/rewrite-asset-paths, @/ghes-releases/scripts/deprecate/update-automated-pipelines, @/ghes-releases/scripts/deprecate/update-content, @/ghes-releases/scripts/deprecate/update-data, @/languages/lib/languages-server, @/redirects/lib/precompile, @/types

## Détail des fichiers

### `archive-version.ts`

Module TypeScript. Nombre de lignes: 149.

**Fonctions** : main, createRedirectsFile
**Dépendances** : path, fs, website-scraper, commander, rimraf, http, @/frame/lib/app, @/versions/lib/enterprise-server-releases, @/redirects/lib/precompile, @/frame/lib/page-data, @/languages/lib/languages-server, @/ghes-releases/scripts/deprecate/rewrite-asset-paths

### `collapse-blank-lines.ts`

Module TypeScript. Nombre de lignes: 77. Elements detectés: function getChangedMarkdownFiles, function collapse

**Fonctions** : getChangedMarkdownFiles, collapse, collapseBlankLines
**Dépendances** : fs, child_process

### `create-docs-ghes-version-repo.sh`

### `index.ts`

Module TypeScript. Nombre de lignes: 43.

**Dépendances** : commander, child_process, @/ghes-releases/scripts/deprecate/update-content, @/ghes-releases/scripts/deprecate/update-data, @/ghes-releases/scripts/deprecate/update-automated-pipelines, @/ghes-releases/scripts/deprecate/collapse-blank-lines

### `rewrite-asset-paths.ts`

Module TypeScript. Nombre de lignes: 74.

**Classes** : RewriteAssetPathsPlugin
**Dépendances** : fs, path

### `update-automated-pipelines.ts`

Module TypeScript. Nombre de lignes: 170.

**Fonctions** : updateAutomatedConfigFiles, updateAutomatedPipelines
**Dépendances** : fs, fs/promises, rimraf, lodash-es, mkdirp, @/versions/lib/enterprise-server-releases

### `update-content.ts`

Module TypeScript. Nombre de lignes: 158.

**Fonctions** : updateContentFiles, removeFileUpdateParent, getParentFilePath
**Dépendances** : fs, path, js-yaml, walk-sync, @/frame/lib/read-frontmatter, @/versions/lib/enterprise-server-releases, ../version-utils, @/types

### `update-data.ts`

Module TypeScript. Nombre de lignes: 94. Elements detectés: function updateReusableData, function updateFeatureData

**Fonctions** : updateDataFiles, updateReusableData, updateFeatureData
**Dépendances** : fs, lodash-es, walk-sync, js-yaml, ../version-utils, @/types
