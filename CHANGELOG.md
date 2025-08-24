# Changelog

Todas las notables mejoras y cambios en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere al [Versionado Semántico](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Soporte para múltiples calidades de video (360p, 480p, 720p, 1080p)
- Mejoras en la interfaz de usuario con tema rojo personalizable
- Log en tiempo real para monitorear descargas
- Navegador web integrado para YouTube
- Captura automática de URLs de YouTube
- Selección de directorio de destino personalizable

### Changed
- Refactorización completa del código para mejor mantenibilidad
- Mejoras en el manejo de errores y excepciones
- Optimización del rendimiento de las descargas
- Actualización de dependencias a versiones más recientes

### Fixed
- Corrección de problemas de compatibilidad con PyQt5
- Eliminación de importaciones no utilizadas
- Corrección de referencias de archivos en scripts de instalación
- Mejora en la validación de URLs de YouTube

## [1.0.0] - 2024-12-19

### Added
- Interfaz gráfica completa con PyQt5
- Navegador web integrado usando PyQtWebEngine
- Sistema de descarga basado en yt-dlp
- Soporte para descarga de video y extracción de audio
- Interfaz de dos paneles (navegador + controles)
- Tema visual personalizable
- Scripts de instalación automática para Linux/macOS y Windows

### Technical Details
- **Python**: 3.7+
- **GUI Framework**: PyQt5 5.15.9+
- **Web Engine**: PyQtWebEngine 5.15.6+
- **Download Tool**: yt-dlp 2024.4.9+
- **Architecture**: Multi-threaded with QThread for downloads

## [0.1.0] - 2024-12-18

### Added
- Versión inicial del proyecto
- Estructura básica del código
- Dependencias iniciales
- Scripts de instalación básicos

---

## Notas de versión

### Versionado
- **MAJOR**: Cambios incompatibles en la API
- **MINOR**: Nuevas funcionalidades compatibles hacia atrás
- **PATCH**: Correcciones de bugs compatibles hacia atrás

### Dependencias
- Las versiones mínimas están especificadas en `lib/requirements.txt`
- Se recomienda usar las versiones más recientes para mejor compatibilidad

### Compatibilidad
- **Sistemas operativos**: Windows 10+, macOS 10.14+, Linux (Ubuntu 18.04+)
- **Python**: 3.7, 3.8, 3.9, 3.10, 3.11, 3.12
- **Arquitecturas**: x86_64, ARM64 (macOS)

---

## Contribuciones

Para contribuir al changelog:
1. Agrega tus cambios en la sección `[Unreleased]`
2. Usa el formato estándar de este changelog
3. Incluye enlaces a issues o pull requests cuando sea relevante
4. Mantén un tono profesional y descriptivo

## Enlaces

- [README.md](README.md) - Documentación principal del proyecto
- [LICENSE](LICENSE) - Licencia del proyecto
- [Issues](../../issues) - Reportar problemas o solicitar features
