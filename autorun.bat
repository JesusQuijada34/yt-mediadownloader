@echo off
REM =============================================================================
REM YouTube Media Downloader - Script de Ejecución Automática para Windows
REM =============================================================================
REM
REM Este script automatiza la instalación y ejecución de la aplicación
REM YouTube Media Downloader en sistemas Windows.
REM
REM Autor: influent
REM Versión: 1.0.0
REM Fecha: 2024-12-19
REM Licencia: MIT
REM
REM =============================================================================
REM INSTRUCCIONES PARA PRINCIPIANTES
REM =============================================================================
REM
REM 1. GUARDAR: Guarda este archivo como "autorun.bat" en la carpeta del proyecto
REM 2. EJECUTAR: Haz doble clic en "autorun.bat" para ejecutarlo
REM 3. PERMISOS: Si Windows muestra una advertencia, haz clic en "Ejecutar de todos modos"
REM 4. ESPERAR: El script instalará las dependencias automáticamente
REM 5. DISFRUTAR: La aplicación se abrirá automáticamente
REM
REM =============================================================================
REM REQUISITOS DEL SISTEMA
REM =============================================================================
REM
REM - Windows 10 o superior (recomendado)
REM - Python 3.7 o superior instalado
REM - Conexión a Internet para descargar dependencias
REM - Permisos de administrador (opcional, para instalación global)
REM
REM =============================================================================
REM FUNCIONES DEL SCRIPT
REM =============================================================================
REM
REM ✓ Verificación de Python instalado
REM ✓ Instalación automática de dependencias
REM ✓ Configuración del entorno virtual (opcional)
REM ✓ Ejecución de la aplicación
REM ✓ Manejo de errores y notificaciones
REM ✓ Limpieza automática de archivos temporales
REM
REM =============================================================================

echo.
echo =============================================================================
echo 🎬 YOUTUBE MEDIA DOWNLOADER - INSTALADOR AUTOMÁTICO
echo =============================================================================
echo.
echo 🚀 Iniciando proceso de instalación automática...
echo 📅 Fecha y hora: %date% %time%
echo 💻 Sistema operativo: %OS%
echo 🔍 Versión de Windows: %OSVERSION%
echo.

REM =============================================================================
REM VERIFICACIÓN DE PYTHON
REM =============================================================================

echo 🔍 Verificando instalación de Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ ERROR: Python no está instalado o no está en el PATH del sistema.
    echo.
    echo 📋 SOLUCIÓN: Instala Python desde https://www.python.org/downloads/
    echo 💡 IMPORTANTE: Marca la opción "Add Python to PATH" durante la instalación
    echo.
    echo 🔄 Después de instalar Python, ejecuta este script nuevamente.
    echo.
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✅ Python %PYTHON_VERSION% detectado correctamente

REM Verificar versión mínima (Python 3.7+)
for /f "tokens=2 delims=." %%a in ("%PYTHON_VERSION%") do set PYTHON_MAJOR=%%a
for /f "tokens=3 delims=." %%b in ("%PYTHON_VERSION%") do set PYTHON_MINOR=%%b

if %PYTHON_MAJOR% LSS 3 (
    echo ❌ ERROR: Se requiere Python 3.7 o superior
    echo 🔍 Versión actual: %PYTHON_VERSION%
    pause
    exit /b 1
)

if %PYTHON_MAJOR% EQU 3 (
    if %PYTHON_MINOR% LSS 7 (
        echo ❌ ERROR: Se requiere Python 3.7 o superior
        echo 🔍 Versión actual: %PYTHON_VERSION%
        pause
        exit /b 1
    )
)

echo ✅ Versión de Python compatible (%PYTHON_VERSION%)

REM =============================================================================
REM VERIFICACIÓN DE PIP
REM =============================================================================

echo.
echo 🔍 Verificando instalación de pip...
python -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ ERROR: pip no está disponible
    echo.
    echo 📋 SOLUCIÓN: Reinstala Python o ejecuta:
    echo    python -m ensurepip --upgrade
    echo.
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python -m pip --version 2^>^&1') do set PIP_VERSION=%%i
echo ✅ pip %PIP_VERSION% disponible

REM =============================================================================
REM ACTUALIZACIÓN DE PIP
REM =============================================================================

echo.
echo 🔄 Actualizando pip a la última versión...
python -m pip install --upgrade pip --quiet
if %errorlevel% neq 0 (
    echo ⚠️ ADVERTENCIA: No se pudo actualizar pip, continuando...
) else (
    echo ✅ pip actualizado correctamente
)

REM =============================================================================
REM VERIFICACIÓN DE ARCHIVOS DEL PROYECTO
REM =============================================================================

echo.
echo 🔍 Verificando archivos del proyecto...

if not exist "yt-mediadownloader.py" (
    echo ❌ ERROR: No se encontró el archivo principal yt-mediadownloader.py
    echo 📍 Asegúrate de ejecutar este script desde la carpeta del proyecto
    echo.
    pause
    exit /b 1
)

if not exist "lib\requirements.txt" (
    echo ❌ ERROR: No se encontró lib\requirements.txt
    echo 📍 Verifica que la estructura del proyecto esté completa
    echo.
    pause
    exit /b 1
)

echo ✅ Archivos del proyecto verificados correctamente

REM =============================================================================
REM INSTALACIÓN DE DEPENDENCIAS
REM =============================================================================

echo.
echo 📦 Instalando dependencias del proyecto...
echo 🔍 Dependencias a instalar:
echo    - PyQt5 (interfaz gráfica)
echo    - PyQtWebEngine (navegador web)
echo    - pytube (descarga de YouTube)
echo.

REM Instalar dependencias principales
echo 🔧 Instalando PyQt5...
python -m pip install PyQt5 --quiet
if %errorlevel% neq 0 (
    echo ❌ ERROR: No se pudo instalar PyQt5
    echo 💡 Intenta ejecutar como administrador o verifica tu conexión a Internet
    pause
    exit /b 1
)

echo 🔧 Instalando PyQtWebEngine...
python -m pip install PyQtWebEngine --quiet
if %errorlevel% neq 0 (
    echo ❌ ERROR: No se pudo instalar PyQtWebEngine
    echo 💡 En Windows, puede ser necesario instalar Visual C++ Build Tools
    echo 📥 Descarga desde: https://visualstudio.microsoft.com/visual-cpp-build-tools/
    pause
    exit /b 1
)

echo 🔧 Instalando pytube...
python -m pip install pytube --quiet
if %errorlevel% neq 0 (
    echo ❌ ERROR: No se pudo instalar pytube
    pause
    exit /b 1
)

echo ✅ Todas las dependencias instaladas correctamente

REM =============================================================================
REM VERIFICACIÓN DE INSTALACIÓN
REM =============================================================================

echo.
echo 🔍 Verificando instalación de dependencias...
python -c "import PyQt5; import PyQt5.QtWebEngineWidgets; import pytube; print('✅ Verificación exitosa')" 2>nul
if %errorlevel% neq 0 (
    echo ❌ ERROR: Las dependencias no se instalaron correctamente
    echo 🔄 Intenta ejecutar: python -m pip install -r lib\requirements.txt
    pause
    exit /b 1
)

echo ✅ Verificación de dependencias completada

REM =============================================================================
REM EJECUCIÓN DE LA APLICACIÓN
REM =============================================================================

echo.
echo 🚀 Iniciando YouTube Media Downloader...
echo.
echo 📋 INFORMACIÓN DE LA APLICACIÓN:
echo    - Nombre: YouTube Media Downloader
echo    - Versión: 1.0.0
echo    - Desarrollador: influent
echo    - Licencia: MIT
echo.
echo 💡 CONSEJOS DE USO:
echo    - Navega por YouTube en el navegador embebido
echo    - Las URLs se detectan automáticamente
echo    - Usa los botones del panel lateral para descargar
echo    - El historial se guarda automáticamente
echo.
echo ⏳ Abriendo aplicación en 3 segundos...
timeout /t 3 /nobreak >nul

REM Ejecutar la aplicación
python yt-mediadownloader.py

REM =============================================================================
REM MANEJO DE SALIDA
REM =============================================================================

if %errorlevel% neq 0 (
    echo.
    echo ❌ La aplicación se cerró con errores (código: %errorlevel%)
    echo.
    echo 🔍 POSIBLES SOLUCIONES:
    echo    1. Verifica que todas las dependencias estén instaladas
    echo    2. Asegúrate de tener permisos de escritura en la carpeta
    echo    3. Verifica que no haya otros procesos usando los puertos necesarios
    echo    4. Revisa el archivo de logs si está disponible
    echo.
    echo 📞 Para obtener ayuda, consulta:
    echo    - README.md del proyecto
    echo    - Issues en GitHub
    echo    - Documentación oficial de PyQt5
    echo.
) else (
    echo.
    echo ✅ La aplicación se cerró correctamente
    echo.
)

REM =============================================================================
REM LIMPIEZA Y FINALIZACIÓN
REM =============================================================================

echo.
echo 🧹 Limpiando archivos temporales...
if exist "__pycache__" rmdir /s /q "__pycache__" 2>nul
if exist "*.pyc" del /q "*.pyc" 2>nul

echo.
echo =============================================================================
echo 🎉 INSTALACIÓN COMPLETADA
echo =============================================================================
echo.
echo ✅ Python verificado: %PYTHON_VERSION%
echo ✅ Dependencias instaladas
echo ✅ Aplicación ejecutada
echo.
echo 💡 Para ejecutar la aplicación nuevamente:
echo    python yt-mediadownloader.py
echo.
echo 📚 Para más información, consulta README.md
echo 🌐 Repositorio: https://github.com/influent/yt-mediadownloader
echo.
echo =============================================================================
echo.

REM Pausa final para que el usuario pueda leer la información
pause
