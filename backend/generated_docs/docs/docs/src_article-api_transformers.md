# Module : src/article-api/transformers

20 fichier(s), 20 classe(s), 8 fonction(s).

## Vue d'ensemble

- **Classes principales** : ArticleTransformer, AuditLogsTransformer, BespokeLandingTransformer, CategoryLandingTransformer, CodeQLCliTransformer, DiscoveryLandingTransformer, GithubAppsTransformer, GraphQLBreakingChangesTransformer, GraphQLChangelogTransformer, GraphQLIndexTransformer, GraphQLReferenceTransformer, JourneyLandingTransformer
- **Fonctions principales** : bool, bulletize, cleanSecretType, collectCategories, escape, processChanges, renderNoteMarkdown, renderReleaseNotesMarkdown
- **Dépendances** : ./audit-logs-transformer, ./codeql-cli-transformer, ./github-apps-transformer, ./graphql-breaking-changes-transformer, ./graphql-changelog-transformer, ./graphql-index-transformer, ./graphql-reference-transformer, ./rest-transformer, ./secret-scanning-transformer, ./toc-transformer, ./types, ./webhooks-transformer

## Détail des fichiers

### `article-transformer.ts`

Module TypeScript. Nombre de lignes: 23.

**Classes** : ArticleTransformer
**Dépendances** : @/types, ./types

### `audit-logs-transformer.ts`

Module TypeScript. Nombre de lignes: 150.

**Classes** : AuditLogsTransformer
**Dépendances** : @/types, ./types, @/audit-logs/types, @/audit-logs/lib/index, @/content-render/index, @/article-api/lib/load-template, @gr2m/gray-matter

### `bespoke-landing-transformer.ts`

Module TypeScript. Nombre de lignes: 103.

**Classes** : BespokeLandingTransformer
**Dépendances** : @/types, ./types, @/content-render/index, @/article-api/lib/load-template, @/article-api/lib/get-all-toc-items

### `category-landing-transformer.ts`

Module TypeScript. Nombre de lignes: 136.

**Classes** : CategoryLandingTransformer
**Dépendances** : @/types, ./types, @/content-render/index, @/article-api/lib/load-template, @/article-api/lib/resolve-path, @/article-api/lib/get-link-data

### `codeql-cli-transformer.ts`

Module TypeScript. Nombre de lignes: 41.

**Classes** : CodeQLCliTransformer
**Dépendances** : @/types, ./types, @/content-render/index, @/article-api/lib/load-template, @/article-api/lib/strip-html-comments

### `discovery-landing-transformer.ts`

Module TypeScript. Nombre de lignes: 166.

**Classes** : DiscoveryLandingTransformer
**Fonctions** : collectCategories
**Dépendances** : @/types, ./types, @/content-render/index, @/article-api/lib/load-template, @/article-api/lib/get-all-toc-items

### `github-apps-transformer.ts`

Module TypeScript. Nombre de lignes: 300.

**Classes** : GithubAppsTransformer
**Dépendances** : @/types, ./types, @/content-render/index, @/article-api/lib/load-template, @gr2m/gray-matter

### `graphql-breaking-changes-transformer.ts`

Module TypeScript. Nombre de lignes: 56.

**Classes** : GraphQLBreakingChangesTransformer
**Dépendances** : @/types, ./types, @/graphql/components/types, @/content-render/index, @/article-api/lib/load-template, @/content-render/unified/text-only, @/article-api/lib/graphql-helpers, github-slugger

### `graphql-changelog-transformer.ts`

Module TypeScript. Nombre de lignes: 76.

**Classes** : GraphQLChangelogTransformer
**Fonctions** : processChanges
**Dépendances** : @/types, ./types, @/graphql/components/types, @/content-render/index, @/article-api/lib/load-template, @/content-render/unified/text-only, @/article-api/lib/graphql-helpers

### `graphql-index-transformer.ts`

Module TypeScript. Nombre de lignes: 46.

**Classes** : GraphQLIndexTransformer
**Dépendances** : @/types, ./types, @/content-render/index, @/article-api/lib/load-template, @/article-api/lib/graphql-helpers

### `graphql-reference-transformer.ts`

Module TypeScript. Nombre de lignes: 319.

**Classes** : GraphQLReferenceTransformer
**Dépendances** : @/types, ./types, @/content-render/index, @/article-api/lib/load-template, @/content-render/unified/text-only, @/article-api/lib/graphql-helpers

### `index.ts`

Module TypeScript. Nombre de lignes: 45.

**Dépendances** : ./types, ./rest-transformer, ./secret-scanning-transformer, ./codeql-cli-transformer, ./audit-logs-transformer, ./graphql-index-transformer, ./graphql-reference-transformer, ./graphql-changelog-transformer, ./graphql-breaking-changes-transformer, ./github-apps-transformer, ./webhooks-transformer, ./toc-transformer

### `journey-landing-transformer.ts`

Module TypeScript. Nombre de lignes: 102.

**Classes** : JourneyLandingTransformer
**Dépendances** : @/types, ./types, @/content-render/index, @/article-api/lib/load-template, @/article-api/lib/resolve-path, @/article-api/lib/get-link-data

### `release-notes-transformer.ts`

Module TypeScript. Nombre de lignes: 111. Elements detectés: function bulletize

**Classes** : ReleaseNotesTransformer
**Fonctions** : renderNoteMarkdown, bulletize, renderReleaseNotesMarkdown
**Dépendances** : @/types, ./types, @/release-notes/middleware/get-release-notes, @/release-notes/lib/release-notes-utils, @/content-render/index

### `rest-transformer.ts`

Module TypeScript. Nombre de lignes: 245.

**Classes** : RestTransformer
**Dépendances** : @/types, ./types, @/rest/components/types, @/content-render/index, @/content-render/liquid/engine, @/article-api/liquid-renderers, @/article-api/lib/load-template, @/article-api/lib/summarize-schema, @gr2m/gray-matter, @/content-render/unified/text-only, github-slugger

### `search-page-transformer.ts`

Module TypeScript. Nombre de lignes: 23.

**Classes** : SearchPageTransformer
**Dépendances** : @/types, ./types

### `secret-scanning-transformer.ts`

Module TypeScript. Nombre de lignes: 127.

**Classes** : SecretScanningTransformer
**Fonctions** : bool, escape, cleanSecretType
**Dépendances** : @/types, ./types, js-yaml, path, @/content-render/index, @/versions/lib/all-versions, @/article-api/lib/load-template, @/secret-scanning/lib/get-secret-scanning-data

### `toc-transformer.ts`

Module TypeScript. Nombre de lignes: 69.

**Classes** : TocTransformer
**Dépendances** : @/types, ./types, @/content-render/index, @/article-api/lib/load-template, @/article-api/lib/resolve-path, @/article-api/lib/get-link-data

### `types.ts`

Module TypeScript. Nombre de lignes: 134.

**Classes** : is, TransformerRegistry
**Dépendances** : @/types

### `webhooks-transformer.ts`

Module TypeScript. Nombre de lignes: 97.

**Classes** : WebhooksTransformer
**Dépendances** : @/types, ./types, @/content-render/index, @/content-render/unified/text-only, @/article-api/lib/load-template, @gr2m/gray-matter
