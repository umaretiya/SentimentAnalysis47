import os
from pathlib import Path 
import logging


format = '[%(asctime)s]: %(filename)s : %(message)s :'

logging.basicConfig(level=logging.INFO, format=format)

project_name = "sentiment_analysis"
main_repo = "SentimentAnalysis47"

files_list = [
    # Files names
    ".gitignore",
    ".dvcignore", 
    ".dockerignore",
    "LICENSE",
    "dvc.yaml",
    "params.yaml",
    "Dockerfile",
    "setup.py",
    "setup.cfg",
    "init_setup.sh",
    "tox.ini",
    "pyproject.toml",
    "requirements.txt",
    "requirements_dev.txt",
    "README.md",
    # Directory names
    "configs/config.yaml",
    "study_data/part1.ipynb",
    "tests/unit/__init__.py",
    "tests/unit/unit_test.py",
    "tests/integration/__init__.py",
    "tests/integration/int_test.py",
    "tests/data/.gitkeep",
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/pipeline/__init__.py",
]

for filepath in files_list:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Projects Dirs created at: {filedir} & file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating a empty and new file : {filename}")
    else:
        logging.info(f"File already exists: {filename}")
            
    