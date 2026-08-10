from app.extensions import db


class Analysis(db.Model):
    __tablename__ = "analyses"

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    

    project_id = db.Column(
        db.Integer,
        db.ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False
    )

    status = db.Column(
        db.Enum("pending", "running", "completed", "failed"),
        nullable=False,
        default="pending"
    )

    commit_hash = db.Column(
        db.String(64),
        nullable=True
    )
    
    git_info = db.Column(
        db.JSON,
        nullable=True
        )

    started_at = db.Column(
        db.DateTime,
        nullable=True
    )

    finished_at = db.Column(
        db.DateTime,
        nullable=True
    )

    error_message = db.Column(
        db.Text,
        nullable=True
    )

    detected_architecture = db.Column(
        db.String(100),
        nullable=True
    )

    architecture_score = db.Column(
        db.Integer,
        nullable=True
    )

    architecture_confidence = db.Column(
        db.Numeric(5, 2),
        nullable=True
    )

    # Explication textuelle de la détection d'architecture (type +
    # confiance + signaux principaux), générée par le pipeline de
    # documentation. Permet au frontend d'afficher une explication
    # lisible sans recalculer quoi que ce soit.
    architecture_explanation = db.Column(
        db.Text,
        nullable=True
    )

    # Arborescence du repository analysé (même format que
    # `structure` renvoyé par GitAnalyzer.analyze() : dict imbriqué
    # {"files": [...], "dirs": {...}}).
    repository_tree = db.Column(
        db.JSON,
        nullable=True
    )

    # Liste à plat des fichiers analysés, avec un résumé léger par
    # fichier (path, line_count, classes, functions, summary).
    # Sert au frontend pour afficher la liste des fichiers sans
    # avoir à retraverser repository_tree.
    files = db.Column(
        db.JSON,
        nullable=True
    )

    # Statistiques Overview (évite au frontend de recompter depuis
    # repository_tree/files à chaque affichage).
    # Statistiques Overview (évite au frontend de recompter depuis ssssssssssssssssssssss


    files_count = db.Column(
        db.Integer,
        nullable=True
    )

    directories_count = db.Column(
        db.Integer,
        nullable=True
    )

    # Liste des technologies détectées (ex: ["Python", "JavaScript"]).
    technologies = db.Column(
        db.JSON,
        nullable=True
    )

    project_statistics = db.Column(
        db.JSON,
        nullable=True
    )

    readme_content = db.Column(
        db.Text(length=4294967295),
        nullable=True
        )

    ai_summary = db.Column(
        db.Text(length=4294967295),
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.current_timestamp()
    )


    # Relations
    project = db.relationship(
        "Project",
        back_populates="analyses"
    )

    documents = db.relationship(
        "Document",
        back_populates="analysis",
        cascade="all, delete-orphan"
    )


    def to_dict(self):
        return {
            "id": self.id,
            "project_id": self.project_id,
            "project_name": self.project.name if self.project else None,
            "github_url": self.project.github_url if self.project else None,
            "status": self.status,
            "commit_hash": self.commit_hash,
            "git_info": self.git_info,
            
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "finished_at": self.finished_at.isoformat() if self.finished_at else None,
            "error_message": self.error_message,
            "detected_architecture": self.detected_architecture,
            "architecture_score": self.architecture_score,
            "architecture_confidence": float(self.architecture_confidence)
            if self.architecture_confidence is not None else None,
            "architecture_explanation": self.architecture_explanation,
            "repository_tree": self.repository_tree,
            "files": self.files,
            "files_count": self.files_count,
            "directories_count": self.directories_count,
            "technologies": self.technologies,
            "readme_content": self.readme_content,
            "documentation_content":self.documents[0].content if self.documents else "",
            "project_statistics": getattr(self, "project_statistics", None),
            "statistics": getattr(self, "project_statistics", None),
            

            "ai_summary": self.ai_summary,
            "created_at": self.created_at.isoformat()
            if self.created_at else None
        }