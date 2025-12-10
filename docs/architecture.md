# Architecture Overview

## Runtime Topology
- Single Flask app (app factory in `app/__init__.py`, entry via `app/app.py`) with one blueprint (`routes.py`).
- Storage: local filesystem under `uploads/` for audio files; `instance/` reserved for optional SQLite/config.
- Templating: Jinja2 templates in `app/templates/`; static assets in `app/static/`.

## Key Components
- `routes.py`: HTTP endpoints for list, upload, play, and audio streaming. Uses secure filenames and path validation.
- `utils.py`: helpers for extension allowlist, Range header parsing, MIME detection, and streamed file reads.
- `templates/*`: `base.html` layout, `index.html` listing uploaded files, `upload.html` form, `player.html` audio playback.
- `static/css/form.css`: lightweight styling; `static/js/app.js`: basic player hook.

## Request Flow
1. **List (`GET /`)**: Reads `uploads/` and renders filenames; optional `message` query param for user feedback.
2. **Upload (`POST /upload`)**: Validates presence and extension, saves to `uploads/`, redirects to player on success.
3. **Player (`GET /player/<filename>`)**: Confirms file exists then renders the HTML5 audio page.
4. **Stream (`GET /audio/<filename>`)**: Serves audio with Range support. Returns `206 Partial Content` when `Range` is valid; `416` on invalid ranges; `404` for missing/unsafe paths.

## Configuration
- Defaults: `UPLOAD_FOLDER=uploads/`, `MAX_CONTENT_LENGTH=50MB`, `ALLOWED_EXTENSIONS={mp3,wav,m4a,aac,ogg}`.
- `SECRET_KEY` is `"dev"` by default; override via env or Flask config for non-dev use.
- `python-dotenv` supported; load environment variables as needed.

### Environment Variables
- `FLASK_APP`: set to `app.app` for CLI usage.
- `FLASK_ENV`/`FLASK_DEBUG`: enable debug reloading in development (do not use in prod).
- `SECRET_KEY`: override default for session security.
- `UPLOAD_FOLDER`: custom path if not using repo-local `uploads/`.
- `MAX_CONTENT_LENGTH`: adjust upload size limit (bytes).

## Error Handling & Security Notes
- Path traversal blocked by path resolution against `UPLOAD_FOLDER`.
- Non-allowed extensions rejected at upload.
- Large file uploads capped by `MAX_CONTENT_LENGTH`.
- No authentication included; add before exposing beyond trusted environments.

## Testing Strategy
- `tests/test_routes.py`: upload/list, range streaming, and error cases.
- `tests/test_utils.py`: extension allowlist and range parsing permutations.
- Pytest fixtures isolate uploads per test via temp directories.

## Simple Diagram
```
Browser
  |   GET /, /upload, /player
  v
Flask (routes.py) --- uses --> utils.py (range parsing, streaming)
  |                       |
  | serves templates      | reads files
  v                       v
templates/static      uploads/ (audio files)
```
