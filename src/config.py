import os
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    MMLFLOW_TRACKING_URI: Optional[str]
    MLFLOW_TRACKING_USERNAME: Optional[str]
    MLFLOW_TRACKING_PASSWORD: Optional[str]
    AWS_ACCESS_KEY_ID: Optional[str]
    AWS_SECRET_ACCESS_KEY: Optional[str]


_default_prefix = "" if os.path.exists("env/.env") else "local"
_ENV_PREFIX = os.environ.get("ENV_PREFIX") if os.environ.get("ENV_PREFIX") else _default_prefix
_env_file = f"env/{_ENV_PREFIX}.env"
settings = Settings(_env_file=f"{_env_file}", _env_file_encoding="utf-8")
