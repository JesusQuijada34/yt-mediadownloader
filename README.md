# YouTube Media Downloader 🎬

Una aplicación de escritorio moderna y elegante para descargar contenido de YouTube con una interfaz gráfica intuitiva.

## ✨ Características

- 🌐 **Navegador integrado**: Navega directamente por YouTube desde la aplicación
- 🎯 **Detección automática**: Detecta automáticamente videos de YouTube mientras navegas
- 📊 **Extracción de metadatos**: Obtiene título, autor, duración y descripción en tiempo real
- 🎥 **Descarga de video**: Descarga videos en múltiples calidades (360p, 480p, 720p, 1080p)
- 🎵 **Extracción de audio**: Convierte videos a MP3 automáticamente
- 🎨 **Interfaz moderna**: Diseño elegante con tema rojo personalizable
- 📁 **Gestión de archivos**: Selecciona fácilmente el directorio de destino
- 📊 **Log en tiempo real**: Monitorea el progreso de las descargas y detección
- 🚀 **Rendimiento optimizado**: Descargas en segundo plano sin bloquear la interfaz
- 🛠️ **Bibliotecas nativas**: Usa solo Python estándar para extracción de datos

## 🖼️ Capturas de pantalla

La aplicación presenta un diseño de dos paneles:
- **Panel izquierdo**: Navegador web integrado para YouTube
- **Panel derecho**: Controles de descarga y configuración

## 🚀 Instalación

### Requisitos previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)
- Conexión a internet

### Instalación automática

#### Linux/macOS
```bash
chmod +x autorun
./autorun
```

#### Windows
```cmd
autorun.bat
```

### Instalación manual

1. **Clona o descarga el repositorio**
```bash
git clone https://github.com/tu-usuario/yt-mediadownloader.git
cd yt-mediadownloader
```

2. **Instala las dependencias**
```bash
pip install -r lib/requirements.txt
```

3. **Ejecuta la aplicación**
```bash
python yt-mediadownloader.py
```

## 📦 Dependencias

### **Interfaz Gráfica**
- **PyQt5**: Framework de interfaz gráfica
- **PyQtWebEngine**: Motor web integrado

### **Descarga de Medios**
- **yt-dlp**: Herramienta de descarga de YouTube (fork mejorado de youtube-dl)

### **Extracción de Datos (Nativas de Python)**
- **urllib**: Requests HTTP y parsing de URLs
- **re**: Expresiones regulares para validación
- **json**: Procesamiento de respuestas de API
- **html.parser**: Análisis de contenido HTML

## 🎯 Uso

### **Modo Automático (Recomendado)**
1. **Ejecuta la aplicación**
2. **Navega por YouTube** usando el navegador integrado
3. **El sistema detecta automáticamente** cuando entras a un video
4. **La información se extrae y muestra** en tiempo real (título, autor, duración)
5. **Configura las opciones** de descarga si es necesario
6. **Haz clic en "INICIAR DESCARGA"**
7. **Monitorea el progreso** en el log en tiempo real

### **Modo Manual**
- Usa el botón **"🔍 Analizar"** para forzar el análisis de la página actual
- Útil cuando la detección automática no funciona o quieres actualizar la información

## ⚙️ Configuración

### Tipos de descarga
- **🎥 Video Completo**: Descarga el video con audio
- **🎵 Solo Audio (MP3)**: Extrae solo el audio en formato MP3
- **🎬 Solo Video (sin audio)**: Descarga solo el video sin audio

### Calidades disponibles
- **Mejor**: Calidad automática (recomendado)
- **1080p**: Alta definición
- **720p**: Definición estándar
- **480p**: Calidad media
- **360p**: Calidad baja

## 🔧 Solución de problemas

### **Errores de Dependencias**
```bash
# Error: "yt-dlp no está instalado"
pip install yt-dlp

# Error: "PyQt5 no está instalado"
pip install PyQt5 PyQtWebEngine
```

### **Problemas de la Aplicación**
- **La aplicación no se inicia**: Verifica que tienes Python 3.7+ y todas las dependencias instaladas
- **Revisa los logs de error** en la consola para más detalles

### **Problemas de Descarga**
- **Las descargas fallan**: Verifica tu conexión a internet y permisos de escritura
- **URL no válida**: Asegúrate de que estés en una página de video de YouTube

### **Problemas de Detección Automática**
- **No detecta videos**: Verifica que la página sea un video individual de YouTube
- **Información incompleta**: Algunos videos pueden tener metadatos limitados
- **Usa el botón "🔍 Analizar"** para forzar el análisis manual

## 🐛 Reportar problemas

Si encuentras algún problema o tienes una sugerencia:

1. Verifica que el problema no esté ya reportado en [Issues](../../issues)
2. Crea un nuevo issue con:
   - Descripción detallada del problema
   - Pasos para reproducirlo
   - Información del sistema (SO, versión de Python)
   - Capturas de pantalla si es relevante

## 🤝 Contribuir

Las contribuciones son bienvenidas:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

**influent** - Desarrollador principal

## 🙏 Agradecimientos

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) por la herramienta de descarga
- [PyQt](https://www.riverbankcomputing.com/software/pyqt/) por el framework de interfaz
- [YouTube oEmbed API](https://oembed.com/) por proporcionar metadatos de videos
- Comunidad de desarrolladores de código abierto

## 📚 Documentación Adicional

- [DETECCION_AUTOMATICA.md](DETECCION_AUTOMATICA.md) - Sistema de detección automática
- [CHANGELOG.md](CHANGELOG.md) - Historial de cambios
- [test_installation.py](test_installation.py) - Script de verificación de instalación
- [youtube_native_scraper.py](youtube_native_scraper.py) - Script independiente de scraping

## 📈 Roadmap

### **Funcionalidades Principales**
- [ ] Soporte para más plataformas (Vimeo, Dailymotion, etc.)
- [ ] Descargas en lote
- [ ] Programación de descargas
- [ ] Interfaz en múltiples idiomas
- [ ] Temas personalizables

### **Mejoras de Detección**
- [ ] Detección de playlists completas
- [ ] Análisis de comentarios populares
- [ ] Detección automática de calidad disponible
- [ ] Cache inteligente de metadatos

### **Integración y Optimización**
- [ ] Integración con gestores de descarga externos
- [ ] Procesamiento asíncrono para mejor rendimiento
- [ ] Rate limiting para evitar bloqueos
- [ ] Sistema de reintentos automáticos

---

⭐ **Si este proyecto te es útil, por favor dale una estrella en GitHub!**
