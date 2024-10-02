from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from core.config import settings

''' Создание асинхронный движок БД'''


class DatabaseHelper:
    def __init__(self,
                 url: str,
                 echo: bool = False,
                 echo_pool: bool = False,
                 max_overflow: int = 10,
                 pool_size: int = 5,
                 ):
        # Создание движка БД для работы с БД
        self.engine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            max_overflow=max_overflow,
            pool_size=pool_size,
        )
        # Создание фабрику сессии для работы с БД
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False)

    # Завершение движка БД
    async def dispose(self):
        await self.engine.dispose()  # Очистка асинхронного движка

    # Асинхронный получатель сессии
    async def session_getter(self):
        async with self.session_factory() as session:  # Получение сессии из фабрики
            yield session


# Создание объекта для работы с БД
db_helper = DatabaseHelper(
    url=str(settings.db.url),
    echo=settings.db.echo,
    echo_pool=settings.db.echo_pool,
    max_overflow=settings.db.max_overflow,
    pool_size=settings.db.pool_size,
)
