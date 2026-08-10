# Module : src/frame/components/context

5 fichier(s), 5 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : SharedUIContextProvider, addUINamespaces, minimalAllVersions, pageInfo, parseSidebarExpandedCookie
- **Dépendances** : @/frame/components/article/SupportPortalVaIframe, @/frame/components/hooks/useFeatureFlags, @/frame/components/page-header/Breadcrumbs, @/frame/lib/constants, @/journeys/lib/journey-path-resolver, @/landings/lib/featured-links, @/landings/types, @/types, express, lodash/pick, react

## Détail des fichiers

### `ArticleContext.tsx`

**Dépendances** : @/frame/components/article/SupportPortalVaIframe, react, @/journeys/lib/journey-path-resolver

### `CategoryLandingContext.tsx`

**Dépendances** : react, @/landings/lib/featured-links, @/landings/types, @/types

### `MainContext.tsx`

**Fonctions** : minimalAllVersions, addUINamespaces, parseSidebarExpandedCookie, pageInfo
**Dépendances** : react, lodash/pick, express, @/frame/components/page-header/Breadcrumbs, @/frame/components/hooks/useFeatureFlags, @/types, @/frame/lib/constants

### `SharedUIContext.tsx`

**Fonctions** : SharedUIContextProvider
**Dépendances** : react

### `TocLandingContext.tsx`

**Dépendances** : react, @/landings/lib/featured-links, @/landings/types
