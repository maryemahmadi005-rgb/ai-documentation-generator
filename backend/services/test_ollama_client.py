import sys
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from services.ollama_client import OllamaClient


def test_fallback_technical_documentation_content_is_available(monkeypatch):
    client = OllamaClient(timeout=1)

    def raise_timeout(*args, **kwargs):
        raise requests.exceptions.Timeout("simulated timeout")

    monkeypatch.setattr(client, "generate", raise_timeout)

    content = client.generate_technical_documentation_content(
        project_name="Demo",
        tech_stack=["Python", "Flask"],
        databases=["SQLite"],
        architecture_type="Flask Application",
        architecture_confidence=80,
        structure_overview="app/\nservices/",
        key_files_digest=["- app.py : point d'entrée"],
        entry_points=["app.py"],
        dependencies=["flask==3.0.0"],
    )

    assert isinstance(content, str)
    assert "Documentation technique" in content
    assert "Flask Application" in content


def test_readme_fallback_content_is_available(monkeypatch):
    client = OllamaClient(timeout=1)

    def raise_timeout(*args, **kwargs):
        raise requests.exceptions.Timeout("simulated timeout")

    monkeypatch.setattr(client, "generate", raise_timeout)

    content = client.generate_readme_content(
        project_name="Demo",
        tech_stack=["Python", "Flask"],
        dependencies=["flask==3.0.0"],
        entry_points=["app.py"],
    )

    assert isinstance(content, str)
    assert "Description courte" in content
    assert "Demo" in content
