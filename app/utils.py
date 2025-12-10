import mimetypes
from pathlib import Path
from typing import Iterable, Optional, Tuple


def allowed_file(filename: str, allowed_extensions: set) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in allowed_extensions


def parse_range_header(range_header: str, file_size: int) -> Optional[Tuple[int, int]]:
    """
    Parse HTTP Range header. Returns (start, end) inclusive byte range.
    Supports:
    - bytes=start-end
    - bytes=start-
    - bytes=-suffix_length
    """
    if not range_header or not range_header.startswith("bytes="):
        return None

    try:
        ranges = range_header.replace("bytes=", "").split("-")
        if len(ranges) != 2:
            return None

        start_str, end_str = ranges
        if start_str and end_str:
            start, end = int(start_str), int(end_str)
        elif start_str and not end_str:
            start = int(start_str)
            end = file_size - 1
        elif not start_str and end_str:
            length = int(end_str)
            if length == 0:
                return None
            start = max(file_size - length, 0)
            end = file_size - 1
        else:
            return None

        if start < 0 or end < start or end >= file_size:
            return None
        return start, end
    except ValueError:
        return None


def guess_mimetype(file_path: Path) -> str:
    mimetype, _ = mimetypes.guess_type(file_path.name)
    return mimetype or "application/octet-stream"


def stream_file(path: Path, start: int, end: int, chunk_size: int = 8192) -> Iterable[bytes]:
    """Stream file bytes between start and end (inclusive)."""
    with path.open("rb") as handle:
        handle.seek(start)
        remaining = end - start + 1
        while remaining > 0:
            data = handle.read(min(chunk_size, remaining))
            if not data:
                break
            remaining -= len(data)
            yield data
