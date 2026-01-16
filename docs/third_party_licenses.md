# Third-party dependencies

Cél: Apache-2.0 kompatibilis disztribúció.

| Dependency | Purpose | License |
|---|---|---|
| Django | Web framework | BSD-3-Clause |
| gunicorn | WSGI server (prod) | MIT |
| pytest | Test runner (dev) | MIT |
| pytest-django | Django integration for pytest (dev) | BSD-3-Clause |
| HTMX (CDN) | UI interactions (runtime, loaded from CDN) | BSD-2-Clause (project license) |

Megjegyzés: a frontenden a referencia HTML-ben szereplő HTMX CDN betöltés maradt meg. Ha self-hosted/offline kell, tedd be a saját static alá.
