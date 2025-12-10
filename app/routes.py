from pathlib import Path
from flask import (
    Blueprint,
    Response,
    abort,
    current_app,
    redirect,
    render_template,
    request,
    send_file,
    url_for,
)
from werkzeug.utils import secure_filename

from .utils import allowed_file, guess_mimetype, parse_range_header, stream_file


bp = Blueprint("main", __name__)


def register_routes(app):
    app.register_blueprint(bp)


def _uploads_dir() -> Path:
    return Path(current_app.config["UPLOAD_FOLDER"]).resolve()


def _safe_file_path(filename: str) -> Path:
    uploads = _uploads_dir()
    candidate = (uploads / filename).resolve()
    if not str(candidate).startswith(str(uploads)):
        abort(404)
    return candidate


def _list_audio_files():
    uploads = _uploads_dir()
    uploads.mkdir(parents=True, exist_ok=True)
    return sorted([p.name for p in uploads.iterdir() if p.is_file()])


@bp.route("/")
def index():
    files = _list_audio_files()
    message = request.args.get("message")
    return render_template("index.html", files=files, message=message)


@bp.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        uploaded = request.files.get("file")
        if not uploaded or uploaded.filename == "":
            return redirect(url_for("main.index", message="No file selected"))

        if not allowed_file(uploaded.filename, current_app.config["ALLOWED_EXTENSIONS"]):
            return redirect(url_for("main.index", message="Unsupported file type"))

        filename = secure_filename(uploaded.filename)
        destination = _uploads_dir() / filename
        destination.parent.mkdir(parents=True, exist_ok=True)
        uploaded.save(destination)
        return redirect(url_for("main.player", filename=filename))

    return render_template("upload.html")


@bp.route("/player/<path:filename>")
def player(filename):
    file_path = _safe_file_path(filename)
    if not file_path.exists():
        abort(404)
    return render_template("player.html", filename=filename)


@bp.route("/audio/<path:filename>")
def audio(filename):
    file_path = _safe_file_path(filename)
    if not file_path.exists():
        abort(404)

    file_size = file_path.stat().st_size
    range_header = request.headers.get("Range")
    mimetype = guess_mimetype(file_path)

    if range_header:
        byte_range = parse_range_header(range_header, file_size)
        if byte_range is None:
            return Response(status=416)

        start, end = byte_range
        response = Response(
            stream_file(file_path, start, end),
            status=206,
            mimetype=mimetype,
            direct_passthrough=True,
        )
        response.headers.add("Content-Range", f"bytes {start}-{end}/{file_size}")
        response.headers.add("Accept-Ranges", "bytes")
        response.headers.add("Content-Length", str(end - start + 1))
        return response

    return send_file(file_path, mimetype=mimetype, conditional=True)
