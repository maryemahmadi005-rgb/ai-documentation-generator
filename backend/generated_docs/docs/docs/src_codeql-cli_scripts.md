# Module : src/codeql-cli/scripts

2 fichier(s), 5 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : convertContentToDocs, getRedirect, main, rstToMarkdown, setupEnvironment
- **Dépendances** : ../../automated-pipelines/lib/update-markdown, ../../content-linter/lib/helpers/unified-formatter-options, ./convert-markdown-for-docs, @/languages/lib/languages-server, @gr2m/gray-matter, child_process, fs, fs/promises, mdast-util-from-markdown, mdast-util-to-markdown, mkdirp, path

## Détail des fichiers

### `convert-markdown-for-docs.ts`

Module TypeScript. Nombre de lignes: 293.

**Fonctions** : convertContentToDocs, getRedirect
**Dépendances** : fs/promises, path, mdast-util-from-markdown, mdast-util-to-markdown, unist-util-visit-parents, unist-util-visit, unist-util-remove, @/languages/lib/languages-server, ../../content-linter/lib/helpers/unified-formatter-options

### `sync.ts`

Module TypeScript. Nombre de lignes: 97.

**Fonctions** : main, setupEnvironment, rstToMarkdown
**Dépendances** : fs/promises, fs, walk-sync, mkdirp, child_process, path, @gr2m/gray-matter, rimraf, ../../automated-pipelines/lib/update-markdown, ./convert-markdown-for-docs
