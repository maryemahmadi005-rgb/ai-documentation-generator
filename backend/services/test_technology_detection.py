import json
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from services.analyzers.architecture_analyzer import detect_architecture
from services.documentation_service import _detect_technologies_with_evidence


def test_architecture_detection_requires_multiple_signals():
    structure = {
        "dirs": {
            "controllers": {"dirs": {}, "files": ["user_controller.py"]},
            "services": {"dirs": {}, "files": ["user_service.py"]},
            "repositories": {"dirs": {}, "files": ["user_repository.py"]},
        },
        "files": [],
    }

    result = detect_architecture(structure)

    assert result["type"] == "Layered Architecture"
    assert result["confidence_pct"] >= 50
    assert result["signals"]


def test_technology_detection_includes_evidence_from_repo_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        package_json = {
            "dependencies": {"react": "^18.0.0", "next": "^14.0.0"},
            "devDependencies": {"tailwindcss": "^3.0.0", "typescript": "^5.0.0"},
        }
        with open(os.path.join(tmpdir, "package.json"), "w", encoding="utf-8") as fh:
            json.dump(package_json, fh)

        with open(os.path.join(tmpdir, "next.config.js"), "w", encoding="utf-8") as fh:
            fh.write("module.exports = {}")

        with open(os.path.join(tmpdir, "tsconfig.json"), "w", encoding="utf-8") as fh:
            fh.write("{}")

        os.makedirs(os.path.join(tmpdir, "src"), exist_ok=True)

        with open(os.path.join(tmpdir, "src", "app.tsx"), "w", encoding="utf-8") as fh:
            fh.write("export default function App() { return <div /> }")

        detected = _detect_technologies_with_evidence(tmpdir, {})

        names = {item["name"] for item in detected}
        assert {"React", "Next.js", "TypeScript", "Tailwind CSS", "Vite"}.issubset(names)

        react = next(item for item in detected if item["name"] == "React")
        assert react["evidence"]
        assert any("package.json" in evidence for evidence in react["evidence"])
