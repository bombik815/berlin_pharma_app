from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SRegistrationCertificateBase(BaseModel):
    trade_Name: str
    reg_Cert_Number: str
    createAt_Reg_Cer: datetime

    model_config = ConfigDict(from_attributes=True)


class SRegistrationCertificateCreate(SRegistrationCertificateBase):
    pass


class SRegistrationCertificateUpdate(SRegistrationCertificateBase):
    pass


class SRegistrationCertificatePartial(SRegistrationCertificateBase):
    pass


class SRegistrationCertificate(SRegistrationCertificateBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
