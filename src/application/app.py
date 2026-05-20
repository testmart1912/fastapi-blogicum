from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from application.api.posts import router as posts_router
from application.api.users import router as users_router
from application.api.locations import router as locations_router
from application.api.categories import router as categories_router
from application.api.comments import router as comments_router
from application.api.auth import router as auth_router
from application.core.logging_config import setup_logging
from application.core.config import settings


def create_app() -> FastAPI:
    setup_logging(
        log_file=settings.LOG_FILE,
        max_bytes=settings.LOG_MAX_BYTES,
        backup_count=settings.LOG_BACKUP_COUNT
    )

    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    app.include_router(auth_router, prefix='/api/v1', tags=['Auth'])
    app.include_router(posts_router, prefix='/api/v1', tags=['Posts'])
    app.include_router(users_router, prefix='/api/v1', tags=['Users'])
    app.include_router(locations_router, prefix='/api/v1', tags=['Locations'])
    app.include_router(categories_router, prefix='/api/v1', tags=['Categories'])
    app.include_router(comments_router, prefix='/api/v1', tags=['Comments'])
    return app


app = create_app()
