# Repository Guidelines

## Project Structure & Module Organization
- `app/`: Flask application skeleton; fill `routes.py` with HTTP handlers, `utils.py` for helpers (e.g., range handling), `templates/` for Jinja pages, and `static/` for CSS/JS.
- `uploads/`: Local audio storage; keep out of version control.
- `instance/`: SQLite or runtime config; defaults to `instance/media.db` when used.
- `docs/`: Reference specs (`architecture.md`, `api-spec.md`); update when behavior changes.
- `tests/`: Add unit/functional tests here (`test_routes.py`, `test_utils.py` placeholders).

## Build, Test, and Development Commands
- Create env: `python -m venv .venv && source .venv/bin/activate`.
- Install deps: `pip install -r requirements.txt` (add Flask/pytest/etc. as you implement features).
- Run server: `FLASK_APP=app.app flask run` from repo root; hot-reloads with `FLASK_DEBUG=1`.
- Format/lint (recommended): `python -m black app tests` and `python -m isort app tests` once added to deps.
- Test suite: `pytest` (ensure `pytest` is listed in `requirements.txt` or `requirements-dev.txt`).

## Coding Style & Naming Conventions
- Python: 4-space indent, type hints where practical, small helpers in `utils.py`, route logic in `routes.py`.
- Templates: Prefer small, reusable blocks in `templates/`, extend `base.html`.
- Static assets: Namespace CSS/JS per page (e.g., `static/css/player.css`), avoid inline scripts when possible.
- Naming: snake_case for Python, kebab-case for static asset files, PascalCase for classes if introduced.

## Testing Guidelines
- Use `pytest` with descriptive test names (`test_stream_range_returns_partial_content`).
- Mirror modules under test in `tests/` (e.g., `tests/test_utils.py` for `app/utils.py`).
- Include fixture audio files via temporary directories, not committed to `uploads/`.
- Target coverage of streaming edge cases (range headers), upload validation, and template rendering.

## Commit & Pull Request Guidelines
- Commits: short imperative subjects (e.g., `Add range parser for audio streaming`); group related changes.
- PRs: describe intent, key changes, and testing done; link issues/tasks; include screenshots or curl examples for new endpoints/UI.
- Keep diffs focused; extract refactors into separate PRs where feasible.

## Security & Configuration Tips
- Do not commit secrets or real media; use `.env` for local settings and ignore it.
- Validate uploads (type/size) and serve files via controlled routes, not direct static hosting.
- For optional auth/DB features, prefer parameterized queries/ORM patterns and minimal role sets.
