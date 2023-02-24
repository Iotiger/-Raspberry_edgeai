import time
from datetime import datetime, timezone
from shared import schemas
from shared import config
from edge.camera.camera_service import CameraService
from edge.inference.detector import WasteDetector
from edge.fill_level.estimator import FillLevelEstimator
from edge.comms.publisher import TelemetryPublisher


def run_loop() -> None:
    camera = CameraService(width=config.CAMERA_WIDTH, height=config.CAMERA_HEIGHT)
    detector = WasteDetector(model_path=config.MODEL_PATH, backend=config.MODEL_BACKEND)
    estimator = FillLevelEstimator()
    publisher = TelemetryPublisher(base_url=config.BACKEND_BASE_URL, api_key=config.BACKEND_API_KEY)

    while True:
        frame = camera.capture()
        detections = detector.detect(frame)
        fill_level = estimator.estimate(frame, detections)
        payload = schemas.Telemetry(
            device_id=config.EDGE_DEVICE_ID,
            timestamp_utc=datetime.now(timezone.utc).isoformat(),
            fill_level_pct=fill_level,
            detections=[schemas.Detection(**d) for d in detections],
        )
        publisher.publish(payload)
        time.sleep(config.CAPTURE_INTERVAL_SEC)


if __name__ == "__main__":
    run_loop()


