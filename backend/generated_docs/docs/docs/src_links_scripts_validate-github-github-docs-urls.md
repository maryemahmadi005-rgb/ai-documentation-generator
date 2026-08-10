# Module : src/links/scripts/validate-github-github-docs-urls

5 fichier(s), 9 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : T, cleanUpOldBranches, contentFileMatchesURL, generateNewJSON, makeAbsoluteDocsURL, makeMarkdownTableFragments, postPRComment, updateIssueComment, validate
- **Dépendances** : ../../lib/validate-docs-urls, ./clean-up-old-branches, ./generate-new-json, ./post-pr-comment, ./validate, @/links/lib/validate-docs-urls, @/workflows/github, boxen, chalk, commander, fs

## Détail des fichiers

### `clean-up-old-branches.ts`

Module TypeScript. Nombre de lignes: 48.

**Fonctions** : cleanUpOldBranches
**Dépendances** : @/workflows/github

### `generate-new-json.ts`

Module TypeScript. Nombre de lignes: 45.

**Fonctions** : generateNewJSON
**Dépendances** : fs, chalk, ../../lib/validate-docs-urls

### `index.ts`

Module TypeScript. Nombre de lignes: 68.

**Dépendances** : commander, ./post-pr-comment, ./validate, ./generate-new-json, ./clean-up-old-branches

### `post-pr-comment.ts`

Module TypeScript. Nombre de lignes: 242.

**Fonctions** : postPRComment, contentFileMatchesURL, makeAbsoluteDocsURL, makeMarkdownTableFragments, updateIssueComment
**Dépendances** : fs, boxen, @/workflows/github, ../../lib/validate-docs-urls

### `validate.ts`

Module TypeScript. Nombre de lignes: 79.

**Fonctions** : validate, T
**Dépendances** : fs, chalk, @/links/lib/validate-docs-urls
