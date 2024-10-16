from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
import uvicorn
from starlette.middleware.cors import CORSMiddleware

from fastapi.middleware.cors import CORSMiddleware

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

main_app.include_router(api_router)  # , prefix=settings.api.prefix


# Подключение CORS, чтобы запросы к API могли приходить из браузера
origins = [
    # 3000 - порт, на котором работает фронтенд на React.js
    "http://127.0.0.1:5173",
    "http://localhost:5173",
    "http://192.168.0.101:5173",
]

main_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # Включаем возможность передачи cookie
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
