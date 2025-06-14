from fastapi import FastAPI

from src.infrastructure.di.dependencies import init_dependencies
from src.presentation.v1.error_handlers import init_exc_handlers
from src.presentation.v1.router import api_router as api_router_v1


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(api_router_v1, prefix='/api/v1')
    init_dependencies(app)
    init_exc_handlers(app)

    return app
