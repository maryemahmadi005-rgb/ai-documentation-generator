# Module : src/workflows/tests

7 fichier(s), 1 classe(s), 11 fonction(s).

## Vue d'ensemble

- **Classes principales** : fails
- **Fonctions principales** : actionsUsedInWorkflow, fakeResponse, jobIsPublicDocsScoped, jobRequiresFailureAlerts, makeError, makeFakeOctokit, makeOctokit, makePage, makePages, makeRollup, serves
- **Dépendances** : ../measure-instruction-budget, @/types, @/workflows/github, @octokit/request-error, @octokit/rest, flat, fs, js-yaml, lodash-es, node:module, path, url

## Détail des fichiers

### `actions-workflows.ts`

Module TypeScript. Nombre de lignes: 237. Elements detectés: function actionsUsedInWorkflow, function jobIsPublicDocsScoped, function jobRequiresFailureAlerts

**Fonctions** : actionsUsedInWorkflow, jobIsPublicDocsScoped, jobRequiresFailureAlerts
**Dépendances** : url, path, fs, vitest, js-yaml, flat, lodash-es

### `find-past-built-pr.ts`

Module TypeScript. Nombre de lignes: 137. Elements detectés: function makeFakeOctokit

**Fonctions** : makeFakeOctokit
**Dépendances** : vitest, @octokit/rest

### `generate-llms-txt.ts`

Module TypeScript. Nombre de lignes: 223. Elements detectés: function makePage, function makePages, function makeRollup

**Fonctions** : makePage, makePages, makeRollup
**Dépendances** : vitest, @/types

### `github.ts`

Module TypeScript. Nombre de lignes: 48. Elements detectés: function makeError

**Classes** : fails
**Fonctions** : makeError
**Dépendances** : node:module, vitest, @octokit/request-error, @/workflows/github

### `measure-instruction-budget.ts`

Module TypeScript. Nombre de lignes: 55.

**Dépendances** : vitest, ../measure-instruction-budget

### `purge-fastly-changed-content.ts`

Module TypeScript. Nombre de lignes: 268. Elements detectés: function makeOctokit, function makeOctokit

**Fonctions** : makeOctokit, fakeResponse
**Dépendances** : vitest, @octokit/rest

### `wait-for-build.ts`

Module TypeScript. Nombre de lignes: 69. Elements detectés: function serves

**Fonctions** : serves
**Dépendances** : vitest
