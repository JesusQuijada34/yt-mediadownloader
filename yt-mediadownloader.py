import sys
import os
import subprocess
import platform
import urllib.request
import urllib.parse
import urllib.error
import re
import json
import html.parser
from pathlib import Path
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QSplitter, QPushButton, QLabel, 
                             QLineEdit, QComboBox, QProgressBar, QTextEdit,
                             QFrame, QSizePolicy, QMessageBox, QFileDialog)
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QUrl, QTimer
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtGui import QIcon, QPixmap, QFont, QPalette, QColor
import tempfile

class YouTubeMetadataExtractor:
    """Clase para extraer metadatos de videos de YouTube usando bibliotecas nativas"""
    
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    
    def is_valid_youtube_url(self, url):
        """Verifica si la URL es válida de YouTube"""
        youtube_patterns = [
            r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=[\w-]+',
            r'(?:https?://)?(?:www\.)?youtu\.be/[\w-]+',
            r'(?:https?://)?(?:www\.)?youtube\.com/embed/[\w-]+',
            r'(?:https?://)?(?:www\.)?youtube\.com/v/[\w-]+'
        ]
        
        for pattern in youtube_patterns:
            if re.match(pattern, url):
                return True
        return False
    
    def extract_video_id(self, url):
        """Extrae el ID del video de la URL de YouTube"""
        patterns = [
            r'(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/|youtube\.com/v/)([\w-]+)',
            r'v=([\w-]+)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        return None
    
    def get_video_info(self, url):
        """Obtiene información del video usando la API de oEmbed de YouTube"""
        try:
            video_id = self.extract_video_id(url)
            if not video_id:
                return None
            
            # Usar la API oEmbed de YouTube
            oembed_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"
            
            req = urllib.request.Request(oembed_url, headers={'User-Agent': self.user_agent})
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
                
                return {
                    'title': data.get('title', 'Título no disponible'),
                    'author': data.get('author_name', 'Autor no disponible'),
                    'thumbnail': data.get('thumbnail_url', ''),
                    'width': data.get('width', 0),
                    'height': data.get('height', 0),
                    'video_id': video_id
                }
                
        except Exception as e:
            print(f"Error al obtener información del video: {e}")
            return None
    
    def get_video_duration(self, url):
        """Intenta obtener la duración del video (requiere acceso a la página completa)"""
        try:
            video_id = self.extract_video_id(url)
            if not video_id:
                return None
            
            # URL de la página del video
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            
            req = urllib.request.Request(video_url, headers={'User-Agent': self.user_agent})
            with urllib.request.urlopen(req) as response:
                html_content = response.read().decode('utf-8')
                
                # Buscar información de duración en el HTML
                duration_pattern = r'"lengthSeconds":"(\d+)"'
                duration_match = re.search(duration_pattern, html_content)
                
                if duration_match:
                    seconds = int(duration_match.group(1))
                    minutes = seconds // 60
                    remaining_seconds = seconds % 60
                    return f"{minutes}:{remaining_seconds:02d}"
                
                return None
                
        except Exception as e:
            print(f"Error al obtener duración: {e}")
            return None

class WebPageInspector(QThread):
    """Hilo para inspeccionar páginas web y extraer información"""
    page_analyzed = pyqtSignal(dict)
    error_occurred = pyqtSignal(str)
    
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.metadata_extractor = YouTubeMetadataExtractor()
    
    def run(self):
        try:
            # Verificar si es una URL de YouTube
            if not self.metadata_extractor.is_valid_youtube_url(self.url):
                self.error_occurred.emit("No es una URL válida de YouTube")
                return
            
            # Extraer información del video
            video_info = self.metadata_extractor.get_video_info(self.url)
            if video_info:
                # Obtener duración
                duration = self.metadata_extractor.get_video_duration(self.url)
                if duration:
                    video_info['duration'] = duration
                
                self.page_analyzed.emit(video_info)
            else:
                self.error_occurred.emit("No se pudo extraer información del video")
                
        except Exception as e:
            self.error_occurred.emit(f"Error al analizar la página: {str(e)}")

class DownloadThread(QThread):
    progress = pyqtSignal(str)
    finished = pyqtSignal(bool, str)
    
    def __init__(self, url, output_path, audio_only=False, quality="best"):
        super().__init__()
        self.url = url
        self.output_path = output_path
        self.audio_only = audio_only
        self.quality = quality
        
    def run(self):
        try:
            comando = ["yt-dlp", self.url, "-o", str(self.output_path / "%(title)s.%(ext)s")]
            
            if self.audio_only:
                comando += ["-x", "--audio-format", "mp3"]
            else:
                # Agregar calidad de video
                if self.quality == "1080p":
                    comando += ["-f", "best[height<=1080]"]
                elif self.quality == "720p":
                    comando += ["-f", "best[height<=720]"]
                elif self.quality == "480p":
                    comando += ["-f", "best[height<=480]"]
                elif self.quality == "360p":
                    comando += ["-f", "best[height<=360]"]
                # "Mejor" usa la calidad por defecto de yt-dlp
                
            proceso = subprocess.Popen(comando, stdout=subprocess.PIPE, 
                                     stderr=subprocess.STDOUT, text=True)
            
            for linea in proceso.stdout:
                self.progress.emit(linea.strip())
                
            proceso.wait()
            
            if proceso.returncode == 0:
                self.finished.emit(True, "Descarga completada exitosamente")
            else:
                self.finished.emit(False, "Error durante la descarga")
                
        except Exception as e:
            self.finished.emit(False, f"Error: {str(e)}")

class YouTubeDownloaderGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.download_thread = None
        self.page_inspector = None
        self.metadata_extractor = YouTubeMetadataExtractor()
        self.current_video_info = None
        self.init_ui()
        self.apply_red_theme()
        
        # Timer para monitorear cambios de URL
        self.url_monitor_timer = QTimer()
        self.url_monitor_timer.timeout.connect(self.check_url_changes)
        self.url_monitor_timer.start(2000)  # Verificar cada 2 segundos
        
    def init_ui(self):
        self.setWindowTitle("YouTube Media Downloader - Navegador Integrado")
        self.setGeometry(100, 100, 1600, 1000)
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        main_layout = QHBoxLayout(central_widget)
        
        # Splitter principal
        splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(splitter)
        
        # Panel izquierdo - Navegador
        left_panel = self.create_browser_panel()
        splitter.addWidget(left_panel)
        
        # Panel derecho - Controles de descarga
        right_panel = self.create_download_panel()
        splitter.addWidget(right_panel)
        
        # Configurar proporciones del splitter
        splitter.setSizes([1000, 600])
        
    def create_browser_panel(self):
        panel = QFrame()
        panel.setFrameStyle(QFrame.Box)
        panel.setStyleSheet("QFrame { border: 2px solid #cc0000; border-radius: 8px; }")
        
        layout = QVBoxLayout(panel)
        
        # Barra de navegación
        nav_layout = QHBoxLayout()
        
        # Botones de navegación
        self.back_btn = QPushButton("◀")
        self.back_btn.setFixedSize(40, 40)
        self.back_btn.clicked.connect(self.go_back)
        
        self.forward_btn = QPushButton("▶")
        self.forward_btn.setFixedSize(40, 40)
        self.forward_btn.clicked.connect(self.go_forward)
        
        self.refresh_btn = QPushButton("🔄")
        self.refresh_btn.setFixedSize(40, 40)
        self.refresh_btn.clicked.connect(self.refresh_page)
        
        # Barra de URL
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Ingresa URL de YouTube...")
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        
        # Botón de ir
        self.go_btn = QPushButton("Ir")
        self.go_btn.clicked.connect(self.navigate_to_url)
        
        # Botón de análisis automático
        self.analyze_btn = QPushButton("🔍 Analizar")
        self.analyze_btn.clicked.connect(self.analyze_current_page)
        self.analyze_btn.setStyleSheet("""
            QPushButton {
                background-color: #0066cc;
                color: white;
                border: none;
                padding: 8px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0088ff;
            }
        """)
        
        nav_layout.addWidget(self.back_btn)
        nav_layout.addWidget(self.forward_btn)
        nav_layout.addWidget(self.refresh_btn)
        nav_layout.addWidget(self.url_bar)
        nav_layout.addWidget(self.go_btn)
        nav_layout.addWidget(self.analyze_btn)
        
        layout.addLayout(nav_layout)
        
        # Navegador web
        self.web_view = QWebEngineView()
        self.web_view.setPage(QWebEnginePage())
        
        # Cargar YouTube por defecto
        self.web_view.setUrl(QUrl("https://www.youtube.com"))
        self.url_bar.setText("https://www.youtube.com")
        
        # Conectar señales
        self.web_view.urlChanged.connect(self.url_changed)
        self.web_view.loadFinished.connect(self.page_loaded)
        
        layout.addWidget(self.web_view)
        
        return panel
        
    def create_download_panel(self):
        panel = QFrame()
        panel.setFrameStyle(QFrame.Box)
        panel.setStyleSheet("QFrame { border: 2px solid #cc0000; border-radius: 8px; background-color: #1a1a1a; }")
        
        layout = QVBoxLayout(panel)
        
        # Título del panel
        title_label = QLabel("🎥 Información del Video")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #ffffff; font-size: 18px; font-weight: bold; margin: 10px;")
        layout.addWidget(title_label)
        
        # Información del video
        self.video_info_frame = QFrame()
        self.video_info_frame.setStyleSheet("QFrame { background-color: #2a2a2a; border-radius: 6px; padding: 10px; }")
        self.video_info_frame.setVisible(False)
        video_info_layout = QVBoxLayout(self.video_info_frame)
        
        self.video_title_label = QLabel("Título: No disponible")
        self.video_title_label.setStyleSheet("color: #ffffff; font-size: 14px; font-weight: bold;")
        self.video_title_label.setWordWrap(True)
        
        self.video_author_label = QLabel("Autor: No disponible")
        self.video_author_label.setStyleSheet("color: #cccccc; font-size: 12px;")
        
        self.video_duration_label = QLabel("Duración: No disponible")
        self.video_duration_label.setStyleSheet("color: #cccccc; font-size: 12px;")
        
        self.video_id_label = QLabel("ID: No disponible")
        self.video_id_label.setStyleSheet("color: #cccccc; font-size: 12px;")
        
        video_info_layout.addWidget(self.video_title_label)
        video_info_layout.addWidget(self.video_author_label)
        video_info_layout.addWidget(self.video_duration_label)
        video_info_layout.addWidget(self.video_id_label)
        
        layout.addWidget(self.video_info_frame)
        
        # Estado de detección
        self.detection_status = QLabel("🔍 Esperando detección automática...")
        self.detection_status.setStyleSheet("color: #ffff00; font-size: 12px; padding: 5px; background-color: #2a2a2a; border-radius: 4px;")
        self.detection_status.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.detection_status)
        
        # URL actual
        self.current_url_label = QLabel("URL: No seleccionada")
        self.current_url_label.setStyleSheet("color: #cccccc; font-size: 12px; padding: 5px; background-color: #2a2a2a; border-radius: 4px;")
        self.current_url_label.setWordWrap(True)
        layout.addWidget(self.current_url_label)
        
        # Botón para capturar URL actual
        self.capture_btn = QPushButton("📋 Capturar URL Actual")
        self.capture_btn.setStyleSheet("""
            QPushButton {
                background-color: #cc0000;
                color: white;
                border: none;
                padding: 12px;
                border-radius: 6px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #ff0000;
            }
            QPushButton:pressed {
                background-color: #990000;
            }
        """)
        self.capture_btn.clicked.connect(self.capture_current_url)
        layout.addWidget(self.capture_btn)
        
        # Separador
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setStyleSheet("QFrame { background-color: #cc0000; }")
        layout.addWidget(separator)
        
        # Opciones de descarga
        options_label = QLabel("⚙️ Opciones de Descarga")
        options_label.setStyleSheet("color: #ffffff; font-size: 16px; font-weight: bold; margin: 10px;")
        layout.addWidget(options_label)
        
        # Tipo de descarga
        type_layout = QHBoxLayout()
        type_layout.addWidget(QLabel("Tipo:"))
        self.download_type = QComboBox()
        self.download_type.addItems(["🎥 Video Completo", "🎵 Solo Audio (MP3)", "🎬 Solo Video (sin audio)"])
        self.download_type.setStyleSheet("""
            QComboBox {
                background-color: #2a2a2a;
                color: white;
                border: 1px solid #cc0000;
                border-radius: 4px;
                padding: 8px;
                font-size: 14px;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox::down-arrow {
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 5px solid #cc0000;
            }
        """)
        type_layout.addWidget(self.download_type)
        layout.addLayout(type_layout)
        
        # Calidad
        quality_layout = QHBoxLayout()
        quality_layout.addWidget(QLabel("Calidad:"))
        self.quality_combo = QComboBox()
        self.quality_combo.addItems(["Mejor", "1080p", "720p", "480p", "360p"])
        self.quality_combo.setStyleSheet("""
            QComboBox {
                background-color: #2a2a2a;
                color: white;
                border: 1px solid #cc0000;
                border-radius: 4px;
                padding: 8px;
                font-size: 14px;
            }
        """)
        quality_layout.addWidget(self.quality_combo)
        layout.addLayout(quality_layout)
        
        # Directorio de destino
        dest_layout = QHBoxLayout()
        dest_layout.addWidget(QLabel("Destino:"))
        self.dest_path = QLineEdit()
        self.dest_path.setText(str(Path.home() / "Videos"))
        self.dest_path.setStyleSheet("""
            QLineEdit {
                background-color: #2a2a2a;
                color: white;
                border: 1px solid #cc0000;
                border-radius: 4px;
                padding: 8px;
                font-size: 14px;
            }
        """)
        dest_layout.addWidget(self.dest_path)
        
        self.browse_btn = QPushButton("📁")
        self.browse_btn.setFixedSize(40, 40)
        self.browse_btn.clicked.connect(self.browse_destination)
        self.browse_btn.setStyleSheet("""
            QPushButton {
                background-color: #cc0000;
                color: white;
                border: none;
                border-radius: 4px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #ff0000;
            }
        """)
        dest_layout.addWidget(self.browse_btn)
        layout.addLayout(dest_layout)
        
        # Botón de descarga
        self.download_btn = QPushButton("🚀 INICIAR DESCARGA")
        self.download_btn.setStyleSheet("""
            QPushButton {
                background-color: #00cc00;
                color: white;
                border: none;
                padding: 15px;
                border-radius: 8px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #00ff00;
            }
            QPushButton:pressed {
                background-color: #009900;
            }
            QPushButton:disabled {
                background-color: #666666;
                color: #cccccc;
            }
        """)
        self.download_btn.clicked.connect(self.start_download)
        self.download_btn.setEnabled(False)
        layout.addWidget(self.download_btn)
        
        # Barra de progreso
        self.progress_bar = QProgressBar()
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #cc0000;
                border-radius: 5px;
                text-align: center;
                background-color: #2a2a2a;
            }
            QProgressBar::chunk {
                background-color: #cc0000;
                border-radius: 3px;
            }
        """)
        self.progress_bar.setVisible(False)
        layout.addWidget(self.progress_bar)
        
        # Log de descarga
        log_label = QLabel("📋 Log de Actividad")
        log_label.setStyleSheet("color: #ffffff; font-size: 14px; font-weight: bold; margin: 5px;")
        layout.addWidget(log_label)
        
        self.log_text = QTextEdit()
        self.log_text.setStyleSheet("""
            QTextEdit {
                background-color: #2a2a2a;
                color: #00ff00;
                border: 1px solid #cc0000;
                border-radius: 4px;
                font-family: 'Courier New', monospace;
                font-size: 12px;
            }
        """)
        self.log_text.setMaximumHeight(200)
        layout.addWidget(self.log_text)
        
        # SVG decorativo (simulado con texto)
        svg_label = QLabel("🎬")
        svg_label.setAlignment(Qt.AlignCenter)
        svg_label.setStyleSheet("font-size: 48px; margin: 20px;")
        layout.addWidget(svg_label)
        
        # Espaciador para empujar todo hacia arriba
        layout.addStretch()
        
        return panel
        
    def apply_red_theme(self):
        # Aplicar tema rojo a toda la aplicación
        app = QApplication.instance()
        if app:
            palette = QPalette()
            
            # Colores del tema rojo
            palette.setColor(QPalette.Window, QColor(26, 26, 26))
            palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
            palette.setColor(QPalette.Base, QColor(42, 42, 42))
            palette.setColor(QPalette.AlternateBase, QColor(66, 66, 66))
            palette.setColor(QPalette.ToolTipBase, QColor(204, 0, 0))
            palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
            palette.setColor(QPalette.Text, QColor(255, 255, 255))
            palette.setColor(QPalette.Button, QColor(204, 0, 0))
            palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
            palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
            palette.setColor(QPalette.Link, QColor(255, 100, 100))
            palette.setColor(QPalette.Highlight, QColor(204, 0, 0))
            palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
            
            app.setPalette(palette)
            
            # Estilo global
            app.setStyleSheet("""
                QMainWindow {
                    background-color: #1a1a1a;
                }
                QLabel {
                    color: #ffffff;
                }
                QLineEdit {
                    background-color: #2a2a2a;
                    color: white;
                    border: 1px solid #cc0000;
                    border-radius: 4px;
                    padding: 8px;
                }
                QPushButton {
                    background-color: #cc0000;
                    color: white;
                    border: none;
                    padding: 10px;
                    border-radius: 5px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #ff0000;
                }
                QPushButton:pressed {
                    background-color: #990000;
                }
            """)
    
    def go_back(self):
        self.web_view.back()
        
    def go_forward(self):
        self.web_view.forward()
        
    def refresh_page(self):
        self.web_view.reload()
        
    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        self.web_view.setUrl(QUrl(url))
        
    def url_changed(self, url):
        self.url_bar.setText(url.toString())
        self.current_url_label.setText(f"URL: {url.toString()}")
        
        # Verificar si es una URL válida de YouTube
        if self.metadata_extractor.is_valid_youtube_url(url.toString()):
            self.download_btn.setEnabled(True)
            self.capture_btn.setStyleSheet("""
                QPushButton {
                    background-color: #00cc00;
                    color: white;
                    border: none;
                    padding: 12px;
                    border-radius: 6px;
                    font-size: 14px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #00ff00;
                }
                QPushButton:pressed {
                    background-color: #009900;
                }
            """)
            
            # Extraer información del video
            self.extract_video_metadata(url.toString())
        else:
            self.download_btn.setEnabled(False)
            self.capture_btn.setStyleSheet("""
                QPushButton {
                    background-color: #666666;
                    color: #cccccc;
                    border: none;
                    padding: 12px;
                    border-radius: 6px;
                    font-size: 14px;
                    font-weight: bold;
                }
            """)
            
            # Ocultar información del video
            self.video_info_frame.setVisible(False)
        
    def page_loaded(self, success):
        if success:
            self.log_text.append("✅ Página cargada correctamente")
        else:
            self.log_text.append("❌ Error al cargar la página")
            
    def capture_current_url(self):
        current_url = self.web_view.url().toString()
        if "youtube.com" in current_url or "youtu.be" in current_url:
            self.log_text.append(f"📋 URL capturada: {current_url}")
            self.current_url_label.setText(f"URL: {current_url}")
        else:
            self.log_text.append("⚠️ La página actual no parece ser de YouTube")
            
    def browse_destination(self):
        folder = QFileDialog.getExistingDirectory(self, "Seleccionar directorio de destino")
        if folder:
            self.dest_path.setText(folder)
            
    def start_download(self):
        current_url = self.web_view.url().toString()
        if not current_url or ("youtube.com" not in current_url and "youtu.be" not in current_url):
            QMessageBox.warning(self, "Error", "Por favor, navega a un video de YouTube primero.")
            return
            
        # Obtener opciones
        download_type = self.download_type.currentText()
        quality = self.quality_combo.currentText()
        dest_path = Path(self.dest_path.text())
        
        # Crear directorio si no existe
        dest_path.mkdir(parents=True, exist_ok=True)
        
        # Determinar si es solo audio
        audio_only = "Solo Audio" in download_type
        
        # Configurar barra de progreso
        self.progress_bar.setVisible(True)
        self.progress_bar.setRange(0, 0)  # Modo indeterminado
        
        # Deshabilitar controles durante la descarga
        self.download_btn.setEnabled(False)
        self.capture_btn.setEnabled(False)
        
        # Iniciar hilo de descarga
        self.download_thread = DownloadThread(current_url, dest_path, audio_only, quality)
        self.download_thread.progress.connect(self.update_log)
        self.download_thread.finished.connect(self.download_finished)
        self.download_thread.start()
        
        self.log_text.append("🚀 Iniciando descarga...")
        
    def update_log(self, message):
        self.log_text.append(message)
        # Auto-scroll al final
        self.log_text.verticalScrollBar().setValue(
            self.log_text.verticalScrollBar().maximum()
        )
        
    def download_finished(self, success, message):
        self.progress_bar.setVisible(False)
        self.download_btn.setEnabled(True)
        self.capture_btn.setEnabled(True)
        
        if success:
            self.log_text.append(f"✅ {message}")
            QMessageBox.information(self, "Éxito", message)
        else:
            self.log_text.append(f"❌ {message}")
            QMessageBox.critical(self, "Error", message)

    def extract_video_metadata(self, url):
        """Extrae metadatos del video de YouTube"""
        try:
            self.log_text.append("🔍 Extrayendo información del video...")
            
            # Obtener información básica
            video_info = self.metadata_extractor.get_video_info(url)
            
            if video_info:
                # Mostrar información del video
                self.video_title_label.setText(f"Título: {video_info['title']}")
                self.video_author_label.setText(f"Autor: {video_info['author']}")
                
                # Obtener duración
                duration = self.metadata_extractor.get_video_duration(url)
                if duration:
                    self.video_duration_label.setText(f"Duración: {duration}")
                else:
                    self.video_duration_label.setText("Duración: No disponible")
                
                # Mostrar el frame de información
                self.video_info_frame.setVisible(True)
                
                self.log_text.append(f"✅ Información extraída: {video_info['title']}")
            else:
                self.video_info_frame.setVisible(False)
                self.log_text.append("⚠️ No se pudo extraer información del video")
                
        except Exception as e:
            self.log_text.append(f"❌ Error al extraer metadatos: {str(e)}")
            self.video_info_frame.setVisible(False)

    def check_url_changes(self):
        """Verifica cambios en la URL y analiza automáticamente"""
        current_url = self.web_view.url().toString()
        
        # Solo analizar si la URL cambió y es de YouTube
        if (self.metadata_extractor.is_valid_youtube_url(current_url) and 
            current_url != getattr(self, '_last_analyzed_url', '')):
            
            self._last_analyzed_url = current_url
            self.log_text.append("🔄 URL cambiada, analizando automáticamente...")
            self.analyze_current_page()
    
    def analyze_current_page(self):
        """Analiza la página actual para extraer información"""
        current_url = self.web_view.url().toString()
        
        if not current_url:
            self.log_text.append("⚠️ No hay URL para analizar")
            return
        
        # Detener análisis anterior si existe
        if self.page_inspector and self.page_inspector.isRunning():
            self.page_inspector.terminate()
            self.page_inspector.wait()
        
        # Crear nuevo inspector
        self.page_inspector = WebPageInspector(current_url)
        self.page_inspector.page_analyzed.connect(self.on_page_analyzed)
        self.page_inspector.error_occurred.connect(self.on_page_analysis_error)
        
        # Actualizar estado
        self.detection_status.setText("🔍 Analizando página...")
        self.detection_status.setStyleSheet("color: #ffff00; font-size: 12px; padding: 5px; background-color: #2a2a2a; border-radius: 4px;")
        
        self.log_text.append("🔍 Iniciando análisis de la página...")
        self.page_inspector.start()
    
    def on_page_analyzed(self, video_info):
        """Callback cuando se completa el análisis de la página"""
        self.current_video_info = video_info
        
        # Mostrar información del video
        self.video_title_label.setText(f"Título: {video_info['title']}")
        self.video_author_label.setText(f"Autor: {video_info['author']}")
        self.video_id_label.setText(f"ID: {video_info['video_id']}")
        
        if 'duration' in video_info:
            self.video_duration_label.setText(f"Duración: {video_info['duration']}")
        else:
            self.video_duration_label.setText("Duración: No disponible")
        
        # Mostrar el frame de información
        self.video_info_frame.setVisible(True)
        
        # Actualizar estado
        self.detection_status.setText("✅ Video detectado automáticamente")
        self.detection_status.setStyleSheet("color: #00ff00; font-size: 12px; padding: 5px; background-color: #2a2a2a; border-radius: 4px;")
        
        # Habilitar botón de descarga
        self.download_btn.setEnabled(True)
        
        self.log_text.append(f"✅ Video detectado: {video_info['title']}")
        self.log_text.append(f"   Autor: {video_info['author']}")
        if 'duration' in video_info:
            self.log_text.append(f"   Duración: {video_info['duration']}")
    
    def on_page_analysis_error(self, error_message):
        """Callback cuando hay error en el análisis"""
        self.detection_status.setText("❌ Error en detección")
        self.detection_status.setStyleSheet("color: #ff0000; font-size: 12px; padding: 5px; background-color: #2a2a2a; border-radius: 4px;")
        
        self.log_text.append(f"❌ Error: {error_message}")
        
        # Ocultar información del video
        self.video_info_frame.setVisible(False)
        
        # Deshabilitar botón de descarga
        self.download_btn.setEnabled(False)

def main():
    app = QApplication(sys.argv)
    
    # Verificar si yt-dlp está instalado
    try:
        subprocess.run(["yt-dlp", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        QMessageBox.critical(None, "Error", 
                           "yt-dlp no está instalado. Por favor, instálalo primero:\n"
                           "pip install yt-dlp")
        sys.exit(1)
    
    window = YouTubeDownloaderGUI()
    window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
