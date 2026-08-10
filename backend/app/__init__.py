from flask import Flask, jsonify

from app.config import Config
from app.extensions import db, cors, jwt,migrate

# Nimportiw juste el routes el core lli khallinahom
from app.routes import (
    user_bp,
    project_bp,
    analysis_bp,
    document_bp,
    analyze_bp,
    auth_bp
)


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(
    app,
    resources={
        r"/api/*": {
            "origins": [
                "http://localhost:5173",
            ],
            "methods": [
                "GET",
                "POST",
                "PUT",
                "DELETE",
                "OPTIONS"
            ],
            "allow_headers": [
                "Content-Type",
                "Authorization"
            ],
            "supports_credentials": True
        }
    }
)
    jwt.init_app(app)



    # Import core models (Na77ina repository_file, generated_file, log)
    from app.models import (
        user,
        project,
        analysis,
        document
    )


    # ==========================
    # Routes registration (Épurée)
    # ==========================

    app.register_blueprint(
        user_bp,
        url_prefix="/api/users"
    )

    app.register_blueprint(
        project_bp,
        url_prefix="/api/projects"
    )

    app.register_blueprint(
        analysis_bp,
        url_prefix="/api/analyses"
    )

    app.register_blueprint(
        document_bp,
        url_prefix="/api/documents"
    )

    # Pipeline principal
    app.register_blueprint(
        analyze_bp,
        url_prefix="/api/analyze"
    )
        # Authentication
    app.register_blueprint(
        auth_bp,
        url_prefix="/api/auth"
    )




    # ==========================
    # Health check
    # ==========================

    @app.route("/api/health")
    def health_check():
        return jsonify({
            "status": "ok",
            "message": "API Flask opérationnelle"
        })

    return app