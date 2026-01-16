"""Service layer: data assembly for routes."""
from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List

from portfolio.core.catalog import build_profile, build_projects
from portfolio.core.types import Profile, Project


class PortfolioService:
    """Facade for portfolio data.

    A service réteg célja, hogy a route/view réteg ne érintse közvetlenül a core konfigurációt.
    """

    def get_profile(self) -> Profile:
        return build_profile()

    def list_projects(self) -> List[Project]:
        return build_projects()

    def profile_payload(self) -> Dict[str, Any]:
        p = self.get_profile()
        return {
            "name": p.name,
            "tagline": p.tagline,
            "location": p.location,
            "contact": {
                "email": p.email,
            },
            "socials": [{"label": s.label, "url": s.url} for s in p.socials],
        }

    def projects_payload(self) -> Dict[str, Any]:
        return {
            "projects": [
                {
                    "key": pr.key,
                    "title": pr.title,
                    "note": pr.note,
                    "tag": pr.tag,
                    "description": pr.description,
                    "goal": pr.goal,
                    "chips": list(pr.chips),
                    "demo_url": pr.demo_url,
                    "github_url": pr.github_url,
                }
                for pr in self.list_projects()
            ]
        }
