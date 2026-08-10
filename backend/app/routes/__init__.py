from app.routes.user_routes import user_bp
from app.routes.project_routes import project_bp
from app.routes.analysis_routes import analysis_bp
from app.routes.document_routes import document_bp
from app.routes.analyze_routes import analyze_bp
from app.routes.auth_routes import auth_bp

__all__ = [
    "user_bp",
    "project_bp",
    "analysis_bp",
    "document_bp",
    "analyze_bp",
    "auth_bp"
    ]