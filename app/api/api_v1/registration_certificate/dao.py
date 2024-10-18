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
    # async def update_registration_certificate_new(
    #     cls,
    #     session: AsyncSession,
    #     certificate_update: (
    #         SRegistrationCertificateUpdate | SRegistrationCertificatePartial
    #     ),
    #     certificate: RegistrationCertificate,
    #     partial: bool = False,
    # ) -> RegistrationCertificate:
    #
    #     for name, value in certificate_update.dict(exclude_unset=partial).items():
    #         setattr(
    #             certificate_update, name, value
    #         )  # Обновляем атрибуты объекта certificate
    #         print(f"Обновлено поле {name=} значение {value=}")
    #
    #     await session.commit()
    #     # await session.refresh(certificate)  # Обновляем состояние объекта в БД
    #     print("Сохранено в БД данные")
    #
    #     return certificate

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

    # @classmethod
    # async def update_registration_certificate_partial(
    #     cls,
    #     session: AsyncSession,
    #     certificate_id: UUID,
    #     certificate_update: SRegistrationCertificatePartial,
    # ) -> RegistrationCertificate:
    #
    #     # Получаем существующий сертификат
    #     query = select(cls.model).filter_by(id=certificate_id)
    #     result = await session.execute(query)
    #     certificate = result.scalar_one_or_none()
    #
    #     if not certificate:
    #         raise Exception(f"Сертификат с ID {certificate_id} не найден")
    #
    #     # Обновить только те поля, которые указаны
    #     if certificate_update.trade_Name is not None:
    #         certificate.trade_name = certificate_update.trade_Name
    #
    #     if certificate_update.reg_Cert_Number is not None:
    #         certificate.reg_cert_number = certificate_update.reg_Cert_Number
    #
    #     if certificate_update.createAt_Reg_Cer is not None:
    #         certificate.create_at_reg_cer = certificate_update.createAt_Reg_Cer
    #
    #     # Сохранить изменения
    #     await session.commit()
    #
    #     return certificate

    @classmethod
    async def delete_registration_certificate(
        cls, session: AsyncSession, certificate: SRegistrationCertificate
    ) -> None:
        await session.delete(certificate)
        await session.commit()
