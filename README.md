# 🎬 YouTube Media Downloader

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-green.svg)](https://www.riverbankcomputing.com/software/pyqt/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/influent/yt-mediadownloader)

> **Una aplicación de escritorio moderna y elegante para descargar contenido multimedia de YouTube con interfaz gráfica intuitiva.**

## 📋 Tabla de Contenidos

- [🎯 Descripción General](#-descripción-general)
- [✨ Características Principales](#-características-principales)
- [🖥️ Capturas de Pantalla](#️-capturas-de-pantalla)
- [🚀 Instalación Rápida](#-instalación-rápida)
- [📦 Instalación Detallada](#-instalación-detallada)
- [🔧 Configuración](#-configuración)
- [📖 Guía de Uso](#-guía-de-uso)
- [🏗️ Arquitectura del Proyecto](#️-arquitectura-del-proyecto)
- [🔬 Análisis Técnico](#-análisis-técnico)
- [📚 Investigación y Contexto](#-investigación-y-contexto)
- [🤝 Contribución](#-contribución)
- [📄 Licencia](#-licencia)
- [📞 Soporte](#-soporte)

## 🎯 Descripción General

**YouTube Media Downloader** es una aplicación de escritorio desarrollada en Python que permite a los usuarios descargar videos y audio de YouTube de manera sencilla y eficiente. La aplicación combina la potencia de un navegador web embebido con herramientas especializadas de descarga, ofreciendo una experiencia de usuario fluida e intuitiva.

### 🎨 Filosofía de Diseño

- **Simplicidad**: Interfaz limpia y fácil de usar
- **Eficiencia**: Descargas rápidas y optimizadas
- **Flexibilidad**: Múltiples formatos y opciones de descarga
- **Accesibilidad**: Diseño responsive y accesible para todos los usuarios

## ✨ Características Principales

### 🌐 Navegador Embebido
- **Navegación integrada**: Acceso directo a YouTube desde la aplicación
- **Detección automática**: Identificación instantánea de URLs de videos
- **Historial de navegación**: Seguimiento de videos visitados

### 📥 Sistema de Descarga
- **Descarga de video**: Obtiene la mejor calidad disponible
- **Extracción de audio**: Conversión automática a formato MP3
- **Múltiples resoluciones**: Selección de calidad según preferencias
- **Gestión de archivos**: Organización automática de descargas

### 🎛️ Interfaz de Usuario
- **Panel lateral intuitivo**: Controles de descarga siempre visibles
- **Información en tiempo real**: Título, duración y metadatos del video
- **Notificaciones**: Alertas de éxito y error durante las descargas
- **Tema adaptable**: Interfaz que se adapta al sistema operativo

## 🖥️ Capturas de Pantalla

> *Nota: Las capturas de pantalla se mostrarán aquí una vez que la aplicación esté en funcionamiento*

## 🚀 Instalación Rápida

### Requisitos Previos
- **Python 3.7 o superior**
- **Sistema operativo**: Windows 10+, macOS 10.14+, Ubuntu 18.04+

### Comando de Instalación
```bash
# Clonar el repositorio
git clone https://github.com/influent/yt-mediadownloader.git
cd yt-mediadownloader

# Instalar dependencias
pip install -r lib/requirements.txt

# Ejecutar la aplicación
python yt-mediadownloader.py
```

## 📦 Instalación Detallada

### Paso 1: Preparación del Sistema

#### Windows
```bash
# Instalar Python desde python.org
# Verificar instalación
python --version
pip --version

# Instalar Visual C++ Build Tools (si es necesario)
# Descargar desde: https://visualstudio.microsoft.com/visual-cpp-build-tools/
```

#### macOS
```bash
# Instalar Homebrew (si no está instalado)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar Python
brew install python

# Verificar instalación
python3 --version
pip3 --version
```

#### Linux (Ubuntu/Debian)
```bash
# Actualizar sistema
sudo apt update && sudo apt upgrade

# Instalar Python y pip
sudo apt install python3 python3-pip python3-venv

# Instalar dependencias del sistema para PyQt5
sudo apt install python3-pyqt5 python3-pyqt5.qtwebengine

# Verificar instalación
python3 --version
pip3 --version
```

### Paso 2: Configuración del Entorno Virtual (Recomendado)

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# Verificar que esté activado
which python
```

### Paso 3: Instalación de Dependencias

```bash
# Instalar dependencias principales
pip install PyQt5 PyQtWebEngine pytube

# O instalar desde requirements.txt
pip install -r lib/requirements.txt

# Verificar instalación
pip list
```

### Paso 4: Verificación de la Instalación

```bash
# Probar importación de módulos
python -c "import PyQt5; import PyQt5.QtWebEngineWidgets; import pytube; print('✅ Todas las dependencias están instaladas correctamente')"
```

## 🔧 Configuración

### Archivo de Configuración
La aplicación puede ser configurada mediante variables de entorno o archivos de configuración:

```bash
# Variables de entorno (opcionales)
export YT_DOWNLOAD_PATH="/path/to/downloads"
export YT_DEFAULT_QUALITY="720p"
export YT_AUTO_CONVERT_MP3="true"
```

### Configuración del Navegador
- **User-Agent personalizado**: Para evitar restricciones de YouTube
- **Proxy configurable**: Para entornos corporativos o con restricciones geográficas
- **Cookies persistentes**: Para mantener sesiones de usuario

## 📖 Guía de Uso

### Primeros Pasos

1. **Iniciar la aplicación**
   ```bash
   python yt-mediadownloader.py
   ```

2. **Navegar a YouTube**
   - La aplicación se abre automáticamente en YouTube
   - Navega normalmente como en cualquier navegador

3. **Seleccionar un video**
   - Haz clic en cualquier video de YouTube
   - La URL se detectará automáticamente
   - El título aparecerá en el panel lateral

4. **Descargar contenido**
   - **Video**: Haz clic en "📥 Descargar Video"
   - **Audio**: Haz clic en "🎧 Descargar Audio (MP3)"

### Funciones Avanzadas

#### Descarga por URL Directa
```python
# Puedes pegar URLs directamente en el campo de URL
# La aplicación procesará automáticamente el video
```

#### Gestión de Calidad
- **Video**: Se descarga automáticamente en la mejor calidad disponible
- **Audio**: Se extrae en la mejor calidad de audio disponible

#### Historial de Descargas
- Cada video visitado se añade al historial
- Acceso rápido a videos previamente procesados

## 🏗️ Arquitectura del Proyecto

### Estructura de Directorios
```
yt-mediadownloader/
├── yt-mediadownloader.py      # Archivo principal de la aplicación
├── lib/
│   └── requirements.txt       # Dependencias del proyecto
├── app/                       # Recursos de la aplicación
├── assets/                    # Imágenes y recursos gráficos
├── config/                    # Archivos de configuración
├── docs/                      # Documentación adicional
├── source/                    # Código fuente adicional
├── setup.py                   # Script de instalación
├── autorun                    # Script de ejecución automática (Linux/macOS)
├── autorun.bat               # Script de ejecución automática (Windows)
├── README.md                  # Este archivo
├── CHANGELOG.md              # Historial de cambios
└── LICENSE                    # Licencia del proyecto
```

### Componentes Principales

#### 1. Interfaz de Usuario (PyQt5)
- **QWidget**: Ventana principal de la aplicación
- **QWebEngineView**: Navegador web embebido
- **QVBoxLayout/QHBoxLayout**: Organización de elementos de la interfaz

#### 2. Motor de Descarga (pytube)
- **YouTube**: Clase principal para manejo de videos
- **Stream**: Gestión de diferentes calidades de video/audio
- **Download**: Proceso de descarga de archivos

#### 3. Sistema de Navegación
- **QWebEngineView**: Renderizado de páginas web
- **QUrl**: Manejo de URLs y navegación
- **Signal/Slot**: Comunicación entre componentes

## 🔬 Análisis Técnico

### Tecnologías Utilizadas

#### PyQt5
- **Framework de GUI**: Interfaz gráfica moderna y responsive
- **Licencia**: GPL v3 (comercial) o LGPL v3 (open source)
- **Ventajas**: Multiplataforma, rendimiento nativo, documentación extensa
- **Alternativas**: Tkinter (Python nativo), Kivy (móvil), wxPython

#### PyQtWebEngine
- **Motor web**: Basado en Chromium/Blink
- **Capacidades**: HTML5, CSS3, JavaScript moderno
- **Integración**: Perfecta integración con PyQt5
- **Consideraciones**: Tamaño de descarga mayor, dependencias del sistema

#### pytube
- **Biblioteca de descarga**: Especializada en YouTube
- **Características**: Extracción de metadatos, múltiples formatos
- **Mantenimiento**: Activamente desarrollada y actualizada
- **Alternativas**: yt-dlp, youtube-dl

### Patrones de Diseño

#### Modelo-Vista-Controlador (MVC)
- **Modelo**: Lógica de descarga y metadatos (pytube)
- **Vista**: Interfaz de usuario (PyQt5 widgets)
- **Controlador**: Manejo de eventos y coordinación

#### Observer Pattern
- **Signal/Slot**: Sistema de eventos de PyQt5
- **URL Detection**: Notificación automática de cambios de URL
- **Download Progress**: Seguimiento del estado de descargas

#### Factory Pattern
- **Stream Selection**: Creación de objetos de descarga según tipo
- **Format Conversion**: Generación de conversores de formato

### Consideraciones de Rendimiento

#### Optimizaciones Implementadas
- **Lazy Loading**: Carga de metadatos solo cuando es necesario
- **Async Operations**: Operaciones de descarga no bloqueantes
- **Memory Management**: Gestión eficiente de recursos del navegador

#### Escalabilidad
- **Modular Design**: Fácil adición de nuevas funcionalidades
- **Plugin System**: Arquitectura extensible para formatos adicionales
- **Configuration**: Sistema de configuración flexible

## 📚 Investigación y Contexto

### Contexto Histórico

#### Evolución de YouTube
- **2005**: Fundación de YouTube como plataforma de videos
- **2006**: Adquisición por Google
- **2010s**: Expansión a múltiples formatos y resoluciones
- **2020s**: Enfoque en contenido premium y restricciones

#### Cambios en Políticas de Descarga
- **Términos de Servicio**: Restricciones legales y técnicas
- **DRM**: Protección de contenido digital
- **Geoblocking**: Restricciones geográficas
- **Rate Limiting**: Limitaciones de velocidad de descarga

### Aspectos Legales y Éticos

#### Consideraciones Legales
- **Derechos de Autor**: Respeto a la propiedad intelectual
- **Uso Justo**: Excepciones para investigación y educación
- **Licencias Creative Commons**: Contenido con permisos de reutilización
- **Jurisdicción**: Diferentes leyes por país

#### Uso Ético
- **Educación**: Aprendizaje y investigación académica
- **Preservación**: Archivo de contenido histórico
- **Accesibilidad**: Contenido offline para áreas con conectividad limitada
- **Backup Personal**: Respaldo de contenido propio

### Investigación Académica

#### Aplicaciones de Investigación
- **Análisis de Contenido**: Estudio de tendencias y patrones
- **Lingüística**: Análisis de transcripciones y subtítulos
- **Sociología**: Investigación de comportamiento en redes sociales
- **Educación**: Creación de recursos educativos offline

#### Metodologías de Investigación
- **Análisis Cuantitativo**: Estadísticas de visualización y engagement
- **Análisis Cualitativo**: Contenido y contexto de videos
- **Análisis Temporal**: Evolución de tendencias a lo largo del tiempo
- **Análisis Comparativo**: Comparación entre diferentes canales o épocas

### Tendencias Tecnológicas

#### Inteligencia Artificial
- **Reconocimiento de Contenido**: Detección automática de temas
- **Generación de Subtítulos**: Transcripción automática
- **Análisis de Sentimientos**: Evaluación de reacciones del público
- **Recomendaciones**: Algoritmos de sugerencia de contenido

#### Realidad Virtual y Aumentada
- **Contenido 360°**: Videos inmersivos
- **Streaming en Vivo**: Transmisiones en tiempo real
- **Interactividad**: Contenido que responde a la interacción del usuario

## 🤝 Contribución

### Cómo Contribuir

1. **Fork del repositorio**
2. **Crear una rama para tu feature**
3. **Realizar cambios y commits**
4. **Crear un Pull Request**

### Áreas de Contribución

#### Desarrollo
- **Nuevas funcionalidades**: Formatos adicionales, mejoras de UI
- **Optimizaciones**: Mejoras de rendimiento y eficiencia
- **Testing**: Pruebas unitarias y de integración
- **Documentación**: Mejoras en la documentación

#### Diseño
- **Interfaz de usuario**: Mejoras en la experiencia del usuario
- **Iconografía**: Diseño de iconos y elementos visuales
- **Temas**: Nuevos esquemas de color y estilos

#### Investigación
- **Análisis de tendencias**: Investigación sobre nuevas funcionalidades
- **Estudios de usuario**: Feedback y mejoras basadas en uso real
- **Benchmarking**: Comparación con herramientas similares

### Guías de Contribución

#### Estándares de Código
- **PEP 8**: Estilo de código Python
- **Type Hints**: Anotaciones de tipo para mejor documentación
- **Docstrings**: Documentación inline del código
- **Testing**: Cobertura de pruebas mínima del 80%

#### Proceso de Review
- **Code Review**: Revisión obligatoria de cambios
- **Testing**: Verificación de que las pruebas pasen
- **Documentation**: Actualización de documentación relacionada
- **Changelog**: Registro de cambios en CHANGELOG.md

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

### Licencias de Dependencias

- **PyQt5**: GPL v3 o LGPL v3
- **pytube**: MIT License
- **PyQtWebEngine**: GPL v3 o LGPL v3

## 📞 Soporte

### Canales de Soporte

- **Issues de GitHub**: [Reportar bugs o solicitar features](https://github.com/influent/yt-mediadownloader/issues)
- **Discussions**: [Foro de discusión y preguntas](https://github.com/influent/yt-mediadownloader/discussions)
- **Wiki**: [Documentación adicional y tutoriales](https://github.com/influent/yt-mediadownloader/wiki)

### Recursos Adicionales

- **Documentación de PyQt5**: [https://doc.qt.io/qtforpython/](https://doc.qt.io/qtforpython/)
- **Documentación de pytube**: [https://pytube.io/](https://pytube.io/)
- **Comunidad Python**: [https://www.python.org/community/](https://www.python.org/community/)

### FAQ Frecuentes

#### Problemas Comunes

**Q: La aplicación no se inicia**
A: Verifica que Python 3.7+ esté instalado y que todas las dependencias estén instaladas correctamente.

**Q: Error al descargar videos**
A: YouTube actualiza frecuentemente su sistema. Actualiza pytube con `pip install --upgrade pytube`.

**Q: Problemas con PyQt5 en Linux**
A: Instala los paquetes del sistema: `sudo apt install python3-pyqt5 python3-pyqt5.qtwebengine`.

---

## 🎉 ¡Gracias por usar YouTube Media Downloader!

Si este proyecto te ha sido útil, considera:
- ⭐ Dar una estrella al repositorio
- 🐛 Reportar bugs o problemas
- 💡 Sugerir nuevas funcionalidades
- 🤝 Contribuir al desarrollo

**Desarrollado con ❤️ por la comunidad open source**
