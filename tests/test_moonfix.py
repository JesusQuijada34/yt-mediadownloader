import importlib.util
from pathlib import Path


MODULE_PATH = Path(__file__).parents[1] / "yt-mediadownloader.py"
spec = importlib.util.spec_from_file_location("yt_media_downloader", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
YoutubeDownloader = module.YoutubeDownloader


def test_format_url_normalizes_watch_and_short_links():
    assert YoutubeDownloader.format_url(
        "https://www.youtube.com/watch?v=abc123&list=xyz"
    ) == "https://www.youtube.com/watch?v=abc123"
    assert YoutubeDownloader.format_url(
        "https://youtu.be/abc123?t=10"
    ) == "https://www.youtube.com/watch?v=abc123"
    assert YoutubeDownloader.format_url(
        "https://www.youtube.com/shorts/abc123?feature=share"
    ) == "https://www.youtube.com/shorts/abc123"


def test_supported_url_rejects_non_youtube_hosts():
    assert YoutubeDownloader.is_supported_url("https://www.youtube.com/watch?v=abc")
    assert not YoutubeDownloader.is_supported_url("https://example.com/watch?v=abc")


def test_safe_filename_blocks_path_separators_and_control_characters():
    result = YoutubeDownloader.safe_filename("../folder/video:name\n")
    assert "/" not in result
    assert "\\" not in result
    assert ".." not in result
    assert "\n" not in result
    assert result == "_folder_video_name_"
