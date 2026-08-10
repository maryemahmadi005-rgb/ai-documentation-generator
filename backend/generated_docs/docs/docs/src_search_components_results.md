# Module : src/search/components/results

6 fichier(s), 13 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : NoQuery, NoSearchResults, ResultsPagination, Search, SearchResultHit, SearchResultHits, SearchResults, SearchResultsAggregations, SidebarSearchAggregates, ValidationErrors, hrefBuilder, makeClearHref, makeHref
- **Dépendances** : ../../types, ../context/SearchContext, ./Aggregations, ./Aggregations.module.scss, ./NoQuery.module.scss, ./SearchResults.module.scss, ./ValidationErrors.module.scss, @/events/components/events, @/events/types, @/frame/components/Link, @/frame/components/context/MainContext, @/languages/components/useTranslation

## Détail des fichiers

### `Aggregations.tsx`

**Fonctions** : SearchResultsAggregations, makeHref, makeClearHref
**Dépendances** : @primer/react, next/router, next/link, @/languages/components/useTranslation, @/search/types, ./Aggregations.module.scss

### `NoQuery.tsx`

**Fonctions** : NoQuery
**Dépendances** : @primer/react, @/frame/components/context/MainContext, @/languages/components/useTranslation, ./NoQuery.module.scss

### `SearchResults.tsx`

**Fonctions** : SearchResults, SearchResultHits, NoSearchResults, SearchResultHit, ResultsPagination, hrefBuilder
**Dépendances** : @primer/react-brand, @primer/octicons-react, next/router, react, classnames, @/languages/components/useTranslation, @/frame/components/Link, @/events/components/events, @/events/types, ./SearchResults.module.scss, @/search/components/types, @/search/types

### `SidebarSearchAggregates.tsx`

**Fonctions** : SidebarSearchAggregates
**Dépendances** : ../context/SearchContext, ./Aggregations

### `ValidationErrors.tsx`

**Fonctions** : ValidationErrors
**Dépendances** : @primer/react, @/languages/components/useTranslation, ../../types, ./ValidationErrors.module.scss

### `index.tsx`

**Fonctions** : Search
**Dépendances** : next/head, @primer/react, @/languages/components/useTranslation, @/versions/components/useVersion, @/search/components/hooks/useNumberFormatter, @/search/components/results/SearchResults, @/search/components/results/NoQuery, @/frame/components/context/MainContext, @/search/components/results/ValidationErrors, @/search/components/context/SearchContext, @elastic/elasticsearch
