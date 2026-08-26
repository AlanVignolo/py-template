from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Application settings."""
    model_config = SettingsConfigDict(env_file=".env", env_prefix="APP_")
    
    data_dir: Path = Path("data")
    batch_size: int = 32
    api_key: str | None = None
    debug: bool = False

settings = Settings()