from app.extensions import db


class Document(db.Model):

    __tablename__ = "documents"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    analysis_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "analyses.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )


    title = db.Column(
        db.String(200),
        nullable=False
    )


    content = db.Column(
        db.Text(length=4294967295),
        nullable=True
    )


    format = db.Column(
        db.Enum(
            "markdown",
            "html",
            "pdf"
        ),
        nullable=False,
        default="markdown"
    )


    file_path = db.Column(
        db.String(500),
        nullable=True
    )


    created_at = db.Column(
        db.DateTime,
        server_default=db.func.current_timestamp()
    )



    # ===================================
    # Relation
    # One Analysis -> Many Documents
    # ===================================

    analysis = db.relationship(
        "Analysis",
        back_populates="documents"
    )



    def to_dict(self):

        return {

            "id": self.id,

            "analysis_id":
                self.analysis_id,

            "title":
                self.title,

            "content":
                self.content,

            "format":
                self.format,

            "file_path":
                self.file_path,

            "created_at":
                self.created_at.isoformat()
                if self.created_at else None

        }