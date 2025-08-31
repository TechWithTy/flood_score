import requests
from requests import Session

from app.core.third_party_integrations.flood_score import config


class FloodAPIBase:
    """
    Base for Flood Score API requests.
    Uses FLOOD_SCORE_BASE_URL and FLOOD_SCORE_TIMEOUT from config.
    """

    def __init__(self):
        self.session: Session = requests.Session()
        self.base_url: str = getattr(config, "FLOOD_SCORE_BASE_URL", "").rstrip("/")
        self.timeout: int = int(getattr(config, "FLOOD_SCORE_TIMEOUT", 15))

    def get(self, path: str, *, params: dict | None = None, headers: dict | None = None):
        if not self.base_url:
            raise ValueError("FLOOD_SCORE_BASE_URL not set; cannot perform request")
        url = f"{self.base_url}/{path.lstrip('/')}"
        resp = self.session.get(url, params=params or {}, headers=headers or {}, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()