# Module : src/frame/components/page-header

6 fichier(s), 10 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : Breadcrumbs, BreadcrumbsScroller, DocsSecondaryBar, Header, HeaderNotifications, HeaderSearchAndWidgets, close, handleClick, onScroll, openOnSlash
- **Dépendances** : ../context/MainContext, ../hooks/useHasAccount, ./Breadcrumbs, ./BreadcrumbsScroller, ./BreadcrumbsScroller.module.scss, ./DocsSecondaryBar.module.scss, ./HeaderNotifications.module.scss, ./HeaderSearchAndWidgets, ./HeaderSearchAndWidgets.module.scss, @/frame/components/Link, @/frame/components/context/MainContext, @/frame/components/context/SharedUIContext

## Détail des fichiers

### `Breadcrumbs.tsx`

**Fonctions** : Breadcrumbs, handleClick
**Dépendances** : react, next/router, classnames, @primer/react-brand, ../context/MainContext, @/versions/components/useVersion, @/languages/components/useTranslation, @/frame/components/lib/prefetch

### `BreadcrumbsScroller.tsx`

**Fonctions** : BreadcrumbsScroller
**Dépendances** : react, classnames, @primer/react, @primer/octicons-react, @/languages/components/useTranslation, ./Breadcrumbs, ./BreadcrumbsScroller.module.scss

### `DocsSecondaryBar.tsx`

**Fonctions** : DocsSecondaryBar
**Dépendances** : classnames, next/router, @primer/react, @primer/octicons-react, @/frame/components/context/MainContext, @/languages/components/useTranslation, @/frame/components/sidebar/SidebarCollapseContext, ./BreadcrumbsScroller, ./DocsSecondaryBar.module.scss

### `Header.tsx`

**Fonctions** : Header, onScroll, close, openOnSlash
**Dépendances** : react, classnames, next/router, @primer/octicons-react, @/versions/components/useVersion, @/frame/components/Link, @/frame/components/context/MainContext, @/frame/components/page-header/HeaderNotifications, @/languages/components/useTranslation, @/versions/components/VersionPicker, @/search/components/input/SearchBarButton, ./HeaderSearchAndWidgets

### `HeaderNotifications.tsx`

**Fonctions** : HeaderNotifications
**Dépendances** : react, next/router, classnames, @primer/octicons-react, @/languages/components/LanguagesContext, @/frame/components/context/MainContext, @/languages/components/useTranslation, @/frame/components/lib/ExcludesNull, @/versions/components/useVersion, @/languages/components/useUserLanguage, ./HeaderNotifications.module.scss, @/frame/components/context/SharedUIContext

### `HeaderSearchAndWidgets.tsx`

**Fonctions** : HeaderSearchAndWidgets
**Dépendances** : classnames, react, @primer/octicons-react, @primer/react, @/languages/components/LanguagePicker, @/languages/components/useTranslation, @/versions/components/VersionPicker, @/versions/components/useVersion, ../hooks/useHasAccount, ./HeaderSearchAndWidgets.module.scss
