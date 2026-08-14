import re
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from yt_dlp import YoutubeDL


class YoutubeDownloader(QWidget):
    """GUI Fluthin para descargar audio o vídeo desde YouTube."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("YT Media Downloader")
        self.setGeometry(100, 100, 1000, 600)
        self.setStyleSheet(
            """
            QWidget {
                background-color: #0d1117;
                color: #c9d1d9;
                font-family: Arial;
                font-size: 11pt;
                border: 1px solid #30363d;
                border-radius: 3px;
            }
            QPushButton {
                background-color: #161b22;
                border: none;
                padding: 6px;
                font-weight: bold;
                min-width: 100px;
            }
            QPushButton:hover { background-color: #21262d; }
            QPushButton:pressed { background-color: #30363d; }
            QLineEdit {
                background-color: #161b22;
                border: 1px solid #30363d;
                color: #c9d1d9;
                padding: 4px;
            }
            """
        )

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.youtube.com"))
        self.browser.urlChanged.connect(self.capture_url)

        self.url_label = QLabel("URL detectada:")
        self.url_field = QLineEdit()
        self.url_field.setReadOnly(True)

        self.download_audio_btn = QPushButton("Descargar Audio")
        self.download_audio_btn.clicked.connect(self.download_audio)
        self.download_video_btn = QPushButton("Descargar Video")
        self.download_video_btn.clicked.connect(self.download_video)
        self.path_btn = QPushButton("Cambiar carpeta")
        self.path_btn.clicked.connect(self.change_path)

        self.download_path = str(Path.home() / "Downloads")
        side_layout = QVBoxLayout()
        for widget in (
            self.url_label,
            self.url_field,
            self.download_audio_btn,
            self.download_video_btn,
            self.path_btn,
        ):
            side_layout.addWidget(widget)

        top_layout = QHBoxLayout()
        top_layout.addWidget(self.browser, 3)
        top_layout.addLayout(side_layout, 1)
        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)
        self.setLayout(main_layout)

    @staticmethod
    def format_url(url):
        """Normaliza una URL de vídeo sin eliminar parámetros necesarios."""
        parsed = urlparse(url.strip())
        host = parsed.netloc.lower().split(":", 1)[0]
        if host == "youtu.be":
            video_id = parsed.path.strip("/").split("/", 1)[0]
            return f"https://www.youtube.com/watch?v={video_id}" if video_id else ""
        if host not in {"youtube.com", "www.youtube.com", "m.youtube.com"}:
            return url.strip()
        if parsed.path.startswith("/shorts/"):
            video_id = parsed.path.split("/", 2)[-1]
            return f"https://www.youtube.com/shorts/{video_id}" if video_id else url.strip()
        if parsed.path == "/watch":
            video_id = parse_qs(parsed.query).get("v", [""])[0]
            return f"https://www.youtube.com/watch?v={video_id}" if video_id else url.strip()
        return url.strip()

    @staticmethod
    def is_supported_url(url):
        parsed = urlparse(url)
        host = parsed.netloc.lower().split(":", 1)[0]
        return host in {"youtube.com", "www.youtube.com", "m.youtube.com", "youtu.be"}

    @staticmethod
    def safe_filename(value, fallback="media"):
        """Evita separadores, nombres reservados y archivos ocultos ambiguos."""
        value = re.sub(r"[\\/:*?\"<>|\x00-\x1f]", "_", str(value or ""))
        value = re.sub(r"\s+", " ", value).strip(" .")
        return (value or fallback)[:180]

    def capture_url(self, qurl):
        self.url_field.setText(self.format_url(qurl.toString()))

    def change_path(self):
        folder = QFileDialog.getExistingDirectory(self, "Selecciona carpeta de descarga")
        if folder:
            self.download_path = folder

    def get_title(self, url):
        try:
            with YoutubeDL({"quiet": True, "noplaylist": True}) as ydl:
                info = ydl.extract_info(url, download=False)
                return self.safe_filename(info.get("title", "media"))
        except Exception as exc:
            self.show_error("No se pudo obtener el título", exc)
            return "media"

    def show_error(self, title, error):
        QMessageBox.critical(self, title, str(error))

    def _download(self, url, kind):
        if not self.is_supported_url(url):
            self.show_error("URL no válida", "Selecciona un vídeo de YouTube válido.")
            return
        title = self.get_title(url)
        default_dir = Path.home() / ("Music" if kind == "audio" else "Videos")
        output_dir = Path(self.download_path or default_dir).expanduser().resolve()
        output_dir.mkdir(parents=True, exist_ok=True)
        extension = "mp3" if kind == "audio" else "mp4"
        output = str(output_dir / f"{title}.{extension}")
        opts = {"format": "bestaudio/best" if kind == "audio" else "best", "outtmpl": output}
        if kind == "audio":
            opts["postprocessors"] = [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }]
        try:
            with YoutubeDL(opts) as ydl:
                ydl.download([url])
        except Exception as exc:
            self.show_error("Error durante la descarga", exc)

    def download_audio(self):
        self._download(self.url_field.text(), "audio")

    def download_video(self):
        self._download(self.url_field.text(), "video")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YoutubeDownloader()
    window.show()
    sys.exit(app.exec_())
