from datetime import datetime
from typing import Sequence, Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from api.api_v1.registration_certificate.schemas import (
    SRegistrationCertificateCreate,
    SRegistrationCertificateUpdate,
    SRegistrationCertificatePartial,
    SRegistrationCertificate,
    SRegistrationCertificateBase,
)
from core.dao.base import BaseDAO
from core.models import RegistrationCertificate


class RegistrationCertificateDAO(BaseDAO):
    model = RegistrationCertificate

    @classmethod
    async def get_all_registration_certificates(cls, session: AsyncSession):
        # Создаем запрос для получения всех сертификатов
        query = select(cls.model).order_by(cls.model.id)
        # Выполняем запрос и получаем результаты
        result = await session.execute(query)
        # извлекаем записи как объекты модели и возвращаем их
        return result.scalars().all()

    @classmethod
    async def get_registration_certificate_by_id(
        cls,
        session: AsyncSession,
        certificate_id: UUID,
    ):
        query = select(cls.model).filter_by(id=certificate_id)
        result = await session.execute(query)
        return result.scalar_one_or_none()

    @classmethod
    async def add_registration_certificate(
        cls, session: AsyncSession, certificate_in: SRegistrationCertificateCreate
    ) -> RegistrationCertificate:
        # Создаем новый объект модели сертификата
        new_certificate = RegistrationCertificate(**certificate_in.dict())
        session.add(new_certificate)
        await session.commit()
        await session.refresh(new_certificate)
        return new_certificate

    # @classmethod
    # async def update_registration_certificate(
    #     cls,
    #     session: AsyncSession,
    #     certificate_id: UUID,
    #     certificate_data: RegistrationCertificate,
    # ) -> Optional[SRegistrationCertificateUpdate]:
    #
    #     stmt = (
    #         update(RegistrationCertificate)
    #         .filter_by(id=certificate_id)
    #         .values(**certificate_data.dict())
    #     )
    #     await session.execute(stmt)
    #     await session.commit()
    #     return await cls.get_registration_certificate_by_id(certificate_id)
