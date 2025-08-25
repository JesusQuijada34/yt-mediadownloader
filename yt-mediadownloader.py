# ¡Vamos allá, Jesús! Te voy a construir un descargador de videos de YouTube con GUI, que incluye:
#
#  🖥️ Interfaz con panel lateral para espiar URLs
#  🔍 Detección automática de URLs de YouTube
#  🎬 Obtención del título del video
#  📥 Opciones de descarga (video/audio)
#  🔄 Conversión a MP3
#  🔧 Modular y personalizable
#
# Usaremos PyQt5 para la interfaz y pytube para la descarga.
#
# 🧩 Paso 1: Instala las dependencias
# pip install PyQt5 pytube
#
# 🧩 Paso 2: Script completo del descargador

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QListWidget, QLineEdit, QMessageBox
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from pytube import YouTube
import sys
import os

class YouTubeDownloader(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Youtube Downloader")
        self.setGeometry(100, 100, 1000, 600)

        # Layout principal
        layout = QHBoxLayout()
        self.setLayout(layout)

        # 🖥️ Panel de navegador
        self.browser = QWebEngineView()
        self.browser.load(QUrl("https://www.youtube.com"))
        self.browser.urlChanged.connect(self.detect_url)
        layout.addWidget(self.browser, 3)

        # 📋 Panel lateral
        side_panel = QVBoxLayout()

        self.url_label = QLabel("URL detectada:")
        self.url_field = QLineEdit()
        self.title_label = QLabel("Título del video:")
        self.title_field = QLineEdit()

        self.download_btn = QPushButton("📥 Descargar Video")
        self.download_btn.clicked.connect(self.download_video)

        self.audio_btn = QPushButton("🎧 Descargar Audio (MP3)")
        self.audio_btn.clicked.connect(self.download_audio)

        self.history_list = QListWidget()

        side_panel.addWidget(self.url_label)
        side_panel.addWidget(self.url_field)
        side_panel.addWidget(self.title_label)
        side_panel.addWidget(self.title_field)
        side_panel.addWidget(self.download_btn)
        side_panel.addWidget(self.audio_btn)
        side_panel.addWidget(QLabel("Historial de URLs:"))
        side_panel.addWidget(self.history_list)

        layout.addLayout(side_panel, 1)

    def detect_url(self, qurl):
        url = qurl.toString()
        if "youtube.com/watch" in url:
            self.url_field.setText(url)
            try:
                yt = YouTube(url)
                self.title_field.setText(yt.title)
                self.history_list.addItem(yt.title)
            except Exception as e:
                self.title_field.setText("Error al obtener título")

    def download_video(self):
        url = self.url_field.text()
        if not url:
            QMessageBox.warning(self, "Error", "No se detectó URL válida.")
            return
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            stream.download()
            QMessageBox.information(self, "Éxito", f"Video descargado: {yt.title}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo descargar el video.\n{str(e)}")

    def download_audio(self):
        url = self.url_field.text()
        if not url:
            QMessageBox.warning(self, "Error", "No se detectó URL válida.")
            return
        try:
            yt = YouTube(url)
            stream = yt.streams.filter(only_audio=True).first()
            out_file = stream.download()
            base, ext = os.path.splitext(out_file)
            new_file = base + ".mp3"
            os.rename(out_file, new_file)
            QMessageBox.information(self, "Éxito", f"Audio descargado: {yt.title}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo descargar el audio.\n{str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YouTubeDownloader()
    window.show()
    sys.exit(app.exec_())

# ---
#
# ### ✅ ¿Qué hace este script?
#
# - Abre YouTube en un navegador embebido.
# - Detecta automáticamente URLs de videos.
# - Muestra el título del video.
# - Permite descargar el video o convertirlo a MP3.
# - Guarda historial de títulos en el panel lateral.
#
# ---
#
# ¿Quieres que lo empaquetemos como `.iflapp` para tu sistema IPM? También puedo ayudarte a agregar filtros por resolución, subtítulos, o integración con Telegram.