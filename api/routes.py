import logging
from fastapi import APIRouter
from app.core.third_party_integrations.flood_score.api.proxy import router as proxy_router

logger = logging.getLogger(__name__)
router = APIRouter()

# Aggregate sub-routers
router.include_router(proxy_router)
