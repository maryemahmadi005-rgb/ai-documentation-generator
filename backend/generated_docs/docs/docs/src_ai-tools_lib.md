# Module : src/ai-tools/lib

5 fichier(s), 13 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : callEditor, callModelsApi, cleanAIResponse, convertSpaceToPrompt, enrichIndexContext, ensureGitHubToken, fetchCopilotSpace, findMarkdownFiles, getAvailableEditorTypes, getPromptsDir, getRefinementDescriptions, mergeFrontmatterProperties, parseSpaceUrl
- **Dépendances** : @/ai-tools/lib/call-models-api, @/frame/lib/fetch-utils, @/frame/lib/frontmatter, @/frame/lib/read-frontmatter, child_process, fs, js-yaml, path, url

## Détail des fichiers

### `auth-utils.ts`

Module TypeScript. Nombre de lignes: 22.

**Fonctions** : ensureGitHubToken
**Dépendances** : child_process

### `call-models-api.ts`

Module TypeScript. Nombre de lignes: 124.

**Fonctions** : callModelsApi, cleanAIResponse

### `file-utils.ts`

Module TypeScript. Nombre de lignes: 152.

**Fonctions** : findMarkdownFiles, mergeFrontmatterProperties
**Dépendances** : fs, path, js-yaml, @/frame/lib/read-frontmatter, @/frame/lib/frontmatter

### `prompt-utils.ts`

Module TypeScript. Nombre de lignes: 151.

**Fonctions** : getPromptsDir, getAvailableEditorTypes, getRefinementDescriptions, enrichIndexContext, callEditor
**Dépendances** : url, fs, js-yaml, path, @/frame/lib/read-frontmatter, @/ai-tools/lib/call-models-api

### `spaces-utils.ts`

Module TypeScript. Nombre de lignes: 110.

**Fonctions** : parseSpaceUrl, fetchCopilotSpace, convertSpaceToPrompt
**Dépendances** : @/frame/lib/fetch-utils
