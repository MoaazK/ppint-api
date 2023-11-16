from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "PPInt API"
    debug: bool = True
    file_root: str = "/abolute-path-to-current(root)-folder/"

settings = Settings()
