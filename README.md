# Smart Waste Management System (Raspberry Pi + Computer Vision)

A modular edge-to-cloud system for real-time waste bin monitoring, fill-level estimation, and route optimization. Built for Raspberry Pi devices with onboard camera and accelerated inference (CPU/Coral/NPU), with a FastAPI backend and optional mobile-facing API.

## Highlights
- Edge agent on Raspberry Pi: capture → detect/classify waste → estimate fill-level → publish telemetry
- Backend API: store bin status, analytics, and route suggestions
- Modular Python packages for clarity, testing, and scalability
- Secure configuration via `.env`/environment variables

## Repository Structure
```
Raspberry_edgeai/
├─ edge/
│  ├─ camera/
│  │  └─ camera_service.py
│  ├─ inference/
│  │  ├─ detector.py
│  │  └─ models/
│  ├─ fill_level/
│  │  └─ estimator.py
│  ├─ comms/
│  │  └─ publisher.py
│  ├─ app.py
│  └─ __init__.py
├─ backend/
│  ├─ app/
│  │  ├─ main.py
│  │  ├─ api/
│  │  │  └─ v1.py
│  │  ├─ core/
│  │  │  ├─ config.py
│  │  │  └─ routing.py
│  │  └─ models/
│  │     └─ dto.py
│  └─ __init__.py
├─ shared/
│  ├─ config.py
│  ├─ schemas.py
│  └─ __init__.py
├─ tests/
│  ├─ test_fill_level.py
│  └─ __init__.py
├─ requirements.txt
├─ .env.example
└─ README.md
```

## Quick Start

### 1) Prerequisites
- Python 3.10+
- Raspberry Pi OS (Bookworm recommended) for edge device
- For acceleration (optional): Coral TPU runtime or OpenVINO/ONNX Runtime

### 2) Install
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

### 3) Configure
Copy `.env.example` to `.env` and update values.

### 4) Run Edge Agent (on Pi)
```bash
python -m edge.app
```

### 5) Run Backend API (local dev)
```bash
uvicorn backend.app.main:app --reload --port 8000
```

## Edge Agent Overview
- `camera_service.py`: frame capture via Picamera2/OpenCV
- `detector.py`: object detection/classification via ONNX Runtime or TensorFlow Lite
- `estimator.py`: fill-level estimation from segmented/boxed detections and bin ROI
- `publisher.py`: publish telemetry to backend via HTTPS (or MQTT optional)
- `app.py`: orchestrates pipeline and scheduling

## Backend API Overview
- `main.py`: FastAPI app factory
- `v1.py`: endpoints for bin status ingest, listing, and route optimization stub
- `dto.py`: Pydantic models for requests/responses

## Configuration
Environment variables (see `.env.example`):
- `EDGE_DEVICE_ID`
- `BACKEND_BASE_URL`
- `BACKEND_API_KEY`
- `CAMERA_WIDTH`, `CAMERA_HEIGHT`, `CAPTURE_INTERVAL_SEC`
- `MODEL_PATH`, `MODEL_BACKEND` (onnx, tflite)

## Security
- API key auth for edge → backend communication
- HTTPS required for production
- Minimal PII; telemetry scoped to bin/device

## Route Optimization (Roadmap)
- Baseline: greedy nearest-neighbor using bins above threshold
- Future: VRP via OR-Tools with time windows and capacity

## Testing
```bash
pytest -q
```

## License
MIT



# tweak 1 at 2025-09-24 20:37:36

# tweak 20 at 2025-09-24 20:37:44

# tweak 39 at 2025-09-24 20:37:53















