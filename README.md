# Techinai Demo Hub (Django + HTMX)

Ez a repository egy **hub / landing** webalkalmazás, amelyről 4 különálló Django+HTMX demó indítható
(**Digitrec**, **Tajmese**, **RAG_Chat**, **AutoChess**). A UI a mellékelt referencia HTML alapján készült,
és **Django template** formában kerül kiszolgálásra.

## Fő funkciók

- Főoldal (Hero / Projektek / Kapcsolat) – server-side render, HTMX kompatibilis
- JSON API:
  - `GET /api/projects`
  - `GET /api/profile`
  - `GET /api/health`
- Health endpoint:
  - `GET /health`

## Követelmények

- Python 3.12+
- Django 5.x

## Gyors indítás (dev)

```bash
python -m venv .venv
source .venv/bin/activate
.\.venv\Scripts\activate  # Windows
pip install -r requirements.txt

cp .env.example .env
# állítsd be a SECRET_KEY-t!

python manage.py migrate
python manage.py runserver 127.0.0.1:8000
```

## Prod javaslat (Ubuntu + systemd + nginx)

- gunicorn: `gunicorn hubsite.wsgi:application --bind 127.0.0.1:8000 --workers 2`
- nginx reverse proxy: `hub.<domain>` -> `127.0.0.1:8000`

Részletek: `docs/endpoints.md`

## Konfiguráció

A projektek listája és a linkek: `portfolio/core/catalog.py`

A képek: `portfolio/static/portfolio/images/`

## Tesztek

```bash
pip install -r requirements-dev.txt
pytest
```

## Licenc

Apache-2.0 – lásd: `LICENSE`.
