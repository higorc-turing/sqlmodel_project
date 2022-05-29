from pydantic import BaseSettings, SecretStr


class EnvironmentVariables(BaseSettings):
    CDS_MYSQL_ADDRESS: str
    CDS_MYSQL_USER: str
    CDS_MYSQL_DATABASE: str
    CDS_MYSQL_PASSWORD: SecretStr
    CDS_MYSQL_PORT: SecretStr

    class Config:
        env_file = '.env'

ENV_VARS = EnvironmentVariables()  # type: ignore
