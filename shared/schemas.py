from pydantic import BaseModel, Field
from typing import List, Optional


class Detection(BaseModel):
    label: str
    confidence: float = Field(ge=0.0, le=1.0)
    bbox: List[int]  # [x, y, w, h]


class Telemetry(BaseModel):
    device_id: str
    timestamp_utc: str
    fill_level_pct: float = Field(ge=0.0, le=100.0)
    detections: List[Detection] = []


class IngestResponse(BaseModel):
    status: str
    message: Optional[str] = None


class BinStatus(BaseModel):
    device_id: str
    fill_level_pct: float
    last_seen_utc: str


class RouteSuggestion(BaseModel):
    route_order: List[str]
    note: Optional[str] = None



# tweak 7 at 2025-09-24 20:37:38

# tweak 26 at 2025-09-24 20:37:46

# tweak 45 at 2025-09-24 20:37:55


