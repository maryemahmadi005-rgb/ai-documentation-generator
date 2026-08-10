# Module : src/graphql/components

17 fichier(s), 19 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : BreakingChanges, Changelog, Enum, GraphqlCategoryPage, GraphqlItem, GraphqlPage, InputObject, Interface, Mutation, Notice, Object, Previews, Query, Scalar, Table
- **Dépendances** : ./Enum, ./GraphqlItem, ./InputObject, ./Interface, ./Mutation, ./Notice, ./Object, ./Query, ./Scalar, ./Table, ./Union, ./types

## Détail des fichiers

### `BreakingChanges.tsx`

**Fonctions** : BreakingChanges
**Dépendances** : classnames, @/frame/components/article/HeadingLink, @/frame/components/ui/RenderedHTML/RenderedHTML, ./types, @/frame/components/ui/MarkdownContent/MarkdownContent.module.scss

### `Changelog.tsx`

**Fonctions** : YearNav, Changelog
**Dépendances** : react, classnames, github-slugger, @/frame/components/article/HeadingLink, @/frame/components/ui/RenderedHTML/RenderedHTML, ./types, @/frame/components/ui/MarkdownContent/MarkdownContent.module.scss

### `Enum.tsx`

**Fonctions** : Enum
**Dépendances** : @/languages/components/useTranslation, ./GraphqlItem, ./types, @/frame/components/ui/RenderedHTML/RenderedHTML

### `GraphqlCategoryPage.tsx`

**Fonctions** : GraphqlCategoryPage, renderItem
**Dépendances** : react, classnames, ./Enum, ./InputObject, ./Interface, ./Scalar, ./Mutation, ./Object, ./Query, ./Union, @/frame/components/article/HeadingLink, @/frame/components/ui/MarkdownContent/MarkdownContent.module.scss

### `GraphqlItem.tsx`

**Fonctions** : headingTag, GraphqlItem
**Dépendances** : react, @primer/react-brand, @/frame/components/article/HeadingLink, ./types, ./Notice, @/graphql/lib/categories, @/frame/components/ui/RenderedHTML/RenderedHTML

### `GraphqlPage.tsx`

**Fonctions** : GraphqlPage
**Dépendances** : react, classnames, ./Enum, ./InputObject, ./Interface, ./Scalar, ./Mutation, ./Object, ./Query, ./Union, @/frame/components/ui/MarkdownContent/MarkdownContent.module.scss

### `InputObject.tsx`

**Fonctions** : InputObject
**Dépendances** : ./GraphqlItem, ./Table, @/languages/components/useTranslation, ./types

### `Interface.tsx`

**Fonctions** : Interface
**Dépendances** : @/frame/components/Link, ./GraphqlItem, ./Table, @/languages/components/useTranslation, ./types, @/frame/components/ui/RenderedHTML/RenderedHTML

### `Mutation.tsx`

**Fonctions** : Mutation
**Dépendances** : @/frame/components/Link, ./GraphqlItem, ./Notice, @/languages/components/useTranslation, ./Table, ./types, @/frame/components/ui/RenderedHTML/RenderedHTML, react

### `Notice.tsx`

**Fonctions** : Notice
**Dépendances** : @/frame/components/Link, @/frame/components/ui/Alert, @/languages/components/useTranslation, ./types, @/frame/components/ui/RenderedHTML/RenderedHTML

### `Object.tsx`

**Fonctions** : Object
**Dépendances** : @/frame/components/Link, ./GraphqlItem, ./Table, @/languages/components/useTranslation, ./types, @/frame/components/ui/RenderedHTML/RenderedHTML

### `Previews.tsx`

**Fonctions** : Previews
**Dépendances** : github-slugger, classnames, @/frame/components/article/HeadingLink, @/languages/components/useTranslation, ./types, @/frame/components/ui/MarkdownContent/MarkdownContent.module.scss

### `Query.tsx`

**Fonctions** : Query
**Dépendances** : @/frame/components/Link, ./GraphqlItem, ./Table, @/languages/components/useTranslation, ./types, @/frame/components/ui/RenderedHTML/RenderedHTML

### `Scalar.tsx`

**Fonctions** : Scalar
**Dépendances** : ./GraphqlItem, ./types

### `Table.tsx`

**Fonctions** : Table
**Dépendances** : @/frame/components/Link, ./Notice, @/languages/components/useTranslation, ./types, @/frame/components/ui/RenderedHTML/RenderedHTML

### `Union.tsx`

**Fonctions** : Union
**Dépendances** : @/frame/components/Link, ./GraphqlItem, @/languages/components/useTranslation, ./types

### `types.tsx`
