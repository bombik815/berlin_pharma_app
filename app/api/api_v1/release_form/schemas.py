from pydantic import BaseModel, ConfigDict
from uuid import UUID


class ReleaseFormBase(BaseModel):
    primary_packaging: str
    count_primary_packaging: int
    gtin: str
    id_drug_name: str
    registration_certificate_id: UUID


class ReleaseFormCreate(ReleaseFormBase):
    pass


class ReleaseFormUpdate(ReleaseFormBase):
    pass


class ReleaseFormPatch(BaseModel):
    primary_packaging: str | None = None
    count_primary_packaging: int | None = None
    gtin: str | None = None
    id_drug_name: str | None = None
    registration_certificate_id: UUID | None = None


class ReleaseForm(ReleaseFormBase):
    id: UUID

    model_config = ConfigDict(from_attributes=True)
