from datetime import datetime

from sqlalchemy import String, DateTime, Boolean
from sqlalchemy.orm import mapped_column, Mapped

from .base import Base


class RegistrationCertificate(Base):

    trade_Name: Mapped[str] = mapped_column(String, nullable=False)
    reg_Cert_Number: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    createAt_Reg_Cer: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    is_Active: Mapped[bool] = mapped_column(Boolean, default=True)

    def __repr__(self) -> str:
        return f'<RegistrationCertificate(trade_Name="{self.trade_Name}", reg_Cert_Number="{self.reg_Cert_Number}")>'
