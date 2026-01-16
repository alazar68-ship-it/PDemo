"""HTTP page routes."""
from __future__ import annotations

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from portfolio.service.portfolio_service import PortfolioService


def home(request: HttpRequest) -> HttpResponse:
    """Render the landing page."""
    svc = PortfolioService()
    ctx = {
        "profile": svc.get_profile(),
        "projects": svc.list_projects(),
    }
    return render(request, "portfolio/index.html", ctx)


def health(_: HttpRequest) -> HttpResponse:
    """Lightweight health endpoint for load balancers and monitoring."""
    return HttpResponse("ok", content_type="text/plain; charset=utf-8")
