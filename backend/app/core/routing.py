from fastapi import APIRouter
from backend.app.api.v1 import router as api_v1_router
from backend.app.core.config import settings


def get_api_router() -> APIRouter:
    api_router = APIRouter()
    api_router.include_router(api_v1_router, prefix=settings.api_v1_prefix)
    return api_router


