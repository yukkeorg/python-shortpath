from pathlib import Path

import shortpath


def test_absolute_path():
    source = Path("/aaaa/bbbb/cccc/dddd/")
    result = shortpath.shortpath(source)
    assert result == "/a/b/c/dddd"


def test_related_path():
    source = Path("aaaa/bbbb/cccc/dddd/")
    result = shortpath.shortpath(source)
    assert result == "a/b/c/dddd"


def test_string_path():
    source = "aaaa/bbbb/cccc/dddd/"
    result = shortpath.shortpath(source)
    assert result == "a/b/c/dddd"


def test_including_multibyte_in_path():
    source = "aaaa/あいうえお/亜胃雨絵尾/dddd"
    result = shortpath.shortpath(source)
    assert result == "a/あ/亜/dddd"
