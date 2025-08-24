# YouTube Media Downloader 🎬

Una aplicación de escritorio moderna y elegante para descargar contenido de YouTube con una interfaz gráfica intuitiva.

## ✨ Características

- 🌐 **Navegador integrado**: Navega directamente por YouTube desde la aplicación
- 🎥 **Descarga de video**: Descarga videos en múltiples calidades (360p, 480p, 720p, 1080p)
- 🎵 **Extracción de audio**: Convierte videos a MP3 automáticamente
- 🎨 **Interfaz moderna**: Diseño elegante con tema rojo personalizable
- 📁 **Gestión de archivos**: Selecciona fácilmente el directorio de destino
- 📊 **Log en tiempo real**: Monitorea el progreso de las descargas
- 🚀 **Rendimiento optimizado**: Descargas en segundo plano sin bloquear la interfaz

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

- **PyQt5**: Framework de interfaz gráfica
- **PyQtWebEngine**: Motor web integrado
- **yt-dlp**: Herramienta de descarga de YouTube (fork mejorado de youtube-dl)

## 🎯 Uso

1. **Ejecuta la aplicación**
2. **Navega a YouTube** usando el navegador integrado
3. **Selecciona un video** que quieras descargar
4. **Configura las opciones**:
   - Tipo de descarga (video completo, solo audio, solo video)
   - Calidad del video
   - Directorio de destino
5. **Haz clic en "INICIAR DESCARGA"**
6. **Monitorea el progreso** en el log en tiempo real

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

### Error: "yt-dlp no está instalado"
```bash
pip install yt-dlp
```

### Error: "PyQt5 no está instalado"
```bash
pip install PyQt5 PyQtWebEngine
```

### La aplicación no se inicia
- Verifica que tienes Python 3.7+
- Asegúrate de que todas las dependencias estén instaladas
- Revisa los logs de error en la consola

### Las descargas fallan
- Verifica tu conexión a internet
- Asegúrate de que la URL de YouTube sea válida
- Comprueba que tienes permisos de escritura en el directorio de destino

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
- Comunidad de desarrolladores de código abierto

## 📈 Roadmap

- [ ] Soporte para más plataformas (Vimeo, Dailymotion, etc.)
- [ ] Descargas en lote
- [ ] Programación de descargas
- [ ] Interfaz en múltiples idiomas
- [ ] Temas personalizables
- [ ] Integración con gestores de descarga externos

---

⭐ **Si este proyecto te es útil, por favor dale una estrella en GitHub!**
