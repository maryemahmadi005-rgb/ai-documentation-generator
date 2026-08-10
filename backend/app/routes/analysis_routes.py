"""
analysis_routes.py

CRUD endpoints for analyses.
"""

from flask import Blueprint, request, jsonify

from services.analysis_service import (
    create_analysis,
    update_analysis_status,
    get_analysis_by_id,
    ProjectNotFoundError,
    AnalysisNotFoundError
)


analysis_bp = Blueprint(
    "analysis",
    __name__,
    url_prefix="/api/analyses"
)



# =====================================================
# GET ONE ANALYSIS
# GET /api/analyses/<id>
# =====================================================

@analysis_bp.route("/<int:analysis_id>", methods=["GET"])
def get_analysis(analysis_id):

    try:

        analysis = get_analysis_by_id(
            analysis_id
        )

        return jsonify(
            analysis.to_dict()
        ), 200


    except AnalysisNotFoundError as e:

        return jsonify({
            "error": str(e)
        }), 404


    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500





# =====================================================
# CREATE ANALYSIS
# POST /api/analyses
# =====================================================

@analysis_bp.route("", methods=["POST"])
def create_new_analysis():

    data = request.get_json() or {}

    project_id = data.get(
        "project_id"
    )


    if not project_id:

        return jsonify({
            "error": "project_id obligatoire"
        }), 400



    try:

        analysis = create_analysis(
            project_id=project_id
        )


        return jsonify(
            analysis.to_dict()
        ), 201



    except ProjectNotFoundError as e:

        return jsonify({
            "error": str(e)
        }), 404



    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500





# =====================================================
# UPDATE ANALYSIS
# PUT /api/analyses/<id>
# =====================================================

@analysis_bp.route("/<int:analysis_id>", methods=["PUT"])
def update_analysis(analysis_id):

    data = request.get_json() or {}


    try:

        analysis = update_analysis_status(

            analysis_id=analysis_id,


            status=data.get(
                "status"
            ),


            error_message=data.get(
                "error_message"
            ),


            detected_architecture=data.get(
                "detected_architecture"
            ),


            architecture_score=data.get(
                "architecture_score"
            ),


            architecture_confidence=data.get(
                "architecture_confidence"
            ),


            readme_content=data.get(
                "readme_content"
            ),


            ai_summary=data.get(
                "ai_summary"
            ),


            project_statistics=data.get(
                "project_statistics"
            )

        )


        return jsonify(
            analysis.to_dict()
        ), 200




    except AnalysisNotFoundError as e:

        return jsonify({
            "error": str(e)
        }), 404




    except ValueError as e:

        return jsonify({
            "error": str(e)
        }), 400




    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500