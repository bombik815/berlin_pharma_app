from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
import uvicorn

from core.config import settings

from api import router as api_router
from core.models import db_helper


@asynccontextmanager
async def lifespan(app):
    # startup
    print("Starting up database...")
    yield
    # shutdown
    print("Shutting down database...")
    await db_helper.dispose()


main_app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

main_app.include_router(api_router, prefix=settings.api.prefix)


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
