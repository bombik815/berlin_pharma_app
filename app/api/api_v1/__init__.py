from fastapi import APIRouter

from core.config import settings

from .registration_certificate.router import router as registration_certificate_router


router = APIRouter(
    prefix=settings.api.v1.prefix,
)


router.include_router(
    registration_certificate_router,
    prefix=settings.api.v1.registration_certificates,
)
