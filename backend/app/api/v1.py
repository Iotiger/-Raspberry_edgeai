from typing import List
from fastapi import APIRouter, Depends, Header, HTTPException
from shared.schemas import Telemetry, IngestResponse, BinStatus, RouteSuggestion
from backend.app.core.config import settings


router = APIRouter()

# In-memory store for demo
BIN_STORE: dict[str, BinStatus] = {}


def verify_api_key(authorization: str = Header("") ) -> None:
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="invalid auth header")
    token = authorization.split(" ", 1)[1]
    if token != settings.api_key:
        raise HTTPException(status_code=403, detail="invalid api key")


@router.post("/ingest", response_model=IngestResponse, dependencies=[Depends(verify_api_key)])
def ingest_telemetry(payload: Telemetry) -> IngestResponse:
    BIN_STORE[payload.device_id] = BinStatus(
        device_id=payload.device_id,
        fill_level_pct=payload.fill_level_pct,
        last_seen_utc=payload.timestamp_utc,
    )
    return IngestResponse(status="ok")


@router.get("/bins", response_model=List[BinStatus])
def list_bins() -> List[BinStatus]:
    return list(BIN_STORE.values())


@router.get("/optimize-route", response_model=RouteSuggestion)
def optimize_route(threshold: float = 60.0) -> RouteSuggestion:
    candidates = [b.device_id for b in BIN_STORE.values() if b.fill_level_pct >= threshold]
    return RouteSuggestion(route_order=candidates, note="greedy order (demo)")



# tweak 12 at 2025-09-24 20:37:40

# tweak 31 at 2025-09-24 20:37:49

# tweak 50 at 2025-09-24 20:37:57


