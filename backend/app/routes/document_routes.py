from flask import Blueprint, request, jsonify, send_file, send_from_directory
import os

from app.models.document import Document
from services.document_service import (
    create_document,
    get_document_by_id,
    DocumentNotFoundError
)


document_bp = Blueprint(
    "document",
    __name__
)


def _resolve_site_dir(document):

    if not document.file_path:
        return None

    file_path = os.path.abspath(
        document.file_path
    )

    site_dir = os.path.join(
        os.path.dirname(file_path),
        "site"
    )

    print("FILE PATH ABS:", file_path)
    print("SITE DIR:", site_dir)
    print("EXISTS:", os.path.isdir(site_dir))

    return site_dir if os.path.isdir(site_dir) else None



def _document_dict_with_site(document):
    """
    Ajoute site_url au document.
    """

    data = document.to_dict()

    data["site_url"] = (
        f"/api/documents/{document.id}/site"
        if _resolve_site_dir(document)
        else None
        )

    return data



# ===================================
# GET ALL DOCUMENTS
# ===================================

@document_bp.route("", methods=["GET"])
def get_documents():

    documents = Document.query.all()

    return jsonify(
        [
            _document_dict_with_site(d)
            for d in documents
        ]
    ), 200




# ===================================
# CREATE DOCUMENT
# ===================================

@document_bp.route("", methods=["POST"])
def create_document_route():

    data = request.get_json() or {}


    if not data.get("analysis_id") or not data.get("title"):

        return jsonify({
            "error": "analysis_id et title sont obligatoires"
        }), 400



    document = create_document(

        analysis_id=data["analysis_id"],

        title=data["title"],

        content=data.get(
            "content",
            ""
        ),

        format=data.get(
            "format",
            "markdown"
        ),

        file_path=data.get(
            "file_path"
        )
    )


    return jsonify({

        "message": "Document created",

        "document":
            _document_dict_with_site(document)

    }), 201





# ===================================
# GET DOCUMENT BY ID
# ===================================

@document_bp.route(
    "/<int:id>",
    methods=["GET"]
)
def get_document(id):

    try:

        document = get_document_by_id(id)

        return jsonify(
            _document_dict_with_site(document)
        ), 200


    except DocumentNotFoundError as e:

        return jsonify({
            "error": str(e)
        }), 404





# ===================================
# GET DOCUMENTS BY ANALYSIS ID
# ===================================

@document_bp.route(
    "/analysis/<int:analysis_id>",
    methods=["GET"]
)
def get_documents_by_analysis(analysis_id):

    documents = Document.query.filter_by(
        analysis_id=analysis_id
    ).all()


    if not documents:

        return jsonify({
            "error": "No documents found"
        }), 404



    return jsonify(
        [
            _document_dict_with_site(doc)
            for doc in documents
        ]
    ), 200





# ===================================
# DELETE DOCUMENT
# ===================================

@document_bp.route(
    "/<int:id>",
    methods=["DELETE"]
)
def delete_document(id):

    document = Document.query.get_or_404(id)


    from app.extensions import db

    db.session.delete(document)
    print(Document.__tablename__)
    print("TYPE TREE:", type(analysis.repository_tree))
    print("TYPE FILES:", type(analysis.files))
    print("TYPE TECH:", type(analysis.technologies))

    db.session.commit()


    return jsonify({

        "message": "Document deleted"

    }), 200





# ===================================
# DOWNLOAD DOCUMENT
# ===================================

@document_bp.route(
    "/<int:id>/download",
    methods=["GET"]
)
def download_document_file(id):

    document = Document.query.get_or_404(id)



    if (
        not document.file_path
        or not os.path.exists(document.file_path)
    ):

        return jsonify({

            "error": "Fichier introuvable"

        }), 404



    return send_file(

        document.file_path,

        as_attachment=True,

        download_name=os.path.basename(
            document.file_path
        )

    )





# ===================================
# SERVE MKDOCS SITE
# ===================================

@document_bp.route(
    "/<int:id>/site",
    methods=["GET"]
)
@document_bp.route(
    "/<int:id>/site/",
    methods=["GET"]
)
def serve_document_site_index(id):

    document = Document.query.get_or_404(id)

    site_dir = _resolve_site_dir(document)


    if not site_dir:

        return jsonify({

            "error":
            "Site MkDocs introuvable pour ce document"

        }), 404



    return send_from_directory(
        site_dir,
        "index.html"
    )





@document_bp.route(
    "/<int:id>/site/<path:filename>",
    methods=["GET"]
)
def serve_document_site_file(id, filename):

    document = Document.query.get_or_404(id)

    site_dir = _resolve_site_dir(document)

    if not site_dir:
        return jsonify({
            "error": "Site MkDocs introuvable pour ce document"
        }), 404


    return send_from_directory(
        site_dir,
        filename
    )
# ===================================
# SERVE MKDOCS ASSETS
# ===================================
@document_bp.route(
    "/<int:id>/<path:filename>/",
    methods=["GET"]
)
@document_bp.route(
    "/<int:id>/<path:filename>",
    methods=["GET"]
)
def serve_document_assets(id, filename):

    document = Document.query.get_or_404(id)

    site_dir = _resolve_site_dir(document)

    if not site_dir:
        return jsonify({
            "error": "Site MkDocs introuvable"
        }), 404


    # نحذف slash الأخير
    filename = filename.rstrip("/")


    requested_path = os.path.join(
        site_dir,
        filename
    )


    print("REQUEST:", filename)
    print("PATH:", requested_path)


    # مثال assets/style.css
    if os.path.isfile(requested_path):
        return send_from_directory(
            site_dir,
            filename
        )


    # مثال comparaison/ -> comparaison/index.html
    index_path = os.path.join(
        requested_path,
        "index.html"
    )


    if os.path.isfile(index_path):
        return send_from_directory(
            requested_path,
            "index.html"
        )


    return jsonify({
        "error": "Page MkDocs introuvable",
        "requested": filename
    }),404