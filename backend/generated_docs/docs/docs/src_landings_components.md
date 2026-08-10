# Module : src/landings/components

12 fichier(s), 36 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : ArticleList, CategoryLanding, CookBookArticleCard, CookBookFilter, ExpandableItem, HomePageHero, LeafLink, NavListItem, ProductSelectionCard, ProductSelections, RestNavListItem, SidebarExpandStateProvider, SidebarProduct, TableOfContents, TocLanding
- **Dépendances** : ../lib/octicons, ./ArticleList.module.scss, ./CookBookArticleCard, ./CookBookArticleCard.module.scss, ./CookBookFilter, ./CookBookFilter.module.scss, ./HomePageHero.module.scss, ./ProductSelectionCard, ./ProductSelectionCard.module.scss, ./SidebarProduct.module.scss, ./sidebar-navlist-depth, ./useSidebarExpandState

## Détail des fichiers

### `ArticleList.tsx`

**Fonctions** : ArticleList
**Dépendances** : @/frame/components/Link, @/landings/types, @/languages/components/useTranslation, @primer/octicons-react, @primer/react, clsx, dayjs, ./ArticleList.module.scss

### `CategoryLanding.tsx`

**Fonctions** : CategoryLanding, applyFilters, handleSearch, handleFilter, handleResetFilter, findArticleData
**Dépendances** : react, next/router, ./CookBookArticleCard, ./CookBookFilter, @/languages/components/useTranslation, @/frame/components/DefaultLayout, @/frame/components/article/ArticleTitle, @/frame/components/ui/Lead, @/frame/components/context/CategoryLandingContext, @/rest/components/ClientSideRedirects, @/rest/components/RestRedirect, @/landings/types

### `CookBookArticleCard.tsx`

**Fonctions** : setImage, CookBookArticleCard
**Dépendances** : @primer/react-brand, @primer/react, ../lib/octicons, ./CookBookArticleCard.module.scss

### `CookBookFilter.tsx`

**Fonctions** : CookBookFilter, onFilter, onResetFilter
**Dépendances** : @primer/react, @primer/react-brand, @primer/octicons-react, react, @/landings/types, @/languages/components/useTranslation, ./CookBookFilter.module.scss

### `HomePageHero.tsx`

**Fonctions** : HomePageHero
**Dépendances** : @primer/react-brand, @/languages/components/useTranslation, ./HomePageHero.module.scss, classnames

### `ProductSelectionCard.tsx`

**Fonctions** : ProductSelectionCard, icon
**Dépendances** : @/landings/components/ProductSelections, react, @/frame/components/Link, ./ProductSelectionCard.module.scss

### `ProductSelections.tsx`

**Fonctions** : ProductSelections
**Dépendances** : @/frame/components/context/MainContext, ./ProductSelectionCard

### `SidebarProduct.tsx`

**Fonctions** : handleNavClick, useSidebarNav, leafLinkProps, useRestNav, prefetchHandlers, SidebarProduct, clearPending, productSection, restSection, ExpandableItem, navListLevelSentinel, LeafLink, NavListItem, RestNavListItem
**Dépendances** : next/router, @primer/react-brand, @/frame/components/context/MainContext, @/automated-pipelines/components/AutomatedPageContext, @/rest/lib/config, @/frame/components/lib/prefetch, ./useSidebarExpandState, ./sidebar-navlist-depth, ./SidebarProduct.module.scss

### `TableOfContents.tsx`

**Fonctions** : TableOfContents
**Dépendances** : @/frame/components/Link, @/landings/types, @/frame/components/ui/RenderedHTML/RenderedHTML

### `TocLanding.tsx`

**Fonctions** : TocLanding
**Dépendances** : next/router, @/frame/components/context/TocLandingContext, @/languages/components/useTranslation, @/frame/components/DefaultLayout, @/landings/components/TableOfContents, @/frame/components/article/ArticleTitle, @/frame/components/ui/MarkdownContent, @/landings/components/ArticleList, @/frame/components/article/ArticleGridLayout, @/frame/components/ui/PermissionsStatement, @/frame/components/ui/Lead, @/rest/components/ClientSideRedirects

### `sidebar-navlist-depth.ts`

Module TypeScript. Nombre de lignes: 26.

### `useSidebarExpandState.tsx`

**Fonctions** : readStore, persistStore, SidebarExpandStateProvider, useSidebarExpandState
**Dépendances** : react, @/frame/components/lib/cookies, @/frame/lib/constants
