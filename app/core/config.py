from pydantic import BaseModel
from pydantic_settings import BaseSettings

''' Класс настройки запуска app'''
class RunConfig(BaseModel):
    host: str = '127.0.0.1' # адрес сервера
    port: int = 8000        # порт сервера


class ApiPrefix(BaseModel):
    prefix: str = '/api' # префикс запросов


''' Файл для всех настроеек приложения  '''
class Settings(BaseSettings):
    run: RunConfig = RunConfig() # вызов настройки запуска приложения
    api: ApiPrefix = ApiPrefix() # префикс запросов

settings = Settings()