from datetime import datetime

from app.extensions import db
from app.models.analysis import Analysis
from app.models.project import Project
import json


# ==========================================================
# Exceptions
# ==========================================================

class ProjectNotFoundError(Exception):
    pass


class AnalysisNotFoundError(Exception):
    pass


class InvalidAnalysisStatusError(Exception):
    pass
def safe_json_load(value):
    if isinstance(value, str):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value
    return value



# ==========================================================
# Allowed statuses
# ==========================================================

VALID_STATUSES = {
    "pending",
    "running",
    "completed",
    "failed"
}



# ==========================================================
# Create analysis
# ==========================================================

def create_analysis(project_id: int) -> Analysis:

    project = db.session.get(
        Project,
        project_id
    )

    if not project:
        raise ProjectNotFoundError(
            f"Aucun projet avec l'id {project_id}."
        )


    analysis = Analysis(
        project_id=project_id,
        status="pending"
    )


    db.session.add(
        analysis
    )

    db.session.commit()


    return analysis



# ==========================================================
# Update analysis
# ==========================================================

def update_analysis_status(

    analysis_id: int,

    status: str,

    error_message: str = None,

    detected_architecture: str = None,

    architecture_score: int = None,

    architecture_confidence=None,

    architecture_explanation: str = None,

    repository_tree: dict = None,

    files: list = None,

    files_count: int = None,

    directories_count: int = None,

    technologies: list = None,

    readme_content: str = None,

    ai_summary: str = None,

    commit_hash: str = None,

    git_info=None,

    project_statistics=None


) -> Analysis:


    if status not in VALID_STATUSES:

        raise InvalidAnalysisStatusError(
            f"Status invalide : {status}"
        )



    analysis = db.session.get(
        Analysis,
        analysis_id
    )


    if not analysis:

        raise AnalysisNotFoundError(
            f"Aucune analyse avec l'id {analysis_id}."
        )



    # Status

    analysis.status = status



    # Dates

    if status == "running":

        analysis.started_at = datetime.utcnow()



    if status in {"completed", "failed"}:

        analysis.finished_at = datetime.utcnow()



    # Error

    if error_message is not None:

        analysis.error_message = error_message



    # Architecture

    if detected_architecture is not None:

        analysis.detected_architecture = detected_architecture



    if architecture_score is not None:

        analysis.architecture_score = architecture_score
    if git_info is not None:
        analysis.git_info = git_info
    



    if architecture_confidence is not None:

        analysis.architecture_confidence = architecture_confidence



    if architecture_explanation is not None:

        analysis.architecture_explanation = architecture_explanation



    # Repository data
    if repository_tree is not None:
        analysis.repository_tree = safe_json_load(repository_tree)


    if files is not None:
        analysis.files = safe_json_load(files)




    if files_count is not None:

        analysis.files_count = files_count



    if directories_count is not None:

        analysis.directories_count = directories_count



    if technologies is not None:
        analysis.technologies = safe_json_load(technologies)



    # README stored in analyses table

    if readme_content is not None:

        analysis.readme_content = readme_content



    # AI summary

    if ai_summary is not None:

        analysis.ai_summary = ai_summary

    if commit_hash is not None:

        analysis.commit_hash = commit_hash

    if project_statistics is not None:

        analysis.project_statistics = safe_json_load(project_statistics)


    db.session.commit()


    return analysis



# ==========================================================
# Get analysis by id
# ==========================================================

def get_analysis_by_id(
    analysis_id: int
) -> Analysis:


    analysis = db.session.get(
        Analysis,
        analysis_id
    )


    if not analysis:

        raise AnalysisNotFoundError(
            f"Aucune analyse avec l'id {analysis_id}."
        )


    return analysis