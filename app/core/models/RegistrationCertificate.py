from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from .base import Base


class RegistrationCertificate(Base):

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    trade_Name: Mapped[str] = mapped_column(String, nullable=False)
    reg_Cert_Number: Mapped[str] = mapped_column(String, nullable=False)
    createAt_Reg_Cer: Mapped[datetime] = mapped_column(String, nullable=False)
