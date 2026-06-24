import os

from dotenv import load_dotenv

load_dotenv()


def is_mock_mode() -> bool:
    return os.getenv("SIGMA_MOCK_MODE", "true").strip().lower() in ("true", "1", "yes")
