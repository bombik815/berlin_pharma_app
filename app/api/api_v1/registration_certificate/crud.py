from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import RegistrationCertificate


"""
Retrieve all registration certificates from the database.

Args:
    session (AsyncSession): The asynchronous session to interact with the database.

Returns:
    Sequence[RegistrationCertificate]: A sequence of RegistrationCertificate objects representing all retrieved certificates.
"""


async def get_registration_certificates(
    session: AsyncSession,
) -> Sequence[RegistrationCertificate]:
    # Создаем запрос для получения всех сертификатов
    stmt = select(RegistrationCertificate).order_by(RegistrationCertificate.id)
    # Выполняем запрос и получаем результаты
    result = await session.execute(stmt)
    # извлекаем записи как объекты модели и возвращаем их
    return result.scalars().all()


"""
Retrieve a registration certificate by its unique registration certificate number.

Args:
    session (AsyncSession): The asynchronous session to interact with the database.
    reg_Cert_Number (str): The unique registration certificate number to search for.

Returns:
    RegistrationCertificate | None: The registration certificate if found, else None.
"""


async def get_registration_certificate_by_id(
    session: AsyncSession,
    certificate_id: int,
) -> RegistrationCertificate | None:
    query = select(RegistrationCertificate).where(
        RegistrationCertificate.id == certificate_id
    )
    result = await session.execute(query)
    return result.scalar_one_or_none()
