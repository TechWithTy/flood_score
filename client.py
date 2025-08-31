import os
from typing import Any, Dict, Optional

import requests
from app.core.third_party_integrations.flood_score import config


class FloodScoreClient:
    """
    Generic Flood Score provider client.
    Configure FLOOD_SCORE_BASE_URL to the provider's REST base.
    """

    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None, timeout: Optional[int] = None):
        self.api_key = api_key or os.getenv("FLOOD_SCORE_API_KEY") or getattr(config, "FLOOD_SCORE_API_KEY", None)
        resolved_base = base_url or os.getenv("FLOOD_SCORE_BASE_URL") or getattr(config, "FLOOD_SCORE_BASE_URL", "")
        self.base_url = (resolved_base or "").rstrip("/")
        self.timeout = timeout if timeout is not None else int(getattr(config, "FLOOD_SCORE_TIMEOUT", 15))

    def _headers(self) -> Dict[str, str]:
        headers = {"Accept": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers

    def get(self, path: str, *, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        if not self.base_url:
            raise ValueError("FLOOD_SCORE_BASE_URL not set; cannot perform request")
        url = f"{self.base_url}/{path.lstrip('/')}"
        resp = requests.get(url, headers=self._headers(), params=params or {}, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()

    def health(self) -> bool:
        return bool(self.base_url)