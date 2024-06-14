import os
from pathlib import Path

project_name = "us_visa_prediction"

list_of_files = [

    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/train_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "demo.py",
    "setup.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "config/model.yaml",
    "config/schema.yaml"
]


def create_project_structure(files: list) -> None:

    for filepath in files:
        filepath = Path(filepath)  

        # Split the path into directory and filename components
        filedir, filename = os.path.split(filepath)

        if filedir != "":  # Check if there are parent directories to create
            os.makedirs(filedir, exist_ok=True)  

        # Check if the file doesn't exist or is empty (0 bytes)
        if not filepath.is_file() or filepath.stat().st_size == 0: 
            filepath.touch()  # Create an empty file
        else:
            print(f"File already exists: {filepath}")


create_project_structure(list_of_files)
