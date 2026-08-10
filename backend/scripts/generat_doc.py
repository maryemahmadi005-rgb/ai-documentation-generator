"""
documentation_service.py

Pipeline complet:

GitHub URL
    ->
clone repository
    ->
git analysis
    ->
AI summaries
    ->
architecture detection
    ->
documentation generation

No database operations.
"""

import os


from services.git_service import clone_repository

from services.analyzers.git_analyzer import GitAnalyzer

from services.ollama_client import OllamaClient

from services.analyzers.architecture_analyzer import (
    detect_architecture
)

from services.doc_builder import DocBuilder



class DocumentationPipelineError(Exception):
    pass




def generate_documentation(
    github_url: str,
    analysis_id=None,
    log_callback=None
):

    print("🚀 START DOCUMENTATION PIPELINE")
    print("URL =", github_url)


    def log(level, message):

        if log_callback:
            log_callback(level, message)



    try:

        # ==================================================
        # 1) Clone repository
        # ==================================================

        log(
            "INFO",
            "Clonage du dépôt GitHub..."
        )


        repo_path = clone_repository(
            github_url
        )


        print("✅ CLONE DONE:", repo_path)


        log(
            "INFO",
            f"Dépôt cloné : {repo_path}"
        )



        # ==================================================
        # 2) Git analysis
        # ==================================================

        log(
            "INFO",
            "Analyse du repository..."
        )


        analyzer = GitAnalyzer(
            repo_path
        )


        print("✅ GIT ANALYZER CREATED")


        structure = analyzer.walk_structure()

        metadata = analyzer.repo_metadata()
        print("✅ METADATA DONE")
        print("✅ METADATA DONE")
        print("METADATA TYPE:", type(metadata))
        print("METADATA VALUE:", metadata)

        project_name = analyzer.project_name()



        print(
            "✅ STRUCTURE DONE:",
            len(structure)
        )



        # ==================================================
        # 3) AI summaries
        # ==================================================

        log(
            "INFO",
            "Génération des résumés IA..."
        )


        ollama = OllamaClient()


        file_summaries = {}

        summaries = []



        for path, full_path, content in analyzer.iter_text_files():

            try:

                summary = ollama.summarize_file(
                    filepath=path,
                    content=content
                )


                file_summaries[path] ={
                    "summary": summary,
                    "content": content,
                    "line_count": len(content.splitlines()),
                    

                }

                summaries.append(summary)


            except Exception as e:

                file_summaries[path] = (
                    "Résumé indisponible"
                )



        ai_summary = "\n\n".join(
            summaries
        )



        # ==================================================
        # 4) Architecture detection
        # ==================================================

        log(
            "INFO",
            "Détection architecture..."
        )


        #
        # IMPORTANT:
        # Version actuelle de architecture_analyzer.py
        # utilise un seul paramètre
        #

        architecture_result = detect_architecture(
            structure
        )



        architecture = (
            architecture_result.get("type")
            or architecture_result.get("architecture")
            or architecture_result.get("detected_architecture")
            or "Unknown"
            )


        ranking = architecture_result.get(
            "full_ranking",
            []
        )


        architecture_score = None


        if ranking:

            architecture_score = ranking[0].get(
                "raw_score"
            )


        aarchitecture_confidence = (
            architecture_result.get("confidence_pct")
            or architecture_result.get("confidence")
            or 0
            )


        # ==================================================
        # 5) Documentation generation
        # ==================================================

        log(
            "INFO",
            "Création documentation..."
        )


        output_dir = os.path.join(
            "generated_docs",
            project_name
        )



        builder = DocBuilder(
            project_name,
            output_dir
        )



        readme_content = builder.build_readme(

            intro=ai_summary,

            metadata=metadata,

            structure=structure,

            folder_summaries=file_summaries

        )



        builder.build_index_page(

            intro=ai_summary,

            metadata=metadata

        )
        # Page documentation technique complète
        builder.build_documentation_page(
            ai_summary=ai_summary,
            files=file_summaries,
            architecture=architecture_explanation,
            technical_content=documentation_ai_content,
            )



        #
        # build_architecture_page attend un dictionnaire
        # de descriptions dossiers
        #

        builder.build_architecture_page(

            {
                architecture_result
            }

        )



        builder.build_detection_page(

            architecture_result,

            ai_summary

        )



        file_path = os.path.join(
            output_dir,
            "README.md"
        )



        log(
            "INFO",
            "Documentation générée avec succès."
        )



        return {


            "readme_content":
                readme_content,


            "file_path":
                file_path,


            "architecture":
                architecture,


            "architecture_score":
                architecture_score,


            "architecture_confidence":
                architecture_confidence,


            "ai_summary":
                ai_summary,


            "structure":
                structure,


            "metadata":
                metadata

        }



    except Exception as e:

        print("❌ PIPELINE ERROR:", str(e))

        raise DocumentationPipelineError(
            str(e)
        )