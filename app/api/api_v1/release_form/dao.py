from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from starlette import status

from core.models import ReleaseForm
from .schemas import ReleaseFormCreate, ReleaseFormUpdate, ReleaseFormPatch
from typing import List, Optional
import uuid


class ReleaseFormDAO:
    @classmethod
    async def create(
        cls, session: AsyncSession, release_form: ReleaseFormCreate
    ) -> ReleaseForm:
        # Проверьте, существует ли уже запись с таким GTIN
        stmt = select(ReleaseForm).where(ReleaseForm.gtin == release_form.gtin)
        result = await session.execute(stmt)
        existing_form = result.scalar_one_or_none()

        if existing_form:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Форма выпуска с этим GTIN уже существует.",
            )

        db_release_form = ReleaseForm(**release_form.dict())
        session.add(db_release_form)
        await session.commit()
        await session.refresh(db_release_form)
        return db_release_form

    @classmethod
    async def get_all(
        cls,
        session: AsyncSession,
    ) -> List[ReleaseForm]:
        stmt = select(ReleaseForm)
        result = await session.execute(stmt)
        return list(result.scalars())

    @classmethod
    async def get_by_id(
        cls, session: AsyncSession, release_form_id: uuid.UUID
    ) -> Optional[ReleaseForm]:
        stmt = select(ReleaseForm).where(ReleaseForm.id == release_form_id)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()

    @classmethod
    async def patch(
        cls,
        session: AsyncSession,
        release_form_id: uuid.UUID,
        release_form_data: ReleaseFormPatch,
    ) -> Optional[ReleaseForm]:
        stmt = select(ReleaseForm).where(ReleaseForm.id == release_form_id)
        result = await session.execute(stmt)
        db_release_form = result.scalar_one_or_none()

        if db_release_form:
            for key, value in release_form_data.dict(exclude_unset=True).items():
                setattr(db_release_form, key, value)
            await session.commit()
            await session.refresh(db_release_form)
        return db_release_form
