from fastapi import FastAPI
from backend.app.core.routing import get_api_router


def create_app() -> FastAPI:
    app = FastAPI(title="Smart Waste Backend")
    app.include_router(get_api_router())
    return app


app = create_app()


