# Flood Score (Provider-agnostic)

SDK and FastAPI proxy for a Flood Score provider, aligned with other integrations.

## Environment Variables

- FLOOD_SCORE_BASE_URL (required)
- FLOOD_SCORE_API_KEY (optional, if provider requires)
- FLOOD_SCORE_TIMEOUT (default: 15)

Example .env:
FLOOD_SCORE_BASE_URL=https://www.fema.gov/flood-maps/products-tools/hazus
FLOOD_SCORE_API_KEY=your_api_key_if_required
FLOOD_SCORE_TIMEOUT=15

## Endpoints

- GET /flood-score/health
  - Returns: { healthy, base_url, has_api_key }

- GET /flood-score/{path}
  - Proxies a GET to {FLOOD_SCORE_BASE_URL}/{path}
  - Query string is forwarded as-is

Examples:
curl "http://localhost:8000/flood-score/health"

# Example: score-by-address (if provider supports)
# Sends GET to {FLOOD_SCORE_BASE_URL}/score and forwards params
curl "http://localhost:8000/flood-score/score?address=123+Main+St&city=Austin&state=TX&postalCode=78701"

## Internal Structure

- client.py: FloodScoreClient resolving env/config; headers, GET, health.
- api/proxy.py: Routes (`/flood-score/health`, passthrough `/{path:path}`).
- api/routes.py: Aggregates flood_score sub-routers.
- api/_base.py: FloodAPIBase with shared requests session.
- api/_requests.py: ListParams, ScoreByAddressParams.
- api/_enums.py, api/_responses.py, api/_exceptions.py: helpers.
