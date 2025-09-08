from fastapi import APIRouter

from src.presentation.v1.views.user.router import router

api_router = APIRouter()

api_router.include_router(router)
