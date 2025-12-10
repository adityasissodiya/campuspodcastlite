from pathlib import Path
from flask import Flask


def create_app(test_config=None):
    """Application factory for Campus Podcast Lite."""
    app = Flask(__name__, instance_relative_config=True)

    base_config = {
        "SECRET_KEY": "dev",  # replace in production
        "UPLOAD_FOLDER": Path(app.root_path).parent / "uploads",
        "MAX_CONTENT_LENGTH": 50 * 1024 * 1024,  # 50 MB
        "ALLOWED_EXTENSIONS": {"mp3", "wav", "m4a", "aac", "ogg"},
    }
    app.config.from_mapping(base_config)

    if test_config:
        app.config.update(test_config)

    upload_dir = Path(app.config["UPLOAD_FOLDER"])
    upload_dir.mkdir(parents=True, exist_ok=True)

    from .routes import register_routes

    register_routes(app)
    return app
