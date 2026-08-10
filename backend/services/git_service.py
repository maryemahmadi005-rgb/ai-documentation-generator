"""
git_service.py

Service responsable du clonage et nettoyage
des dépôts GitHub.
"""


import os
import stat
import shutil
import tempfile

from git import (
    Repo,
    GitCommandError,
    InvalidGitRepositoryError
)
IGNORED_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".ico",
    ".svg",
    ".pdf",
    ".zip",
    ".rar",
    ".exe",
    ".dll",
    ".class",
    ".pyc",
    ".mp3",
    ".mp4",
    ".woff",
    ".woff2",
    ".ttf"
}




# ==========================================================
# Exceptions
# ==========================================================

class GitCloneError(Exception):
    pass





# ==========================================================
# Remove readonly files
# ==========================================================

def _remove_readonly(
    func,
    path,
    excinfo
):

    try:

        os.chmod(
            path,
            stat.S_IWRITE
        )

        func(path)


    except Exception:

        pass






# ==========================================================
# Clone repository
# ==========================================================

def clone_repository(
    github_url: str,
    full_history=False
) -> str:


    if not github_url:

        raise GitCloneError(
            "URL GitHub vide."
        )



    if not github_url.startswith(
        (
            "http://",
            "https://",
            "git@"
        )
    ):

        raise GitCloneError(
            "URL GitHub invalide."
        )





    local_path = tempfile.mkdtemp(
        prefix="ai_doc_gen_"
    )




    try:
        if full_history:
            Repo.clone_from(
                github_url,
                local_path
            )
        else:
            Repo.clone_from(
                github_url,
                local_path,
                 depth=1

                 )
        print("CLONED PATH:", local_path)
        print(
            "HAS .GIT:",
            os.path.exists(os.path.join(local_path, ".git"))
            )



    except GitCommandError as e:



        shutil.rmtree(

            local_path,

            onerror=_remove_readonly

        )



        raise GitCloneError(

            f"Impossible de cloner le dépôt : {str(e)}"

        )




    except Exception as e:



        shutil.rmtree(

            local_path,

            onerror=_remove_readonly

        )



        raise GitCloneError(

            f"Erreur inattendue pendant le clonage : {str(e)}"

        )





    return local_path






# ==========================================================
# Verify repository
# ==========================================================

def is_git_repository(
    path: str
) -> bool:


    try:


        Repo(path)


        return True



    except InvalidGitRepositoryError:


        return False






# ==========================================================
# Cleanup repository
# ==========================================================

def cleanup_repository(
    local_path: str
):


    if not local_path:

        return




    if os.path.exists(
        local_path
    ):


        try:


            shutil.rmtree(

                local_path,

                onerror=_remove_readonly

            )



        except Exception as e:


            print(

                f"[WARNING] Cleanup impossible : {e}"

            )