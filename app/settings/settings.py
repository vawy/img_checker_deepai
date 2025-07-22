import os

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEEPAI_API_KEY: str
    DEEPAI_GENERATE_IMG_URL: str

    model_config = ConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"),
        env_file_encoding="utf-8"
    )
