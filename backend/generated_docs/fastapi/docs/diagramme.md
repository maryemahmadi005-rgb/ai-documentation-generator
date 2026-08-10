# Diagrammes du projet

## Architecture

```mermaid
graph TD
presentation["Presentation / Routes"]
database[("Database")]
presentation --> database
```

## Flux de données

```mermaid
graph TD
gateway["API Gateway"]
svc_app_a_py310["app_a_py310"]
svc_app_an_py310["app_an_py310"]
svc_app_b_an_py310["app_b_an_py310"]
svc_app_b_py310["app_b_py310"]
svc_app_testing["app_testing"]
database[("Database")]
gateway --> svc_app_a_py310
svc_app_a_py310 --> svc_app_an_py310
svc_app_an_py310 --> svc_app_b_an_py310
svc_app_b_an_py310 --> svc_app_b_py310
svc_app_b_py310 --> svc_app_testing
svc_app_testing --> database
```

## Dépendances des modules

```mermaid
graph TD
info["Module dependency diagram unavailable"]
```

## Arborescence du projet

```mermaid
graph TD
ROOT["fastapi"]
ROOT_docs["docs/"]
ROOT --> ROOT_docs
ROOT_docs_de["de/"]
ROOT_docs --> ROOT_docs_de
ROOT_docs_en["en/"]
ROOT_docs --> ROOT_docs_en
ROOT_docs_hi["hi/"]
ROOT_docs --> ROOT_docs_hi
ROOT_docs_ja["ja/"]
ROOT_docs --> ROOT_docs_ja
ROOT_docs_ko["ko/"]
ROOT_docs --> ROOT_docs_ko
ROOT_docs_pt["pt/"]
ROOT_docs --> ROOT_docs_pt
ROOT_docs_ru["ru/"]
ROOT_docs --> ROOT_docs_ru
ROOT_docs_tr["tr/"]
ROOT_docs --> ROOT_docs_tr
ROOT_docs_uk["uk/"]
ROOT_docs --> ROOT_docs_uk
ROOT_docs_zh_hant["zh-hant/"]
ROOT_docs --> ROOT_docs_zh_hant
ROOT_docs_src["docs_src/"]
ROOT --> ROOT_docs_src
ROOT_docs_src_additional_respo["additional_responses/"]
ROOT_docs_src --> ROOT_docs_src_additional_respo
ROOT_docs_src_additional_statu["additional_status_codes/"]
ROOT_docs_src --> ROOT_docs_src_additional_statu
ROOT_docs_src_advanced_middlew["advanced_middleware/"]
ROOT_docs_src --> ROOT_docs_src_advanced_middlew
ROOT_docs_src_app_testing["app_testing/"]
ROOT_docs_src --> ROOT_docs_src_app_testing
ROOT_docs_src_async_tests["async_tests/"]
ROOT_docs_src --> ROOT_docs_src_async_tests
ROOT_docs_src_authentication_e["authentication_error_status_code/"]
ROOT_docs_src --> ROOT_docs_src_authentication_e
ROOT_docs_src_background_tasks["background_tasks/"]
ROOT_docs_src --> ROOT_docs_src_background_tasks
ROOT_docs_src_behind_a_proxy["behind_a_proxy/"]
ROOT_docs_src --> ROOT_docs_src_behind_a_proxy
ROOT_docs_src_bigger_applicati["bigger_applications/"]
ROOT_docs_src --> ROOT_docs_src_bigger_applicati
ROOT_docs_src_body["body/"]
ROOT_docs_src --> ROOT_docs_src_body
ROOT_docs_src_body_fields["body_fields/"]
ROOT_docs_src --> ROOT_docs_src_body_fields
ROOT_docs_src_body_multiple_pa["body_multiple_params/"]
ROOT_docs_src --> ROOT_docs_src_body_multiple_pa
ROOT_docs_src_body_nested_mode["body_nested_models/"]
ROOT_docs_src --> ROOT_docs_src_body_nested_mode
ROOT_docs_src_body_updates["body_updates/"]
ROOT_docs_src --> ROOT_docs_src_body_updates
ROOT_docs_src_conditional_open["conditional_openapi/"]
ROOT_docs_src --> ROOT_docs_src_conditional_open
ROOT_docs_src_configure_swagge["configure_swagger_ui/"]
ROOT_docs_src --> ROOT_docs_src_configure_swagge
ROOT_docs_src_cookie_params["cookie_params/"]
ROOT_docs_src --> ROOT_docs_src_cookie_params
ROOT_docs_src_cookie_param_mod["cookie_param_models/"]
ROOT_docs_src --> ROOT_docs_src_cookie_param_mod
ROOT_docs_src_cors["cors/"]
ROOT_docs_src --> ROOT_docs_src_cors
ROOT_docs_src_custom_docs_ui["custom_docs_ui/"]
ROOT_docs_src --> ROOT_docs_src_custom_docs_ui
ROOT_docs_src_custom_request_a["custom_request_and_route/"]
ROOT_docs_src --> ROOT_docs_src_custom_request_a
ROOT_docs_src_custom_response["custom_response/"]
ROOT_docs_src --> ROOT_docs_src_custom_response
ROOT_docs_src_dataclasses_["dataclasses_/"]
ROOT_docs_src --> ROOT_docs_src_dataclasses_
ROOT_docs_src_debugging["debugging/"]
ROOT_docs_src --> ROOT_docs_src_debugging
ROOT_docs_src_dependencies["dependencies/"]
ROOT_docs_src --> ROOT_docs_src_dependencies
ROOT_docs_src_dependency_testi["dependency_testing/"]
ROOT_docs_src --> ROOT_docs_src_dependency_testi
ROOT_docs_src_encoder["encoder/"]
ROOT_docs_src --> ROOT_docs_src_encoder
ROOT_docs_src_events["events/"]
ROOT_docs_src --> ROOT_docs_src_events
ROOT_docs_src_extending_openap["extending_openapi/"]
ROOT_docs_src --> ROOT_docs_src_extending_openap
ROOT_docs_src_extra_data_types["extra_data_types/"]
ROOT_docs_src --> ROOT_docs_src_extra_data_types
ROOT_docs_src_extra_models["extra_models/"]
ROOT_docs_src --> ROOT_docs_src_extra_models
ROOT_docs_src_first_steps["first_steps/"]
ROOT_docs_src --> ROOT_docs_src_first_steps
ROOT_docs_src_frontend["frontend/"]
ROOT_docs_src --> ROOT_docs_src_frontend
ROOT_docs_src_generate_clients["generate_clients/"]
ROOT_docs_src --> ROOT_docs_src_generate_clients
ROOT_docs_src_graphql_["graphql_/"]
ROOT_docs_src --> ROOT_docs_src_graphql_
ROOT_docs_src_handling_errors["handling_errors/"]
ROOT_docs_src --> ROOT_docs_src_handling_errors
ROOT_docs_src_header_params["header_params/"]
ROOT_docs_src --> ROOT_docs_src_header_params
ROOT_docs_src_header_param_mod["header_param_models/"]
ROOT_docs_src --> ROOT_docs_src_header_param_mod
ROOT_docs_src_json_base64_byte["json_base64_bytes/"]
ROOT_docs_src --> ROOT_docs_src_json_base64_byte
ROOT_docs_src_metadata["metadata/"]
ROOT_docs_src --> ROOT_docs_src_metadata
ROOT_docs_src_middleware["middleware/"]
ROOT_docs_src --> ROOT_docs_src_middleware
ROOT_docs_src_openapi_callback["openapi_callbacks/"]
ROOT_docs_src --> ROOT_docs_src_openapi_callback
ROOT_docs_src_openapi_webhooks["openapi_webhooks/"]
ROOT_docs_src --> ROOT_docs_src_openapi_webhooks
ROOT_docs_src_path_operation_a["path_operation_advanced_configuration/"]
ROOT_docs_src --> ROOT_docs_src_path_operation_a
ROOT_docs_src_path_operation_c["path_operation_configuration/"]
ROOT_docs_src --> ROOT_docs_src_path_operation_c
ROOT_docs_src_path_params["path_params/"]
ROOT_docs_src --> ROOT_docs_src_path_params
ROOT_docs_src_path_params_nume["path_params_numeric_validations/"]
ROOT_docs_src --> ROOT_docs_src_path_params_nume
ROOT_docs_src_pydantic_v1_in_v["pydantic_v1_in_v2/"]
ROOT_docs_src --> ROOT_docs_src_pydantic_v1_in_v
ROOT_docs_src_python_types["python_types/"]
ROOT_docs_src --> ROOT_docs_src_python_types
ROOT_docs_src_query_params["query_params/"]
ROOT_docs_src --> ROOT_docs_src_query_params
ROOT_docs_src_query_params_str["query_params_str_validations/"]
ROOT_docs_src --> ROOT_docs_src_query_params_str
ROOT_docs_src_query_param_mode["query_param_models/"]
ROOT_docs_src --> ROOT_docs_src_query_param_mode
ROOT_docs_src_request_files["request_files/"]
ROOT_docs_src --> ROOT_docs_src_request_files
ROOT_docs_src_request_forms["request_forms/"]
ROOT_docs_src --> ROOT_docs_src_request_forms
ROOT_docs_src_request_forms_an["request_forms_and_files/"]
ROOT_docs_src --> ROOT_docs_src_request_forms_an
ROOT_docs_src_request_form_mod["request_form_models/"]
ROOT_docs_src --> ROOT_docs_src_request_form_mod
ROOT_docs_src_response_change_["response_change_status_code/"]
ROOT_docs_src --> ROOT_docs_src_response_change_
ROOT_docs_src_response_cookies["response_cookies/"]
ROOT_docs_src --> ROOT_docs_src_response_cookies
ROOT_docs_src_response_directl["response_directly/"]
ROOT_docs_src --> ROOT_docs_src_response_directl
ROOT_docs_src_response_headers["response_headers/"]
ROOT_docs_src --> ROOT_docs_src_response_headers
ROOT_docs_src_response_model["response_model/"]
ROOT_docs_src --> ROOT_docs_src_response_model
ROOT_docs_src_response_status_["response_status_code/"]
ROOT_docs_src --> ROOT_docs_src_response_status_
ROOT_docs_src_schema_extra_exa["schema_extra_example/"]
ROOT_docs_src --> ROOT_docs_src_schema_extra_exa
ROOT_docs_src_security["security/"]
ROOT_docs_src --> ROOT_docs_src_security
ROOT_docs_src_separate_openapi["separate_openapi_schemas/"]
ROOT_docs_src --> ROOT_docs_src_separate_openapi
ROOT_docs_src_server_sent_even["server_sent_events/"]
ROOT_docs_src --> ROOT_docs_src_server_sent_even
ROOT_docs_src_settings["settings/"]
ROOT_docs_src --> ROOT_docs_src_settings
ROOT_docs_src_sql_databases["sql_databases/"]
ROOT_docs_src --> ROOT_docs_src_sql_databases
ROOT_docs_src_static_files["static_files/"]
ROOT_docs_src --> ROOT_docs_src_static_files
ROOT_docs_src_stream_data["stream_data/"]
ROOT_docs_src --> ROOT_docs_src_stream_data
ROOT_docs_src_stream_json_line["stream_json_lines/"]
ROOT_docs_src --> ROOT_docs_src_stream_json_line
ROOT_docs_src_strict_content_t["strict_content_type/"]
ROOT_docs_src --> ROOT_docs_src_strict_content_t
ROOT_docs_src_sub_applications["sub_applications/"]
ROOT_docs_src --> ROOT_docs_src_sub_applications
ROOT_docs_src_templates["templates/"]
ROOT_docs_src --> ROOT_docs_src_templates
ROOT_docs_src_using_request_di["using_request_directly/"]
ROOT_docs_src --> ROOT_docs_src_using_request_di
ROOT_docs_src_websockets_["websockets_/"]
ROOT_docs_src --> ROOT_docs_src_websockets_
ROOT_docs_src_wsgi["wsgi/"]
ROOT_docs_src --> ROOT_docs_src_wsgi
ROOT_fastapi["fastapi/"]
ROOT --> ROOT_fastapi
ROOT_fastapi_dependencies["dependencies/"]
ROOT_fastapi --> ROOT_fastapi_dependencies
ROOT_fastapi_middleware["middleware/"]
ROOT_fastapi --> ROOT_fastapi_middleware
ROOT_fastapi_openapi["openapi/"]
ROOT_fastapi --> ROOT_fastapi_openapi
ROOT_fastapi_security["security/"]
ROOT_fastapi --> ROOT_fastapi_security
ROOT_fastapi__compat["_compat/"]
ROOT_fastapi --> ROOT_fastapi__compat
ROOT_scripts["scripts/"]
ROOT --> ROOT_scripts
ROOT_scripts_playwright["playwright/"]
ROOT_scripts --> ROOT_scripts_playwright
ROOT_scripts_tests["tests/"]
ROOT_scripts --> ROOT_scripts_tests
ROOT_tests["tests/"]
ROOT --> ROOT_tests
ROOT_tests_benchmarks["benchmarks/"]
ROOT_tests --> ROOT_tests_benchmarks
ROOT_tests_memory_benchmarks["memory_benchmarks/"]
ROOT_tests --> ROOT_tests_memory_benchmarks
ROOT_tests_test_modules_same_n["test_modules_same_name_body/"]
ROOT_tests --> ROOT_tests_test_modules_same_n
ROOT_tests_test_request_params["test_request_params/"]
ROOT_tests --> ROOT_tests_test_request_params
ROOT_tests_test_tutorial["test_tutorial/"]
ROOT_tests --> ROOT_tests_test_tutorial
ROOT_tests_test_validate_respo["test_validate_response_recursive/"]
ROOT_tests --> ROOT_tests_test_validate_respo
```
