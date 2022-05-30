from pydantic import BaseSettings

class Globals(BaseSettings):
    LOGGER_NAME: str = 'Centralized Data Service'

GLOBALS = Globals()
