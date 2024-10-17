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

from .schemas import (
    SRegistrationCertificate,
    SRegistrationCertificateUpdate,
    SRegistrationCertificateCreate,
)

router = APIRouter(tags=["Регистрационные удостоверения"])


@router.get("/", summary="Получить все Регистрационные удостоверения")
async def get_registration_certificates(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
):
    return await certificateDAO.get_all_registration_certificates(session=session)


@router.post(
    "/add/",
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


# @router.put("/{certificate_id}/", summary="Обновить Регистрационное удостоверение")
# async def update_registration_certificate(
#     session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
#     certificate_update: SRegistrationCertificateUpdate,
#     certificate: SRegistrationCertificate = Depends(
#         certificateDAO.get_registration_certificate_by_id
#     ),
# ):
#     result = await certificateDAO.update_registration_certificate(
#         session=session,
#         certificate=certificate,
#         certificate_update=certificate_update,
#     )
#     return result
