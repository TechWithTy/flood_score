from typing import Any, Dict, List, TypedDict


class FloodScoreResult(TypedDict, total=False):
    address: str
    score: float
    details: Dict[str, Any]


class PaginatedResults(TypedDict, total=False):
    page: int
    pageSize: int
    total: int
    items: List[Dict[str, Any]]