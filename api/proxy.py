import logging
from typing import Dict

from fastapi import APIRouter, Request

from app.core.third_party_integrations.flood_score.client import FloodScoreClient

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/flood-score", tags=["flood_score-proxy"])


# Utility

def proxy_get(path: str, params: Dict) -> Dict:
    client = FloodScoreClient()
    return client.get(path, params=params)


# Routes
@router.get("/health")
async def health() -> Dict:
    client = FloodScoreClient()
    return {
        "healthy": client.health(),
        "base_url": client.base_url,
        "has_api_key": bool(client.api_key),
    }

@router.get("/{path:path}")
async def flood_score_get(path: str, request: Request) -> Dict:
    return proxy_get(path, dict(request.query_params))
