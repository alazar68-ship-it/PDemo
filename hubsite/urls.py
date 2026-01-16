"""URL routing for the demo hub.

Static files policy:
- Development: serve static when running `python manage.py runserver`, even if DEBUG=False.
- Production: serve static via Nginx (recommended). Keep Django static serving disabled.

You can force-enable Django static serving with: SERVE_STATIC_WITH_DJANGO=1
"""

from __future__ import annotations

import os
import sys

from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path

from portfolio.routes.api_views import api_health, api_profile, api_projects
from portfolio.routes.views import health, home


def _truthy(raw: str | None) -> bool:
    if raw is None:
        return False
    return raw.strip().lower() in {"1", "true", "yes", "y", "on"}


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("health", health, name="health"),
    path("api/health", api_health, name="api_health"),
    path("api/profile", api_profile, name="api_profile"),
    path("api/projects", api_projects, name="api_projects"),
]

# Django static serving is ONLY for development.
# In production, serve `/static/` with Nginx (and run `collectstatic`).
_should_serve_static = (
    settings.DEBUG
    or "runserver" in sys.argv
    or _truthy(os.environ.get("SERVE_STATIC_WITH_DJANGO"))
)

if _should_serve_static:
    try:
        # Serve using the staticfiles finders (STATICFILES_DIRS + app/static/),
        # and allow serving even when DEBUG=False (insecure=True).
        from django.contrib.staticfiles.views import serve as staticfiles_serve

        urlpatterns += [
            re_path(
                r"^static/(?P<path>.*)$",
                staticfiles_serve,
                kwargs={"insecure": True},
            )
        ]
    except Exception:
        # Fallback: serve from STATIC_ROOT (requires collectstatic).
        from django.conf.urls.static import static

        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
