import ast
import os


SUPPORTED_EXTENSIONS = {
    ".py"
}


class CodeAnalyzer:
    def is_binary_file(self, path):
        try:
            with open(path, "rb") as f:
                chunk = f.read(1024)

            return b"\x00" in chunk

        except Exception:
            return True

    def __init__(self, repo_path):
        self.repo_path = repo_path
    


    def analyze_file(self, file_path):

        extension = os.path.splitext(file_path)[1].lower()

        if extension not in SUPPORTED_EXTENSIONS:
            return self.basic_info(file_path)


        full_path = os.path.join(
            self.repo_path,
            file_path
        )

        try:
            if self.is_binary_file(full_path):
                print("SKIP BINARY:", full_path)
                return self.basic_info(file_path)
            with open(
                full_path,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as f:
                content = f.read()

            tree = ast.parse(content)

        except Exception:
            return self.basic_info(file_path)


        classes = []
        functions = []
        imports = []


        for node in ast.walk(tree):

            if isinstance(node, ast.ClassDef):

                classes.append({
                    "name": node.name,
                    "line": node.lineno
                })


            elif isinstance(node, ast.FunctionDef):

                functions.append({
                    "name": node.name,
                    "line": node.lineno,
                    "parameters": [
                        arg.arg
                        for arg in node.args.args
                    ]
                })


            elif isinstance(node, ast.Import):

                for alias in node.names:
                    imports.append(alias.name)


            elif isinstance(node, ast.ImportFrom):

                if node.module:
                    imports.append(node.module)


        return {

            "file": file_path,

            "language": "Python",

            "classes": classes,

            "functions": functions,

            "imports": imports,

            "lines": len(content.splitlines())

        }



    def basic_info(self, file_path):

        return {

            "file": file_path,

            "language":
                os.path.splitext(file_path)[1],

            "classes": [],

            "functions": [],

            "imports": []

        }



    def analyze_repository(self, files):

        result = []

        for file in files:

            if file["type"] != "file":
                continue

            result.append(
                self.analyze_file(
                    file["path"]
                )
            )


        return result