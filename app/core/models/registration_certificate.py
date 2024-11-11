from datetime import datetime
from typing import List, TYPE_CHECKING

from sqlalchemy import String, DateTime, Boolean
from sqlalchemy.orm import mapped_column, Mapped, relationship

from utils.date_converter import format_date
from .base import Base

if TYPE_CHECKING:
    from .release_form import ReleaseForm


class RegistrationCertificate(Base):

    trade_Name: Mapped[str] = mapped_column(
        String, nullable=False, info={"description": "Наименование товара"}
    )
    reg_Cert_Number: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False,
        info={"description": "Номер свидетельства о регистрации"},
    )
    createAt_Reg_Cer: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    is_Active: Mapped[bool] = mapped_column(
        Boolean, default=True, info={"description": "Активность записи"}
    )

    release_forms: Mapped[List["ReleaseForm"]] = relationship(
        "ReleaseForm",
        back_populates="registration_certificate",
    )

    def __repr__(self) -> str:
        return f"{self.trade_Name}, {self.reg_Cert_Number}, {format_date(self.createAt_Reg_Cer)}"
