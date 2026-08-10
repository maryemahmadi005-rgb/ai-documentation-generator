"""
Analyzers package.

Contains modules responsible for:
- Git repository analysis
- Software architecture detection
"""

from .git_analyzer import GitAnalyzer
from .architecture_analyzer import detect_architecture

__all__ = [
    "GitAnalyzer",
    "detect_architecture",
]