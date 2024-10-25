from typing import Annotated, Optional, Dict, List
from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.ext.asyncio import AsyncSession


from core.models import db_helper

from .dao import RegistrationCertificateDAO as certificateDAO
from .dependencies import registration_certificate_by_id

from .schemas import (
    SRegistrationCertificate,
    SRegistrationCertificateUpdate,
    SRegistrationCertificateCreate,
    SRegistrationCertificateBase,
    SRegistrationCertificatePartial,
    RegistrationCertificatesResponse,
)

router = APIRouter(tags=["Регистрационные удостоверения"])


@router.get(
    "/",
    summary="Получить все Регистрационные удостоверения",
    response_model=RegistrationCertificatesResponse,
)
async def get_registration_certificates(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    is_active: Optional[bool] = None,
    limit: int = 10,
    skip: int = 0,
):
    total, certificates = await certificateDAO.get_all_registration_certificates(
        session=session, is_active=is_active, skip=skip, limit=limit
    )
    page = (skip // limit) + 1  # Определяем текущую страницу
    size = len(certificates)  # Кол-во записей на текущей странице

    if not certificates:
        # Если не найдено сертификатов и is_active определено, возвращаем 404
        if is_active is not None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No certificates found matching the active status.",
            )

    return RegistrationCertificatesResponse(
        total=total,
        # page=page,
        # size=size,
        data=certificates,
    )


@router.post(
    "/",
    response_model=SRegistrationCertificate,
    status_code=status.HTTP_201_CREATED,
    summary="Создать Регистрационное удостоверение",
)
async def create_registration_certificate(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    certificate_in: SRegistrationCertificateCreate,
):
    return await certificateDAO.add_registration_certificate(
        session=session,
        certificate_in=certificate_in,
    )


@router.get(
    "/{certificate_id}/", summary="Получить Регистрационное удостоверение по ID"
)
async def get_registration_certificate_by_id(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    certificate_id: UUID,
):
    result = await certificateDAO.get_registration_certificate_by_id(
        session=session, certificate_id=certificate_id
    )
    if result:
        return SRegistrationCertificate.from_orm(result)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Регистрационное удостоверение не найдено",
        )


@router.put(
    "/{certificate_id}/",
    response_model=SRegistrationCertificate,
    status_code=status.HTTP_200_OK,
    summary="Обновить Регистрационное удостоверение",
)
async def update_registration_certificate(
    certificate_id: UUID,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    certificate_update: SRegistrationCertificateBase,
):
    # Обновление сертификата в базе данных
    try:
        result = await certificateDAO.update_registration_certificate(
            session=session,
            certificate_id=certificate_id,
            certificate_update=certificate_update,
        )
        return result

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete(
    "/{certificate_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удалить Регистрационное удостоверение",
)
async def delete_registration_certificate(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    certificate: SRegistrationCertificate = Depends(registration_certificate_by_id),
):
    if certificate is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no certificate found",
        )
    # Удаление сертификата из базы данных
    try:
        await certificateDAO.delete_registration_certificate(
            session=session, certificate=certificate
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
