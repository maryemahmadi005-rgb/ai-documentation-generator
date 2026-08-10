# Module : src/github-apps/pages

5 fichier(s), 5 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : FineGrainedPatPermissions, FineGrainedTokenEndpoints, GitHubAppEndpoints, GitHubAppPermissions, UserGitHubAppEndpoints
- **Dépendances** : @/frame/components/context/MainContext, @/github-apps/components/EnabledList, @/github-apps/components/PermissionsList, @/types, express, next

## Détail des fichiers

### `endpoints-available-for-fine-grained-personal-access-tokens.tsx`

**Fonctions** : FineGrainedTokenEndpoints
**Dépendances** : next, express, @/types, @/frame/components/context/MainContext, @/github-apps/components/EnabledList

### `endpoints-available-for-github-app-installation-access-tokens.tsx`

**Fonctions** : GitHubAppEndpoints
**Dépendances** : next, express, @/types, @/frame/components/context/MainContext, @/github-apps/components/EnabledList

### `endpoints-available-for-github-app-user-access-tokens.tsx`

**Fonctions** : UserGitHubAppEndpoints
**Dépendances** : next, express, @/types, @/frame/components/context/MainContext, @/github-apps/components/EnabledList

### `permissions-required-for-fine-grained-personal-access-tokens.tsx`

**Fonctions** : FineGrainedPatPermissions
**Dépendances** : next, express, @/types, @/frame/components/context/MainContext, @/github-apps/components/PermissionsList

### `permissions-required-for-github-apps.tsx`

**Fonctions** : GitHubAppPermissions
**Dépendances** : next, express, @/types, @/frame/components/context/MainContext, @/github-apps/components/PermissionsList
