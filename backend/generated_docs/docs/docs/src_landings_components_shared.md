# Module : src/landings/components/shared

3 fichier(s), 15 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : ArticleCard, ArticleGrid, LandingCarousel, LandingHero, applyFilters, goToNext, goToPrevious, handleFilter, handlePageChange, handleSearch, heroBackgroundCss, updateArticlesPerPage, updateItemsPerView, useResponsiveArticlesPerPage, useResponsiveItemsPerView
- **Dépendances** : ./LandingCarousel.module.scss, ./LandingHero.module.scss, @/frame/components/Link, @/frame/components/ui/RenderedHTML/RenderedHTML, @/landings/context/LandingContext, @/landings/lib/article-search, @/landings/types, @/languages/components/useTranslation, @/search/components/hooks/useMultiQueryParams, @/types, @/versions/components/useVersion, @primer/live-region-element

## Détail des fichiers

### `LandingArticleGridWithFilter.tsx`

**Fonctions** : useResponsiveArticlesPerPage, updateArticlesPerPage, ArticleGrid, applyFilters, handleSearch, handleFilter, handlePageChange, ArticleCard
**Dépendances** : react, @primer/react, @primer/react-brand, @primer/octicons-react, @primer/live-region-element, classnames, @/frame/components/Link, @/languages/components/useTranslation, @/landings/types, @/landings/context/LandingContext, @/search/components/hooks/useMultiQueryParams, @/landings/lib/article-search

### `LandingCarousel.tsx`

**Fonctions** : useResponsiveItemsPerView, updateItemsPerView, LandingCarousel, goToPrevious, goToNext
**Dépendances** : react, next/router, @primer/octicons-react, classnames, @/types, @/languages/components/useTranslation, @/versions/components/useVersion, ./LandingCarousel.module.scss, @/frame/components/ui/RenderedHTML/RenderedHTML

### `LandingHero.tsx`

**Fonctions** : heroBackgroundCss, LandingHero
**Dépendances** : @primer/octicons-react, @primer/react-brand, ./LandingHero.module.scss, @/languages/components/useTranslation, @/frame/components/ui/RenderedHTML/RenderedHTML
