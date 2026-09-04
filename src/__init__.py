import logging
from pathlib import Path

LOG_FORMAT = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "running_logs.log"

LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler()],
)

logger = logging.getLogger(__name__)
