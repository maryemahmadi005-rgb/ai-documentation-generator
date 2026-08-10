# Diagrammes du projet

## Architecture

```mermaid
graph TD
presentation["Presentation / Routes"]
business["Business / Service Layer"]
data["Data / Repository Layer"]
database[("Database")]
presentation --> business
business --> data
data --> database
```

## Flux de données

```mermaid
graph TD
gateway["API Gateway"]
svc_services["services"]
svc_use_containerized_services["use-containerized-services"]
database[("Database")]
gateway --> svc_services
svc_services --> svc_use_containerized_services
svc_use_containerized_services --> database
```

## Dépendances des modules

```mermaid
graph TD
info["Module dependency diagram unavailable"]
```

## Arborescence du projet

```mermaid
graph TD
ROOT["docs"]
ROOT_assets["assets/"]
ROOT --> ROOT_assets
ROOT_config["config/"]
ROOT --> ROOT_config
ROOT_config_kubernetes["kubernetes/"]
ROOT_config --> ROOT_config_kubernetes
ROOT_config_moda["moda/"]
ROOT_config --> ROOT_config_moda
ROOT_content["content/"]
ROOT --> ROOT_content
ROOT_content_account_and_profi["account-and-profile/"]
ROOT_content --> ROOT_content_account_and_profi
ROOT_content_actions["actions/"]
ROOT_content --> ROOT_content_actions
ROOT_content_admin["admin/"]
ROOT_content --> ROOT_content_admin
ROOT_content_apps["apps/"]
ROOT_content --> ROOT_content_apps
ROOT_content_authentication["authentication/"]
ROOT_content --> ROOT_content_authentication
ROOT_content_billing["billing/"]
ROOT_content --> ROOT_content_billing
ROOT_content_code_security["code-security/"]
ROOT_content --> ROOT_content_code_security
ROOT_content_codespaces["codespaces/"]
ROOT_content --> ROOT_content_codespaces
ROOT_content_communities["communities/"]
ROOT_content --> ROOT_content_communities
ROOT_content_contributing["contributing/"]
ROOT_content --> ROOT_content_contributing
ROOT_content_copilot["copilot/"]
ROOT_content --> ROOT_content_copilot
ROOT_content_desktop["desktop/"]
ROOT_content --> ROOT_content_desktop
ROOT_content_discussions["discussions/"]
ROOT_content --> ROOT_content_discussions
ROOT_content_education["education/"]
ROOT_content --> ROOT_content_education
ROOT_content_enterprise_onboar["enterprise-onboarding/"]
ROOT_content --> ROOT_content_enterprise_onboar
ROOT_content_get_started["get-started/"]
ROOT_content --> ROOT_content_get_started
ROOT_content_github_cli["github-cli/"]
ROOT_content --> ROOT_content_github_cli
ROOT_content_github_models["github-models/"]
ROOT_content --> ROOT_content_github_models
ROOT_content_graphql["graphql/"]
ROOT_content --> ROOT_content_graphql
ROOT_content_integrations["integrations/"]
ROOT_content --> ROOT_content_integrations
ROOT_content_issues["issues/"]
ROOT_content --> ROOT_content_issues
ROOT_content_migrations["migrations/"]
ROOT_content --> ROOT_content_migrations
ROOT_content_nonprofit["nonprofit/"]
ROOT_content --> ROOT_content_nonprofit
ROOT_content_organizations["organizations/"]
ROOT_content --> ROOT_content_organizations
ROOT_content_packages["packages/"]
ROOT_content --> ROOT_content_packages
ROOT_content_pages["pages/"]
ROOT_content --> ROOT_content_pages
ROOT_content_pull_requests["pull-requests/"]
ROOT_content --> ROOT_content_pull_requests
ROOT_content_repositories["repositories/"]
ROOT_content --> ROOT_content_repositories
ROOT_content_rest["rest/"]
ROOT_content --> ROOT_content_rest
ROOT_content_search["search/"]
ROOT_content --> ROOT_content_search
ROOT_content_search_github["search-github/"]
ROOT_content --> ROOT_content_search_github
ROOT_content_site_policy["site-policy/"]
ROOT_content --> ROOT_content_site_policy
ROOT_content_sponsors["sponsors/"]
ROOT_content --> ROOT_content_sponsors
ROOT_content_subscriptions_and["subscriptions-and-notifications/"]
ROOT_content --> ROOT_content_subscriptions_and
ROOT_content_support["support/"]
ROOT_content --> ROOT_content_support
ROOT_content_webhooks["webhooks/"]
ROOT_content --> ROOT_content_webhooks
ROOT_contributing["contributing/"]
ROOT --> ROOT_contributing
ROOT_data["data/"]
ROOT --> ROOT_data
ROOT_data_features["features/"]
ROOT_data --> ROOT_data_features
ROOT_data_glossaries["glossaries/"]
ROOT_data --> ROOT_data_glossaries
ROOT_data_graphql["graphql/"]
ROOT_data --> ROOT_data_graphql
ROOT_data_llms_txt["llms-txt/"]
ROOT_data --> ROOT_data_llms_txt
ROOT_data_release_notes["release-notes/"]
ROOT_data --> ROOT_data_release_notes
ROOT_data_reusables["reusables/"]
ROOT_data --> ROOT_data_reusables
ROOT_data_tables["tables/"]
ROOT_data --> ROOT_data_tables
ROOT_data_variables["variables/"]
ROOT_data --> ROOT_data_variables
ROOT_patches["patches/"]
ROOT --> ROOT_patches
ROOT_src["src/"]
ROOT --> ROOT_src
ROOT_src_ai_tools["ai-tools/"]
ROOT_src --> ROOT_src_ai_tools
ROOT_src_app["app/"]
ROOT_src --> ROOT_src_app
ROOT_src_archives["archives/"]
ROOT_src --> ROOT_src_archives
ROOT_src_article_api["article-api/"]
ROOT_src --> ROOT_src_article_api
ROOT_src_assets["assets/"]
ROOT_src --> ROOT_src_assets
ROOT_src_audit_logs["audit-logs/"]
ROOT_src --> ROOT_src_audit_logs
ROOT_src_automated_pipelines["automated-pipelines/"]
ROOT_src --> ROOT_src_automated_pipelines
ROOT_src_codeql_cli["codeql-cli/"]
ROOT_src --> ROOT_src_codeql_cli
ROOT_src_codeql_queries["codeql-queries/"]
ROOT_src --> ROOT_src_codeql_queries
ROOT_src_color_schemes["color-schemes/"]
ROOT_src --> ROOT_src_color_schemes
ROOT_src_content_linter["content-linter/"]
ROOT_src --> ROOT_src_content_linter
ROOT_src_content_pipelines["content-pipelines/"]
ROOT_src --> ROOT_src_content_pipelines
ROOT_src_content_render["content-render/"]
ROOT_src --> ROOT_src_content_render
ROOT_src_data_directory["data-directory/"]
ROOT_src --> ROOT_src_data_directory
ROOT_src_deployments["deployments/"]
ROOT_src --> ROOT_src_deployments
ROOT_src_dev_toc["dev-toc/"]
ROOT_src --> ROOT_src_dev_toc
ROOT_src_early_access["early-access/"]
ROOT_src --> ROOT_src_early_access
ROOT_src_eslint_rules["eslint-rules/"]
ROOT_src --> ROOT_src_eslint_rules
ROOT_src_events["events/"]
ROOT_src --> ROOT_src_events
ROOT_src_fixtures["fixtures/"]
ROOT_src --> ROOT_src_fixtures
ROOT_src_frame["frame/"]
ROOT_src --> ROOT_src_frame
ROOT_src_ghes_releases["ghes-releases/"]
ROOT_src --> ROOT_src_ghes_releases
ROOT_src_github_apps["github-apps/"]
ROOT_src --> ROOT_src_github_apps
ROOT_src_graphql["graphql/"]
ROOT_src --> ROOT_src_graphql
ROOT_src_journeys["journeys/"]
ROOT_src --> ROOT_src_journeys
ROOT_src_landings["landings/"]
ROOT_src --> ROOT_src_landings
ROOT_src_languages["languages/"]
ROOT_src --> ROOT_src_languages
ROOT_src_links["links/"]
ROOT_src --> ROOT_src_links
ROOT_src_metrics["metrics/"]
ROOT_src --> ROOT_src_metrics
ROOT_src_observability["observability/"]
ROOT_src --> ROOT_src_observability
ROOT_src_pages["pages/"]
ROOT_src --> ROOT_src_pages
ROOT_src_products["products/"]
ROOT_src --> ROOT_src_products
ROOT_src_redirects["redirects/"]
ROOT_src --> ROOT_src_redirects
ROOT_src_release_notes["release-notes/"]
ROOT_src --> ROOT_src_release_notes
ROOT_src_rest["rest/"]
ROOT_src --> ROOT_src_rest
ROOT_src_search["search/"]
ROOT_src --> ROOT_src_search
ROOT_src_secret_scanning["secret-scanning/"]
ROOT_src --> ROOT_src_secret_scanning
ROOT_src_shielding["shielding/"]
ROOT_src --> ROOT_src_shielding
ROOT_src_tests["tests/"]
ROOT_src --> ROOT_src_tests
ROOT_src_tools["tools/"]
ROOT_src --> ROOT_src_tools
ROOT_src_types["types/"]
ROOT_src --> ROOT_src_types
ROOT_src_versions["versions/"]
ROOT_src --> ROOT_src_versions
ROOT_src_webhooks["webhooks/"]
ROOT_src --> ROOT_src_webhooks
ROOT_src_workflows["workflows/"]
ROOT_src --> ROOT_src_workflows
```
