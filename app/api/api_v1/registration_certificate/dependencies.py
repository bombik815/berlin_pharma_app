from typing import Annotated
from uuid import UUID

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.models import RegistrationCertificate

from .dao import RegistrationCertificateDAO as crud


"""
Retrieve a registration certificate by its unique registration certificate number.

Args:
    reg_Cert_Number (Annotated[str, Path]): The unique registration certificate number to search for.
    session (AsyncSession, optional): The asynchronous session to interact with the database. Defaults to using the session getter from db_helper.

Returns:
    RegistrationCertificate: The registration certificate if found.

Raises:
    HTTPException: If the registration certificate is not found, raises HTTP 404 Not Found.
"""


async def registration_certificate_by_id(
    certificate_id: Annotated[UUID, Path],
    session: AsyncSession = Depends(db_helper.session_getter),
) -> RegistrationCertificate:

    certificate = await crud.get_registration_certificate_by_id(
        session=session,
        certificate_id=certificate_id,
    )

    if certificate is not None:
        return certificate

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Registration certificate #{certificate_id} not found",
    )
