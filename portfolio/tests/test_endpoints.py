from __future__ import annotations

import pytest


@pytest.mark.django_db
def test_home_renders(client):
    resp = client.get("/")
    assert resp.status_code == 200
    body = resp.content.decode("utf-8")
    # Smoke checks (frontend-ish)
    assert "Digitrec" in body
    assert "Tajmese" in body
    assert "RAG_Chat" in body
    assert "AutoChess" in body
    assert 'id="projects"' in body
    assert 'id="contact"' in body


def test_health_plain(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.content.decode("utf-8").strip() == "ok"


def test_api_health(client):
    resp = client.get("/api/health")
    assert resp.status_code == 200
    payload = resp.json()
    assert payload["status"] == "ok"
    assert payload["time"].endswith("Z")


def test_api_projects(client):
    resp = client.get("/api/projects")
    assert resp.status_code == 200
    payload = resp.json()
    assert "projects" in payload
    assert len(payload["projects"]) == 4
    keys = {p["key"] for p in payload["projects"]}
    assert keys == {"digitrec", "tajmese", "ragchat", "autochess"}
