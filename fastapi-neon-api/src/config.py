import os

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "your_default_database_url")
    API_TITLE = os.getenv("API_TITLE", "FastAPI Neon API")
    API_VERSION = os.getenv("API_VERSION", "1.0.0")
    DEBUG = os.getenv("DEBUG", "false").lower() in ("true", "1", "t")