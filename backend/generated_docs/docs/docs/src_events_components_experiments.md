# Module : src/events/components/experiments

7 fichier(s), 14 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : ExperimentContentSwap, ExperimentSwapper, checkStaff, getActiveExperiments, getExperimentControlGroupFromSession, getExperimentVariationForContext, handleClick, handleKeyDown, initializeExperiments, initializeForwardFeatureUrlParam, sendExperimentSuccess, shouldShowExperiment, updateShouldShow, useShouldShowExperiment
- **Dépendances** : ../dotcom-cookies, ../events, ./experiment, ./experiments, @/events/components/experiments/experiments, @/events/components/experiments/useShouldShowExperiment, @/events/types, @/frame/components/context/MainContext, imurmurhash, next/router, querystring, react

## Détail des fichiers

### `ExperimentContentSwap.tsx`

**Fonctions** : ExperimentContentSwap, ExperimentSwapper
**Dépendances** : react, @/events/components/experiments/useShouldShowExperiment, @/events/components/experiments/experiments

### `README.md`

### `content-ab-testing.md`

### `experiment-event.ts`

Module TypeScript. Nombre de lignes: 13.

**Fonctions** : sendExperimentSuccess
**Dépendances** : @/events/types, ../events, ./experiment, ./experiments

### `experiment.ts`

Module TypeScript. Nombre de lignes: 236.

**Fonctions** : shouldShowExperiment, getExperimentControlGroupFromSession, getExperimentVariationForContext, initializeExperiments, initializeForwardFeatureUrlParam, handleClick, handleKeyDown
**Dépendances** : imurmurhash, next/router, ../events, querystring

### `experiments.ts`

Module TypeScript. Nombre de lignes: 75.

**Fonctions** : getActiveExperiments

### `useShouldShowExperiment.ts`

Module TypeScript. Nombre de lignes: 67.

**Fonctions** : useShouldShowExperiment, checkStaff, updateShouldShow
**Dépendances** : react, next/router, ./experiment, ./experiments, ../dotcom-cookies, @/frame/components/context/MainContext
