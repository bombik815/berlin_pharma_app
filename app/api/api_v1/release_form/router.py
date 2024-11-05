from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional, Annotated

import uuid

from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper

from .dao import ReleaseFormDAO
from .schemas import (
    ReleaseFormCreate,
    ReleaseForm as ReleaseFormSchema,
    ReleaseFormPatch,
)

router = APIRouter(tags=["Формы выпуска"])


@router.post(
    "/",
    summary="Создать новую форму выпуска",
    response_model=ReleaseFormSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_release_form(
    release_form: ReleaseFormCreate,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    """Создать новую форму выпуска"""
    result = await ReleaseFormDAO.create(session, release_form)
    return result


#
@router.get(
    "/",
    summary="Получить все формы выпуска",
    response_model=List[ReleaseFormSchema],
)
async def get_all_release_form(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    """Получите все формы выпуска с дополнительной фильтрацией"""
    result = await ReleaseFormDAO.get_all(session)
    return result


@router.get(
    "/{id}",
    summary="Получить форму выпуска по ID",
    response_model=ReleaseFormSchema,
)
async def get_by_id_release_form(
    id: uuid.UUID,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    """Получите конкретную форму выпуска по идентификатору"""
    release_form = await ReleaseFormDAO.get_by_id(session, id)
    if release_form is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Форма выпуска не найдена"
        )
    return release_form


@router.put(
    "/{id}",
    summary="Обновить  форму выпуска по ID",
    response_model=ReleaseFormSchema,
)
async def update_release_form(
    id: uuid.UUID,
    release_form: ReleaseFormPatch,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    """Частично обновить форму выпуска"""
    updated_release_form_partial = await ReleaseFormDAO.patch(session, id, release_form)
    if updated_release_form_partial is None:
        raise HTTPException(status_code=404, detail="Форма выпуска не найдена")
    return updated_release_form_partial
