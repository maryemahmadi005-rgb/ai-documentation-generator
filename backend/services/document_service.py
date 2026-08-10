"""
document_service.py

Service responsible for managing generated documentation.
"""

from app.extensions import db

from app.models.document import Document
from app.models.analysis import Analysis



# ==========================================================
# Exceptions
# ==========================================================

class AnalysisNotFoundError(Exception):
    pass



class DocumentNotFoundError(Exception):
    pass



class InvalidDocumentFormatError(Exception):
    pass





# ==========================================================
# Allowed formats
# ==========================================================

VALID_FORMATS = {

    "markdown",
    "html",
    "pdf"

}





# ==========================================================
# Create document
# ==========================================================

def create_document(

    analysis_id: int,

    title: str,

    content: str,

    format: str = "markdown",

    file_path: str = None

) -> Document:



    if format not in VALID_FORMATS:

        raise InvalidDocumentFormatError(

            f"Format invalide : {format}"

        )




    analysis = db.session.get(

        Analysis,

        analysis_id

    )



    if not analysis:


        raise AnalysisNotFoundError(

            f"Aucune analyse avec l'id {analysis_id}."

        )





    document = Document(

        analysis_id=analysis_id,

        title=title,

        content=content,

        format=format,

        file_path=file_path

    )





    db.session.add(

        document

    )


    db.session.commit()



    return document





# ==========================================================
# Get document by analysis
# ==========================================================

def get_document_by_analysis(

    analysis_id: int

) -> Document:



    document = (

        db.session

        .query(Document)

        .filter_by(

            analysis_id=analysis_id

        )

        .all()

    )



    if not document:


        raise DocumentNotFoundError(

            f"Aucun document pour l'analyse {analysis_id}."

        )



    return document





# ==========================================================
# Get document by id
# ==========================================================

def get_document_by_id(

    document_id: int

) -> Document:



    document = db.session.get(

        Document,

        document_id

    )



    if not document:


        raise DocumentNotFoundError(

            f"Aucun document avec l'id {document_id}."

        )



    return document





# ==========================================================
# Update document
# ==========================================================

def update_document(

    document_id: int,

    title: str = None,

    content: str = None,

    format: str = None,

    file_path: str = None

) -> Document:



    document = db.session.get(

        Document,

        document_id

    )



    if not document:


        raise DocumentNotFoundError(

            f"Aucun document avec l'id {document_id}."

        )





    if format and format not in VALID_FORMATS:


        raise InvalidDocumentFormatError(

            f"Format invalide : {format}"

        )





    if title is not None:

        document.title = title



    if content is not None:

        document.content = content



    if format is not None:

        document.format = format



    if file_path is not None:

        document.file_path = file_path





    db.session.commit()



    return document





# ==========================================================
# Delete document
# ==========================================================

def delete_document(

    document_id: int

):


    document = db.session.get(

        Document,

        document_id

    )



    if not document:


        raise DocumentNotFoundError(

            f"Aucun document avec l'id {document_id}."

        )



    db.session.delete(

        document

    )


    db.session.commit()



    return True