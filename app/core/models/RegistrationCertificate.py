from datetime import datetime

from sqlalchemy import String, DateTime
from sqlalchemy.orm import mapped_column, Mapped

from .base import Base


class RegistrationCertificate(Base):

    trade_Name: Mapped[str] = mapped_column(String, nullable=False)
    reg_Cert_Number: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    createAt_Reg_Cer: Mapped[datetime] = mapped_column(DateTime, nullable=False)
