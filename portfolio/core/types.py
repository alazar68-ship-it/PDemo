"""Core domain types (framework-agnostic)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True, slots=True)
class Project:
    """A demo project showcased on the hub page."""

    key: str
    title: str
    note: str
    tag: str
    description: str
    goal: str
    chips: Sequence[str]
    thumb_static_path: str
    glow_class: str
    demo_url: str
    github_url: str


@dataclass(frozen=True, slots=True)
class SocialLink:
    label: str
    url: str


@dataclass(frozen=True, slots=True)
class Profile:
    name: str
    tagline: str
    location: str
    email: str
    socials: Sequence[SocialLink]
