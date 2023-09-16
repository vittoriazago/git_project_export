
from pydantic import BaseSettings


class BaseConfig:
    env_file = ".env"
    env_cile_encoding = "utf-8"


class BasicApiModel(BaseSettings):
    base_url: str
    private_token: str


class GitlabApiSettings(BasicApiModel):
    version: str

    class Config(BaseConfig):
        env_prefix = "APP_GITLAB_API_"


gitlab_api_settings = GitlabApiSettings()