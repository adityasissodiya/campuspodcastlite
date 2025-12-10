import io
from pathlib import Path

import pytest

from app import create_app


@pytest.fixture()
def client(tmp_path):
    app = create_app({"TESTING": True, "UPLOAD_FOLDER": tmp_path})
    with app.test_client() as client:
        yield client


def test_index_renders_without_files(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"No audio uploaded yet" in response.data


def test_upload_and_list_file(client, tmp_path):
    data = {"file": (io.BytesIO(b"abc"), "sample.mp3")}
    response = client.post("/upload", data=data, content_type="multipart/form-data", follow_redirects=True)
    assert response.status_code == 200

    uploads = list(Path(tmp_path).glob("*.mp3"))
    assert uploads

    list_response = client.get("/")
    assert b"sample.mp3" in list_response.data


def test_audio_range_request(client, tmp_path):
    file_path = tmp_path / "clip.mp3"
    file_path.write_bytes(b"0123456789")

    response = client.get("/audio/clip.mp3", headers={"Range": "bytes=2-5"})
    assert response.status_code == 206
    assert response.headers["Content-Range"] == "bytes 2-5/10"
    assert response.data == b"2345"


def test_audio_404_for_missing_file(client):
    response = client.get("/audio/missing.mp3")
    assert response.status_code == 404
