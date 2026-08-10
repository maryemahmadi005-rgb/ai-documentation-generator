# Module : src/webhooks/scripts

3 fichier(s), 1 classe(s), 3 fonction(s).

## Vue d'ensemble

- **Classes principales** : Webhook
- **Fonctions principales** : formatWebhookData, processWebhookSchema, syncWebhookData
- **Dépendances** : ../../rest/scripts/utils/get-body-params, ../../rest/scripts/utils/normalize-docs-urls, ../lib/index, ./webhook-schema, @/content-render/index, @/tests/lib/validate-json-schema, @/webhooks/scripts/webhook, fs, fs/promises, lodash-es, mkdirp, path

## Détail des fichiers

### `sync.ts`

Module TypeScript. Nombre de lignes: 133.

**Fonctions** : syncWebhookData, processWebhookSchema, formatWebhookData
**Dépendances** : fs/promises, fs, path, mkdirp, ../lib/index, @/webhooks/scripts/webhook

### `webhook-schema.ts`

Module TypeScript. Nombre de lignes: 32.

### `webhook.ts`

Module TypeScript. Nombre de lignes: 98.

**Classes** : Webhook
**Dépendances** : lodash-es, @/tests/lib/validate-json-schema, @/content-render/index, ../../rest/scripts/utils/normalize-docs-urls, ./webhook-schema, ../../rest/scripts/utils/get-body-params
