import requests
from shared.schemas import Telemetry, IngestResponse


class TelemetryPublisher:
    def __init__(self, base_url: str, api_key: str) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key

    def publish(self, payload: Telemetry) -> IngestResponse:
        url = f"{self.base_url}/api/v1/ingest"
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        try:
            resp = requests.post(url, headers=headers, json=payload.model_dump())
            resp.raise_for_status()
            data = resp.json()
            return IngestResponse(**data)
        except Exception:
            return IngestResponse(status="error", message="failed to publish")



# tweak 17 at 2025-09-24 20:37:42

# tweak 36 at 2025-09-24 20:37:51
