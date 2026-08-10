# Module : src/frame/components

10 fichier(s), 22 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : ClientSideHashFocus, ClientSideLanguageRedirect, ClientSideRefresh, CodeTabsGroup, CodeTabsProvider, CopyButton, DefaultLayout, GenericError, HighlightedCode, LayoutBody, Link, SimpleFooter, SimpleHeader, UtmPreserver, buildApiArticleUrl
- **Dépendances** : ./GenericError.module.scss, @/events/components/events, @/events/types, @/frame/components/lib/cookies, @/frame/components/page-footer/LegalFooter, @/frame/components/page-footer/SupportSection, @/frame/components/page-header/DocsSecondaryBar, @/frame/components/page-header/Header, @/frame/components/sidebar/SidebarNav, @/frame/components/ui/Lead, @/frame/components/ui/ScrollButton, @/frame/lib/constants

## Détail des fichiers

### `ClientSideHashFocus.tsx`

**Fonctions** : ClientSideHashFocus, handleHashChange
**Dépendances** : react

### `ClientSideLanguageRedirect.ts`

Module TypeScript. Nombre de lignes: 18.

**Fonctions** : ClientSideLanguageRedirect
**Dépendances** : react, next/router, @/languages/components/LanguagesContext, @/frame/components/lib/cookies, @/frame/lib/constants

### `ClientSideRefresh.tsx`

**Fonctions** : ClientSideRefresh
**Dépendances** : next/router, swr

### `CodeTabsGroup.tsx`

**Fonctions** : CodeTabsProvider, hasClass, getActiveKey, CodeTabsGroup
**Dépendances** : next/router, @primer/react, classnames, @/frame/components/lib/cookies, @/frame/lib/constants, @/events/components/events, @/events/types, @/languages/components/useTranslation

### `CopyButton.tsx`

**Fonctions** : CopyButton
**Dépendances** : react, @primer/live-region-element

### `DefaultLayout.tsx`

**Fonctions** : DefaultLayout, getCategoryImageUrl, getSocialCardImage, buildApiArticleUrl, LayoutBody
**Dépendances** : react, next/head, next/router, classnames, @/frame/components/sidebar/SidebarNav, @/frame/components/page-header/Header, @/frame/components/page-header/DocsSecondaryBar, @/frame/components/page-footer/LegalFooter, @/frame/components/ui/ScrollButton, @/frame/components/page-footer/SupportSection, @/versions/components/DeprecationBanner, @/rest/components/RestBanner

### `GenericError.tsx`

**Fonctions** : GenericError, SimpleHeader, SimpleFooter
**Dépendances** : next/head, next/link, next/router, @primer/octicons-react, @/frame/components/ui/Lead, ./GenericError.module.scss

### `HighlightedCode.tsx`

**Fonctions** : highlightToReact, HighlightedCode
**Dépendances** : react, react/jsx-runtime, hast-util-to-jsx-runtime, lowlight, highlight.js/lib/languages/json, highlight.js/lib/languages/javascript, highlightjs-curl, classnames

### `Link.tsx`

**Fonctions** : Link
**Dépendances** : next/router, next/link, react, @/versions/components/useVersion

### `UtmPreserver.tsx`

**Fonctions** : UtmPreserver, handleRouteChange
**Dépendances** : react, next/router
