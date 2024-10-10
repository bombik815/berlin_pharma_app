from sqlalchemy import MetaData
from sqlalchemy.orm import declared_attr

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from utils import camel_case_to_snake_case


# Базовая модель для всех моделей
class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{camel_case_to_snake_case(cls.__name__)}s"
