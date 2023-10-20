from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "PPInt API"
    debug: bool = True
    file_root: str = "/path-to-ppint-api-root-folder/"

settings = Settings()
