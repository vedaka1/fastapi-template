from fastapi import APIRouter
from src.presentation.v1.views import user

api_router = APIRouter()

api_router.include_router(user.router)
