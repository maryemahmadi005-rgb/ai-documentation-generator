import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from services.doc_builder import DocBuilder


def test_ai_candidate_files_include_doc_and_config_extensions():
    from services.documentation_service import _select_ai_candidate_files

    files = [
        {"path": "src/app.py"},
        {"path": "README.md"},
        {"path": "docs/guide.mdx"},
        {"path": "config/app.json"},
        {"path": "deploy/docker-compose.yml"},
        {"path": "config/settings.toml"},
        {"path": "assets/logo.png"},
        {"path": "archive.tar.gz"},
    ]

    selected = _select_ai_candidate_files(files)

    assert [item["path"] for item in selected] == [
        "src/app.py",
        "README.md",
        "docs/guide.mdx",
        "config/app.json",
        "deploy/docker-compose.yml",
        "config/settings.toml",
    ]


def test_readme_and_documentation_are_distinct():
    with tempfile.TemporaryDirectory() as tmpdir:
        builder = DocBuilder("DemoProject", tmpdir)

        readme = builder.build_readme(
            intro="README court",
            metadata={"is_git_repo": False},
            structure={"files": [], "dirs": {}},
        )

        documentation = builder.build_documentation_page(
            ai_summary="Documentation technique détaillée avec objectif, architecture, modules, flux de données, points d'entrée, dépendances, recommandations et analyse détaillée des fichiers.",
            files={
                "src/app.py": {"summary": "Point d'entrée principal du service."},
                "src/service.py": {"summary": "Service métier principal."},
            },
            architecture="Architecture détectée : service web Flask",
            diagrams={"project_tree": "graph TD"},
        )

        assert readme != documentation
        assert "README court" in readme
        assert "Documentation technique" in documentation
        assert "Architecture détectée" in documentation
        assert "Analyse des fichiers" in documentation
        assert "Architecture" not in readme
        assert "Analyse des fichiers" not in readme


if __name__ == "__main__":
    test_readme_and_documentation_are_distinct()
    print("test_doc_content_separation passed")
