from app.utils import allowed_file, parse_range_header


def test_allowed_file_accepts_known_extensions():
    assert allowed_file("song.mp3", {"mp3"})
    assert not allowed_file("document.txt", {"mp3"})


def test_parse_range_header_full_formats():
    size = 100
    assert parse_range_header("bytes=0-9", size) == (0, 9)
    assert parse_range_header("bytes=20-", size) == (20, 99)
    assert parse_range_header("bytes=-10", size) == (90, 99)


def test_parse_range_header_invalid_inputs():
    size = 50
    assert parse_range_header("", size) is None
    assert parse_range_header("bytes=100-10", size) is None
    assert parse_range_header("bytes=0-200", size) is None
    assert parse_range_header("notbytes=0-1", size) is None
