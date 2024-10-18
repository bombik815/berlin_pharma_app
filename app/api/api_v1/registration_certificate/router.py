from typing import Annotated
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
)

router = APIRouter(tags=["Регистрационные удостоверения"])


@router.get("/", summary="Получить все Регистрационные удостоверения")
async def get_registration_certificates(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
):
    return await certificateDAO.get_all_registration_certificates(session=session)


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


#     return result
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


# @router.patch(
#     "/{certificate_id}/",
#     summary="Частичное обновление Регистрационного удостоверения",
# )
# async def update_registration_certificate_partial(
#     certificate_update: SRegistrationCertificatePartial,
#     session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
#     certificate: SRegistrationCertificate = Depends(registration_certificate_by_id),
# ):
#     # Обновление сертификата в базе данных
#     return await certificateDAO.update_registration_certificate_new(
#         session=session,
#         certificate=certificate,
#         certificate_update=certificate_update,
#         partial=True,
#     )


@router.delete(
    "/{certificate_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удалить Регистрационное удостоверение",
)
async def delete_registration_certificate(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    certificate: SRegistrationCertificate = Depends(registration_certificate_by_id),
):
    # Удаление сертификата из базы данных
    try:
        await certificateDAO.delete_registration_certificate(
            session=session, certificate=certificate
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
