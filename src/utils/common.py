import json
from base64 import b64decode, b64encode
from pathlib import Path
from typing import Any

import joblib
import yaml
from box import ConfigBox
from box.exceptions import BoxValueError

# type checking decorator to ensure function annotations are correct
# type checking is done at runtime, which can help catch errors early in development but may introduce some overhead in production. Use judiciously.
from ensure import ensure_annotations

from src import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read a YAML file and return its contents as a ConfigBox.

    Args:
        path_to_yaml: Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.

    Returns:
        ConfigBox: Parsed YAML contents.
    """
    try:
        with path_to_yaml.open(encoding="utf-8") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info("YAML file loaded successfully: %s", path_to_yaml)
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty") from None


@ensure_annotations
def create_directories(path_to_directories: list[Path], verbose: bool = True) -> None:
    """Create a list of directories."""
    for path in path_to_directories:
        path.mkdir(parents=True, exist_ok=True)
        if verbose:
            logger.info("Created directory: %s", path)


@ensure_annotations
def save_json(path: Path, data: dict[str, Any]) -> None:
    """Save JSON data to a file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    logger.info("JSON file saved: %s", path)


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Load JSON data as a ConfigBox.

    Args:
        path: Path to the JSON file.

    Returns:
        ConfigBox: JSON data exposed as attributes.
    """
    with path.open(encoding="utf-8") as file:
        content = json.load(file)

    logger.info("JSON file loaded: %s", path)
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    """Save an object as a binary file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(value=data, filename=path)
    logger.info("Binary file saved: %s", path)


@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load an object from a binary file.

    Args:
        path: Path to the binary file.

    Returns:
        Any: Object stored in the file.
    """
    data = joblib.load(path)
    logger.info("Binary file loaded: %s", path)
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """Return a file size formatted in kilobytes."""
    size_in_kb = round(path.stat().st_size / 1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring: str | bytes, fileName: Path) -> None:
    """Decode base64 image data and write it to a file."""
    fileName.parent.mkdir(parents=True, exist_ok=True)
    fileName.write_bytes(b64decode(imgstring))


def encodeImageIntoBase64(croppedImagePath: Path) -> bytes:
    """Read an image and return its base64-encoded bytes."""
    return b64encode(croppedImagePath.read_bytes())
