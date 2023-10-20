from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "PPInt API"
    debug: bool = True
    file_root: str = "/home/mkhokhar21/Documents/COSBI/POC/ppint-api/"

settings = Settings()
