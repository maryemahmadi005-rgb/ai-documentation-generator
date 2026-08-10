from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from app.extensions import db
from app.models.project import Project

project_bp = Blueprint("projects", __name__)


# 1. دالة استخراج اسم المشروع معرّفة في الأعلى بشكل مستقل
def extract_repo_name(url):
    if not url:
        return ""
    return url.rstrip("/").split("/")[-1].replace(".git", "")


# GET ALL PROJECTS
@project_bp.route("", methods=["GET"])
def get_projects():
    projects = Project.query.all()
    return jsonify([p.to_dict() for p in projects]), 200


# CREATE PROJECT (مع التثبت من وجود المشروع والـ Rollback)
@project_bp.route("", methods=["POST"])
def create_project():
    data = request.get_json() or {}

    if "user_id" not in data or "github_url" not in data:
        return jsonify({"error": "user_id et github_url sont obligatoires"}), 400

    github_url = data["github_url"].strip()
    user_id = data["user_id"]
    project_name = extract_repo_name(github_url)

    # التثبت هل المشروع موجود مسبقاً لنفس المستخدم لتفادي الكراش
    existing_project = Project.query.filter_by(
        user_id=user_id, 
        github_url=github_url
    ).first()

    if existing_project:
        return jsonify({
            "message": "Project already exists",
            "project": existing_project.to_dict()
        }), 200

    try:
        project = Project(
            user_id=user_id,
            name=project_name,
            github_url=github_url,
            description=data.get("description"),
            language=data.get("language")
        )

        db.session.add(project)
        db.session.commit()

        return jsonify({
            "message": "Project created",
            "project": project.to_dict()
        }), 201

    except IntegrityError:
        db.session.rollback()
        project = Project.query.filter_by(github_url=github_url).first()
        if project:
            return jsonify({"project": project.to_dict()}), 200
        return jsonify({"error": "Integrity error"}), 400

    except Exception as e:
        db.session.rollback()
        print(f"❌ DATABASE ERROR: {str(e)}")
        return jsonify({"error": "Internal server error", "details": str(e)}), 500


# UPDATE PROJECT
@project_bp.route("/<int:id>", methods=["PUT"])
def update_project(id):
    project = Project.query.get_or_404(id)
    data = request.get_json() or {}

    project.name = data.get("name", project.name)
    project.github_url = data.get("github_url", project.github_url)
    project.description = data.get("description", project.description)
    project.language = data.get("language", project.language)

    try:
        db.session.commit()
        return jsonify({
            "message": "Project updated",
            "project": project.to_dict()
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# DELETE PROJECT
@project_bp.route("/<int:id>", methods=["DELETE"])
def delete_project(id):
    project = Project.query.get_or_404(id)

    try:
        db.session.delete(project)
        db.session.commit()
        return jsonify({"message": "Project deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500