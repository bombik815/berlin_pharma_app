from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from api.api_v1.registration_certificate.schemas import (
    SRegistrationCertificateCreate,
    SRegistrationCertificateUpdate,
)
from core.dao.base import BaseDAO
from core.models import RegistrationCertificate


class RegistrationCertificateDAO(BaseDAO):
    model = RegistrationCertificate

    @classmethod
    async def get_all_registration_certificates(
        cls,
        session: AsyncSession,
        is_active: bool = None,
        limit: int = 10,
        skip: int = 0,
    ):
        query = select(cls.model)
        if is_active is not None:
            query = query.filter(cls.model.is_Active == is_active)

        total_query = select(func.count()).select_from(
            cls.model
        )  # Подсчет общего количества записей
        total = await session.execute(total_query)
        total_count = total.scalar()  # Получите количество записей из результата
        result = await session.execute(query.offset(skip).limit(limit))
        certificates = result.scalars().all()  # Получить фактические записи
        return total_count, certificates

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

    @classmethod
    async def update_registration_certificate(
        cls,
        session: AsyncSession,
        certificate_id: UUID,
        certificate_update: SRegistrationCertificateUpdate,
    ) -> RegistrationCertificate:

        # Получаем существующий сертификат
        query = select(cls.model).filter_by(id=certificate_id)
        result = await session.execute(query)
        certificate_data = result.scalar_one_or_none()

        if not certificate_data:
            raise Exception(f"Сертификат с ID {certificate_id} не найден")

        # Обновляем поля
        for name, value in certificate_update.dict(exclude_unset=True).items():
            setattr(certificate_data, name, value)

        await session.commit()
        await session.refresh(
            certificate_data
        )  # Обновляем объект для получения актуального состояния из БД
        return certificate_data

    @classmethod
    async def delete_registration_certificate(
        cls, session: AsyncSession, certificate: RegistrationCertificate
    ):
        certificate.is_Active = False
        await session.commit()
        await session.refresh(certificate)
        return certificate
