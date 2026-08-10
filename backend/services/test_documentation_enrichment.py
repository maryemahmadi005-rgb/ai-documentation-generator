import importlib.util
import pathlib
import sys
import types


sys.modules.setdefault("services.document_service", types.SimpleNamespace(create_document=lambda *args, **kwargs: None))
sys.modules.setdefault("services.git_service", types.SimpleNamespace(clone_repository=lambda *args, **kwargs: None))
sys.modules.setdefault("services.ollama_client", types.SimpleNamespace(get_default_client=lambda: None, heuristic_summary=lambda *args, **kwargs: ""))
sys.modules.setdefault("services.doc_builder", types.SimpleNamespace(DocBuilder=object))
sys.modules.setdefault("services.analyzers.architecture_analyzer", types.SimpleNamespace(detect_architecture=lambda *args, **kwargs: {}, build_comparison_markdown=lambda *args, **kwargs: "", generate_mermaid_diagram=lambda *args, **kwargs: "", generate_architecture_layers_diagram=lambda *args, **kwargs: "", generate_dataflow_diagram=lambda *args, **kwargs: "", generate_module_dependency_diagram=lambda *args, **kwargs: ""))
sys.modules.setdefault("services.analyzers.git_analyzer", types.SimpleNamespace(GitAnalyzer=object))

MODULE_PATH = pathlib.Path(__file__).resolve().parent / "documentation_service.py"
SPEC = importlib.util.spec_from_file_location("documentation_service_under_test", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

_build_project_statistics = MODULE._build_project_statistics
_build_file_dependencies = MODULE._build_file_dependencies
_build_blueprints = MODULE._build_blueprints


def test_build_project_statistics_aggregates_file_metrics():
    file_summaries = {
        "app/main/views.py": {
            "line_count": 30,
            "structure": {
                "classes": ["View"],
                "functions": ["index"],
                "imports": ["app.models", "os"],
                "api_endpoints": ["/health"],
            },
        },
        "app/auth/forms.py": {
            "line_count": 15,
            "structure": {
                "classes": ["Form"],
                "functions": [],
                "imports": ["flask"],
                "api_endpoints": [],
            },
        },
        "README.md": {
            "line_count": 8,
            "structure": {
                "classes": [],
                "functions": [],
                "imports": [],
                "api_endpoints": [],
            },
        },
    }

    stats = _build_project_statistics(file_summaries, {"files": ["app/main/views.py", "app/auth/forms.py"], "dirs": {}})

    assert stats["total_files"] == 3
    assert stats["python_files"] == 2
    assert stats["markdown_files"] == 1
    assert stats["total_classes"] == 2
    assert stats["total_functions"] == 1
    assert stats["total_api_endpoints"] == 1
    assert stats["total_lines_of_code"] == 53


def test_build_file_dependencies_uses_internal_project_files_only():
    file_summaries = {
        "app/main/views.py": {
            "structure": {
                "imports": ["app.models", "os", "app.forms"],
            }
        },
        "app/models.py": {
            "structure": {
                "imports": [],
            }
        },
        "app/forms.py": {
            "structure": {
                "imports": [],
            }
        },
    }

    dependencies = _build_file_dependencies(file_summaries)

    assert dependencies["app/main/views.py"] == ["app/models.py", "app/forms.py"]


def test_build_blueprints_groups_files_by_blueprint():
    file_summaries = {
        "app/auth/views.py": {
            "structure": {
                "blueprints": ["auth"],
            }
        },
        "app/auth/forms.py": {
            "structure": {
                "blueprints": [],
            }
        },
        "app/main/views.py": {
            "structure": {
                "blueprints": [],
            }
        },
    }

    blueprints = _build_blueprints(file_summaries)

    assert blueprints[0]["name"] == "auth"
    assert blueprints[0]["files"] == ["app/auth/forms.py", "app/auth/views.py"]
