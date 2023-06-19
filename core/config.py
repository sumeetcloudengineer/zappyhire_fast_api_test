import os
from pathlib import Path
from pydantic import BaseSettings
from pydantic import AnyHttpUrl
from typing import List
import gc
from dotenv import load_dotenv

load_dotenv()

gc.collect()
BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    API_STR: str = '/api'
    """
    BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]
    """
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []


    class Config:
        env_file = ".env"


settings = Settings()
