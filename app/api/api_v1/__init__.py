from fastapi import APIRouter

from core.config import settings

from .registration_certificate.router import router as registration_certificate_router
from .release_form.router import router as release_form_router


router = APIRouter(
    prefix=settings.api.v1.prefix,
)


router.include_router(
    registration_certificate_router,
    prefix=settings.api.v1.registration_certificates,
)
router.include_router(
    release_form_router,
    prefix=settings.api.v1.release_form,
)
