# Module : src/graphql/pages

5 fichier(s), 6 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : GraphqlBreakingChanges, GraphqlChangelog, GraphqlChangelogYear, GraphqlPreviews, GraphqlReferencePage, stripParagraphWrappers
- **Dépendances** : @/automated-pipelines/components/AutomatedPage, @/frame/components/context/MainContext, @/graphql/components/BreakingChanges, @/graphql/components/Changelog, @/graphql/components/GraphqlCategoryPage, @/graphql/components/Previews, @/graphql/components/types, @/graphql/pages/changelog, @/types, @/types/types, express, github-slugger

## Détail des fichiers

### `breaking-changes.tsx`

**Fonctions** : GraphqlBreakingChanges
**Dépendances** : next, express, github-slugger, @/types, http, @/frame/components/context/MainContext, @/automated-pipelines/components/AutomatedPage, @/graphql/components/BreakingChanges, @/graphql/components/types

### `changelog-year.tsx`

**Fonctions** : GraphqlChangelogYear
**Dépendances** : next, express, @/types, http, @/frame/components/context/MainContext, @/automated-pipelines/components/AutomatedPage, @/graphql/components/Changelog, @/graphql/components/types, @/graphql/pages/changelog

### `changelog.tsx`

**Fonctions** : GraphqlChangelog, stripParagraphWrappers
**Dépendances** : next, express, @/types, http, @/frame/components/context/MainContext, @/automated-pipelines/components/AutomatedPage, @/graphql/components/Changelog, @/graphql/components/types

### `reference.tsx`

**Fonctions** : GraphqlReferencePage
**Dépendances** : next, express, @/graphql/components/GraphqlCategoryPage, @/graphql/components/types, @/types/types, @/automated-pipelines/components/AutomatedPage

### `schema-previews.tsx`

**Fonctions** : GraphqlPreviews
**Dépendances** : next, express, @/types, http, @/automated-pipelines/components/AutomatedPage, @/graphql/components/Previews, @/graphql/components/types
