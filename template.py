import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(message)s",
)

logger = logging.getLogger(__name__)

project_root = Path.cwd()

list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/utils/__init__.py",
    "src/config/__init__.py",
    "src/config/configuration.py",
    "src/pipeline/__init__.py",
    "src/entity/__init__.py",
    "src/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]

for file_path in list_of_files:
    filepath = project_root / file_path
    filepath.parent.mkdir(parents=True, exist_ok=True)

    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()
        logger.info("Created empty file: %s", filepath)
    else:
        logger.info("File already exists: %s", filepath)
