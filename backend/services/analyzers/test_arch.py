from architecture_analyzer import detect_architecture
structure = {
    "dirs": {
        "controllers": {
            "dirs": {},
            "files": [
                "user_controller.py"
            ]
        },
        "services": {
            "dirs": {},
            "files": [
                "user_service.py"
            ]
        },
        "repositories": {
            "dirs": {},
            "files": [
                "user_repository.py"
            ]
        }
    },
    "files": []
}


result = detect_architecture(structure)

print(result)