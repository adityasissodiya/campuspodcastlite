# API Specification

## Conventions
- Base URL: `http://localhost:5000`
- Auth: None (development only). Add auth before deploying.
- Content: HTML for pages; binary audio for `/audio/*`.

## Endpoints

### GET `/`
- Purpose: List available audio files.
- Response: `200 OK` HTML page; shows filenames from `uploads/`. Optional `message` query string surfaces notices (e.g., upload errors).

### GET `/upload`
- Purpose: Render upload form.
- Response: `200 OK` HTML form.

### POST `/upload`
- Purpose: Upload an audio file to `uploads/`.
- Request:
  - Form-data: `file` (required); allowed extensions: `mp3`, `wav`, `m4a`, `aac`, `ogg`.
- Responses:
  - `302` redirect to `/player/<filename>` on success.
  - `302` redirect to `/` with `?message=...` when missing file or unsupported type.

### GET `/player/<filename>`
- Purpose: Render HTML5 audio player for a given file.
- Responses:
  - `200 OK` HTML page when file exists.
  - `404 Not Found` when file is missing or path invalid.

### GET `/audio/<filename>`
- Purpose: Serve audio file contents with HTTP Range support.
- Request headers: Optional `Range: bytes=<start>-<end>` (e.g., `bytes=0-1023`, `bytes=500-`, `bytes=-1024`).
- Responses:
  - `200 OK` full file when no Range header.
  - `206 Partial Content` with `Content-Range`, `Accept-Ranges: bytes`, and partial body when Range is valid.
  - `416 Range Not Satisfiable` when Range is invalid/out of bounds.
  - `404 Not Found` when file is missing or path invalid.
- MIME type guessed from filename; falls back to `application/octet-stream`.

## Examples
- Upload: `curl -F "file=@sample.mp3" http://localhost:5000/upload -L`
- Stream first KB: `curl -H "Range: bytes=0-1023" http://localhost:5000/audio/sample.mp3 -i`
