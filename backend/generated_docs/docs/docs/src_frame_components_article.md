# Module : src/frame/components/article

7 fichier(s), 8 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : ArticleGridLayout, ArticleInlineLayout, ArticlePage, ArticleTitle, CopyMarkdownMenu, HeadingLink, SupportPortalVaIframe, eventHandler
- **Dépendances** : ./ArticleGridLayout, ./ArticleGridLayout.module.scss, ./ArticleInlineLayout, ./ArticleInlineLayout.module.scss, ./SupportPortalVaIframe, ./SupportPortalVaIframe.module.scss, ./ViewMarkdownButton.module.scss, @/events/components/event-groups, @/events/components/events, @/events/types, @/frame/components/DefaultLayout, @/frame/components/article/ArticleTitle

## Détail des fichiers

### `ArticleGridLayout.tsx`

**Fonctions** : ArticleGridLayout
**Dépendances** : react, classnames, ./SupportPortalVaIframe, ./ArticleGridLayout.module.scss

### `ArticleInlineLayout.tsx`

**Fonctions** : ArticleInlineLayout
**Dépendances** : react, classnames, ./SupportPortalVaIframe, ./ArticleInlineLayout.module.scss

### `ArticlePage.tsx`

**Fonctions** : ArticlePage
**Dépendances** : next/router, next/dynamic, @/frame/components/context/ArticleContext, @/frame/components/DefaultLayout, @/frame/components/article/ArticleTitle, @/frame/components/ui/MarkdownContent, @/frame/components/ui/Lead, @/frame/components/ui/PermissionsStatement, ./ArticleGridLayout, ./ArticleInlineLayout, @/tools/components/PlatformPicker, @/tools/components/ToolPicker

### `ArticleTitle.tsx`

**Fonctions** : ArticleTitle
**Dépendances** : react

### `HeadingLink.tsx`

**Fonctions** : HeadingLink
**Dépendances** : github-slugger, react

### `SupportPortalVaIframe.tsx`

**Fonctions** : SupportPortalVaIframe, eventHandler
**Dépendances** : next/router, react, ./SupportPortalVaIframe.module.scss

### `ViewMarkdownButton.tsx`

**Fonctions** : CopyMarkdownMenu
**Dépendances** : react, @primer/react, @primer/react-brand, @primer/live-region-element, @/events/components/event-groups, @/events/components/events, @/events/types, @/languages/components/useTranslation, classnames, ./ViewMarkdownButton.module.scss
