from pydantic import BaseModel
import os


class Settings(BaseModel):
    api_v1_prefix: str = "/api/v1"
    api_key: str = os.getenv("BACKEND_API_KEY", "devkey")


settings = Settings()



# tweak 13 at 2025-09-24 20:37:40

# tweak 32 at 2025-09-24 20:37:49







