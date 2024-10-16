from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.models import db_helper
from .crud import get_registration_certificates as get_all_certifications
from .dependencies import registration_certificate_by_id
from .schemas import SRegistrationCertificate

router = APIRouter(tags=["Регистрационные удостоверения"])


@router.get(
    "/",
    response_model=list[SRegistrationCertificate],
    summary="Получить все Регистрационные удостоверения",
)
async def get_registration_certificates(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    certifications = await get_all_certifications(session=session)
    return certifications


@router.get(
    "/{certificate_id}/",
    response_model=SRegistrationCertificate,
    summary="Получить Регистрационное удостоверение по ID",
)
async def get_registration_certificate(
    registration_certificate: SRegistrationCertificate = Depends(
        registration_certificate_by_id
    ),
):
    return registration_certificate
