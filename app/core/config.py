from pydantic import BaseModel
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings

''' Класс настройки запуска app'''
class RunConfig(BaseModel):
    host: str = '127.0.0.1' # адрес сервера
    port: int = 8000        # порт сервера


class ApiPrefix(BaseModel):
    prefix: str = '/api' # префикс запросов


''' Настройки подключение к БД '''
class DatabaseConfig(BaseModel):
    url: PostgresDsn  # ссылка подключение к БД
    echo: bool = False,
    echo_pool: bool = False,
    max_overflow:int = 50,
    pool_size: int = 10

''' Файл для всех настроеек приложения  '''
class Settings(BaseSettings):
    run: RunConfig = RunConfig() # вызов настройки запуска приложения
    api: ApiPrefix = ApiPrefix() # префикс запросов
    db: DatabaseConfig           # настройки подключения к БД


settings = Settings()