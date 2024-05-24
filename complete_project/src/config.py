from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Complete Project"
    PROJECT_VERSION: str = "0.1.0"
    # Dont write SECRET_KEY here in production
    SECRET_KEY: str = "fda947bd4b857683646d65967c5365f0ddd52d29dd827f85acc7e782c8f6e2e4"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()