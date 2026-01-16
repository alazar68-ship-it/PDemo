# Endpoints

## Pages

| Route | Method | Response | Notes |
|---|---|---|---|
| `/` | GET | HTML | Főoldal (Hero / Projektek / Kapcsolat) |

## Health

| Route | Method | Response | Error cases |
|---|---|---|---|
| `/health` | GET | `200 OK` text/plain: `ok` | 500 csak akkor, ha a process nem fut |

## API (JSON)

### `GET /api/health`

**Response (200):**
```json
{"status":"ok","time":"2026-01-12T12:00:00Z"}
```

### `GET /api/projects`

**Response (200):**
```json
{"projects":[{"key":"digitrec","title":"...","demo_url":"...","github_url":"..."}]}
```

### `GET /api/profile`

**Response (200):**
```json
{"name":"András Lázár","tagline":"Python AI fejlesztés","location":"Budapest, HU","contact":{"email":"..."}}
```
