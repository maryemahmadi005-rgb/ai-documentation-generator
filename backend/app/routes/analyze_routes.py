"""
analyze_routes.py

Endpoint principal du projet :
- POST /api/analyze
- GET /api/analyze/history
"""

import logging

from flask import Blueprint, request, jsonify

from app.models.analysis import Analysis

from services.analysis_service import (
    create_analysis,
    update_analysis_status,
    ProjectNotFoundError
)

from services.document_service import create_document

from app.routes.document_routes import _document_dict_with_site

from services.documentation_service import (
    generate_documentation,
    DocumentationPipelineError
)
from flask import request


logger = logging.getLogger("app.pipeline")


analyze_bp = Blueprint(
    "analyze",
    __name__
)



# ===================================
# GET ANALYSIS HISTORY
# ===================================

@analyze_bp.route("/history", methods=["GET"])
def get_analyses():

    analyses = Analysis.query.all()

    return jsonify([

        {
            **analysis.to_dict(),

            "readme_content":
                analysis.readme_content or "",


            "documentation_content":
                analysis.documents[0].content 
                if analysis.documents 
                else "",

            "document":
                _document_dict_with_site(
                    analysis.documents[0]
                )
                if analysis.documents
                else None

        }

        for analysis in analyses

    ]), 200





# ===================================
# RUN DOCUMENTATION GENERATION
# ===================================

@analyze_bp.route("", methods=["POST"])
def analyze_repository_route():


    from services.ollama_client import reset_default_client

    reset_default_client()


    data = request.get_json(silent=True) or {}


    project_id = data.get("project_id")

    github_url = data.get("github_url")



    if not project_id or not github_url:

        return jsonify({

            "error":
            "Les champs 'project_id' et 'github_url' sont obligatoires."

        }), 400





    # CREATE ANALYSIS

    try:

        analysis = create_analysis(
            project_id=project_id
        )


    except ProjectNotFoundError as e:

        return jsonify({

            "error": str(e)

        }), 404





    def log_callback(level, message):

        log_message = (
            f"[Analysis #{analysis.id}] {message}"
        )


        if level == "ERROR":

            logger.error(log_message)

        elif level == "WARNING":

            logger.warning(log_message)

        else:

            logger.info(log_message)






    # RUNNING

    update_analysis_status(

        analysis_id=analysis.id,

        status="running"

    )






    # PIPELINE

    try:

        result = generate_documentation(

            github_url,

            analysis_id= analysis.id,

            log_callback=log_callback

        )


    except DocumentationPipelineError as e:


        update_analysis_status(

            analysis_id=analysis.id,

            status="failed",

            error_message=str(e)

        )


        return jsonify({

            "error":
            "Le pipeline d'analyse a échoué.",


            "detail":
            str(e),


            "analysis_id":
            analysis.id

        }), 500






    # CREATE ONLY TECHNICAL DOCUMENTATION

    documentation_document = create_document(

        analysis_id=analysis.id,


        title="Technical Documentation",


        content=result.get(
            "documentation_content",
            ""
        ),


        format="markdown",


        file_path=result.get(
            "file_path"
        )

    )
    metadata = result.get("metadata") or {}

    commit_hash = (
        result.get("commit_hash")
        or metadata.get("last_commit_hash")
    )


    # Git information
    git_info = {

        "branch":
            metadata.get("branch"),

        "last_commit_hash":
            metadata.get("last_commit_hash")
            or result.get("commit_hash"),

        "last_commit_message":
            metadata.get("last_commit_message"),

        "last_commit_author":
            metadata.get("last_commit_author"),

        "last_commit_date":
            metadata.get("last_commit_date"),

        "total_commits":
            metadata.get("total_commits"),

        "remotes":
            metadata.get("remotes")
    }



    # UPDATE ANALYSIS

    analysis = update_analysis_status(

        analysis_id=analysis.id,

        status="completed",

        detected_architecture=(
            result.get("architecture") 
            or result.get("detected_architecture")
            or result.get("architecture_analysis", {}).get("detected_architecture")
        ),

        architecture_score=(
            result.get("architecture_score")
            or result.get("architecture_analysis", {}).get("score")
            ),

        architecture_confidence=(
            result.get("architecture_confidence")
            or result.get("architecture_analysis", {}).get("confidence")
             ),

        architecture_explanation=
            result.get("architecture_explanation"),

        repository_tree=
            result.get("repository_tree"),

        files=
            result.get("files"),

        files_count=
            result.get("files_count"),

        directories_count=
            result.get("directories_count"),

        technologies=
            result.get("technologies"),
        

        readme_content=
            result.get("readme_content"),

        ai_summary=
            result.get("ai_summary"),

        commit_hash=commit_hash,

        git_info=git_info
    )




    site_url = (

        request.host_url.rstrip("/") + f"/api/documents/{documentation_document.id}/site"

        if result.get("site_path")

        else None

    )

    return jsonify({

        "analysis": {


            "id":
                analysis.id,


            "project_id":
                analysis.project_id,


            "project_name":
                analysis.project.name,


            "github_url":
                analysis.project.github_url,


            "status":
                analysis.status,



            "readme_content":
                analysis.readme_content or "",



            "documentation_content":
                documentation_document.content,



            "architecture":
                analysis.detected_architecture,



            "architecture_score":
                analysis.architecture_score,
            "detected_architecture":
                analysis.detected_architecture,
            "architecture_score":
            analysis.architecture_score,



            "architecture_confidence":

                float(
                    analysis.architecture_confidence
                )

                if analysis.architecture_confidence is not None

                else None,



            "architecture_explanation":
                analysis.architecture_explanation,



            "ai_summary":
                analysis.ai_summary,



            "repository_tree":
                analysis.repository_tree,



            "files":
                analysis.files,


            "project_statistics":
                getattr(analysis, "project_statistics", None)
                or result.get("project_statistics"),

            "statistics": (
                getattr(analysis, "project_statistics", None)
                or result.get("project_statistics")
                or {
                    "total_files": analysis.files_count,
                    "total_lines": None,
                    "classes": None,
                    "functions": None,
                    "complexity_score": None,
                    "file_types": None,
                }
            ),

            "file_dependencies":
                result.get("file_dependencies"),


            "blueprints":
                result.get("blueprints"),


            "files_count":
                analysis.files_count,



            "directories_count":
                analysis.directories_count,



            "technologies":
                analysis.technologies,



            "git_info":
                git_info,



            "site_url":
                site_url,



            "document":
                _document_dict_with_site(
                    documentation_document
                )

        }

    }), 201