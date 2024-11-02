from datetime import datetime
from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class SRegistrationCertificateBase(BaseModel):
    trade_Name: str
    reg_Cert_Number: str
    createAt_Reg_Cer: datetime = Field(
        ..., alias="createAt_Reg_Cer"
    )  # Используем 'alias' только если необходимо
    is_Active: bool = None

    model_config = ConfigDict(from_attributes=True)


class SRegistrationCertificateCreate(SRegistrationCertificateBase):
    model_config = ConfigDict(from_attributes=True)


class SRegistrationCertificateUpdate(SRegistrationCertificateBase):
    pass


class SRegistrationCertificatePartial(SRegistrationCertificateBase):

    trade_Name: str | None = None
    reg_Cert_Number: str | None = None
    createAt_Reg_Cer: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


class SRegistrationCertificate(SRegistrationCertificateBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID


class RegistrationCertificatesResponse(BaseModel):
    total: int
    data: List[SRegistrationCertificate]

    model_config = ConfigDict(from_attributes=True)
