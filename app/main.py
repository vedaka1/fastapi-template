from fastapi import FastAPI
from src.infrastructure.di.dependencies import init_dependencies
from src.presentation.v1.error_handlers import init_exc_handlers
from src.presentation.v1.router import api_router as api_router_v1


def create_app() -> FastAPI:
    app = FastAPI()

    api_v1 = FastAPI()
    api_v1.include_router(api_router_v1)

    init_dependencies(api_v1)
    init_exc_handlers(api_v1)

    app.mount('/api/v1', api_v1)

    return app
