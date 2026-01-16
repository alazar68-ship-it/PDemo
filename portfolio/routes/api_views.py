"""JSON API endpoints."""
from __future__ import annotations

from datetime import datetime, timezone

from django.http import HttpRequest, JsonResponse

from portfolio.service.portfolio_service import PortfolioService


def api_health(_: HttpRequest) -> JsonResponse:
    """Return service health in JSON form."""
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    return JsonResponse({"status": "ok", "time": now})


def api_projects(_: HttpRequest) -> JsonResponse:
    """Return the project catalog in JSON form."""
    svc = PortfolioService()
    return JsonResponse(svc.projects_payload())


def api_profile(_: HttpRequest) -> JsonResponse:
    """Return the public profile info in JSON form."""
    svc = PortfolioService()
    return JsonResponse(svc.profile_payload())
