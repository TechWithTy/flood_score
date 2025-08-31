import os


FLOOD_SCORE_BASE_URL = os.getenv("FLOOD_SCORE_BASE_URL", "").rstrip("/")
FLOOD_SCORE_API_KEY = os.getenv("FLOOD_SCORE_API_KEY")
FLOOD_SCORE_TIMEOUT = float(os.getenv("FLOOD_SCORE_TIMEOUT", "15"))