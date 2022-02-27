import os
from dotenv import load_dotenv


load_dotenv()


def get_env_str(key: str, default: str) -> str:
    value = os.getenv(key)
    return value if value is not None else default


def get_env_int(key: str, default: int) -> int:
    value = os.getenv(key)
    try:
        return int(value) if value is not None else default
    except ValueError:
        return default


EDGE_DEVICE_ID = get_env_str("EDGE_DEVICE_ID", "bin-dev")
BACKEND_BASE_URL = get_env_str("BACKEND_BASE_URL", "http://localhost:8000")
BACKEND_API_KEY = get_env_str("BACKEND_API_KEY", "devkey")

CAMERA_WIDTH = get_env_int("CAMERA_WIDTH", 640)
CAMERA_HEIGHT = get_env_int("CAMERA_HEIGHT", 480)
CAPTURE_INTERVAL_SEC = get_env_int("CAPTURE_INTERVAL_SEC", 5)

MODEL_PATH = get_env_str("MODEL_PATH", "./edge/inference/models/waste_det.onnx")
MODEL_BACKEND = get_env_str("MODEL_BACKEND", "onnx")



# tweak 6 at 2025-09-24 20:37:38

# tweak 25 at 2025-09-24 20:37:46

# tweak 44 at 2025-09-24 20:37:55

