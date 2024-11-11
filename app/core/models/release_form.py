from typing import TYPE_CHECKING

from sqlalchemy import String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship
import uuid
from sqlalchemy.dialects.postgresql import UUID

from .base import Base

if TYPE_CHECKING:
    from .registration_certificate import RegistrationCertificate


class ReleaseForm(Base):

    primary_packaging: Mapped[str] = mapped_column(String(255), nullable=False)
    count_primary_packaging: Mapped[int] = mapped_column(Integer, nullable=False)
    gtin: Mapped[str] = mapped_column(String(255), nullable=False)
    id_drug_name: Mapped[str] = mapped_column(String(255), nullable=False)
    registration_certificate_id: Mapped[uuid.UUID] = mapped_column(
        UUID, ForeignKey("registration_certificates.id"), nullable=False
    )

    registration_certificate: Mapped["RegistrationCertificate"] = relationship(
        "RegistrationCertificate", back_populates="release_forms"
    )

    def __repr__(self):
        return f"{self.id_drug_name}, {self.primary_packaging}, {self.count_primary_packaging})"
