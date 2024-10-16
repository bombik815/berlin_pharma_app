from pydantic import BaseModel
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

""" Класс настройки запуска app"""


class RunConfig(BaseModel):
    host: str = "0.0.0.0"  # "127.0.0.1"  # адрес сервера
    port: int = 8000  # порт сервера


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"  # префикс запросов для версии API v1
    registration_certificates: str = "/registration_certificates"


class ApiPrefix(BaseModel):
    prefix: str = "/api"  # префикс запросов
    v1: ApiV1Prefix = ApiV1Prefix()  # префикс запросов для версии API v1


""" Настройки подключение к БД """


class DatabaseConfig(BaseModel):
    url: PostgresDsn  # ссылка подключение к БД
    echo: bool = False
    echo_pool: bool = False
    max_overflow: int = 50
    pool_size: int = 10


""" Файл для всех настроеек приложения  """


class Settings(BaseSettings):
    # настройки модели
    model_config = SettingsConfigDict(
        env_file=".env",  # путь к файлу с переменными окружения
        case_sensitive=False,  # регистр в именах моделей
        env_nested_delimiter="__",  # разделитель в именах моделей
        env_prefix="APP_CONFIG__",  # префикс для переменных окружения
    )
    run: RunConfig = RunConfig()  # вызов настройки запуска приложения
    api: ApiPrefix = ApiPrefix()  # префикс запросов
    db: DatabaseConfig  # настройки подключения к БД


settings = Settings()
