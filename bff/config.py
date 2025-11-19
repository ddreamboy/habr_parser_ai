import os
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class ELogLevel(str):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class Settings(BaseSettings):
    """
    Класс для хранения и валидации настроек приложения
    Загружает переменные из .env файла
    """

    PROXY_URL: str | None = None
    DEV_MODE: bool = False

    RABBITMQ_USER: str = "user"
    RABBITMQ_PASSWORD: str = "password"
    RABBITMQ_HOST: str = "rabbitmq"
    RABBITMQ_PORT: int = 5672

    ARTICLE_QUEUE_NAME: str = "article_queue"

    HABR_ADAPTER_BASE_URL: str = "http://habr-adapter:5000"
    LLM_SERVICE_BASE_URL: str = "http://llm-service:5001"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @property
    def RABBITMQ_URL(self) -> str:
        return f"amqp://{self.RABBITMQ_USER}:{self.RABBITMQ_PASSWORD}@{self.RABBITMQ_HOST}:{self.RABBITMQ_PORT}/"

    @property
    def CONSOLE_LOG_LEVEL(self):
        return ELogLevel.DEBUG if self.DEV_MODE else ELogLevel.WARNING

    @property
    def BASE_DIR(self):
        return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    @property
    def LOGS_DIR(self):
        return os.path.join(self.BASE_DIR, "logs")


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
