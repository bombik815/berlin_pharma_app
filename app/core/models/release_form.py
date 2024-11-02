from sqlalchemy import String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship
import uuid
from sqlalchemy.dialects.postgresql import UUID
from .base import Base


class ReleaseForm(Base):
    __tablename__ = "release_forms"

    primary_packaging: Mapped[str] = mapped_column(String(255), nullable=False)
    count_primary_packaging: Mapped[int] = mapped_column(Integer, nullable=False)
    gtin: Mapped[str] = mapped_column(String(255), nullable=False)
    id_drug_name: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    registration_certificate_id: Mapped[uuid.UUID] = mapped_column(
        UUID, ForeignKey("registration_certificates.id")
    )

    registration_certificate = relationship(
        "RegistrationCertificate", back_populates="release_forms"
    )

    def __repr__(self):
        return f"ReleaseForm(id={self.id}, primary_packaging={self.primary_packaging}, gtin={self.gtin})"
