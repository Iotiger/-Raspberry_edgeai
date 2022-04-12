from fastapi import FastAPI
from backend.app.core.routing import get_api_router


def create_app() -> FastAPI:
    app = FastAPI(title="Smart Waste Backend")
    app.include_router(get_api_router())
    return app


app = create_app()



# tweak 11 at 2025-09-24 20:37:40

# tweak 30 at 2025-09-24 20:37:48

# tweak 49 at 2025-09-24 20:37:57




