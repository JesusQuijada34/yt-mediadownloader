@echo off
chcp 65001 >nul
echo 🎬 YouTube Media Downloader - Instalador Automático
echo ==================================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python no está instalado. Por favor, instala Python 3.7+ primero.
    echo Descarga desde: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✅ Python detectado
echo.

REM Verificar si pip está instalado
pip --version >nul 2>&1
if errorlevel 1 (
    echo ❌ pip no está instalado. Por favor, instala pip primero.
    pause
    exit /b 1
)

echo ✅ pip detectado
echo.

REM Actualizar pip
echo 🔄 Actualizando pip...
pip install --upgrade pip

REM Instalar dependencias desde requirements.txt
echo 📥 Instalando dependencias desde requirements.txt...
if exist "lib\requirements.txt" (
    pip install -r lib\requirements.txt
) else (
    echo ⚠️ No se encontró requirements.txt, instalando dependencias básicas...
    pip install yt-dlp PyQt5 PyQtWebEngine
)

echo.
echo ✅ Instalación completada!
echo.
echo 🚀 Para ejecutar la aplicación:
echo    python yt-mediadownloader.py
echo.
echo 📖 Para más información, consulta README.md
echo.
echo 🎬 ¡Disfruta descargando contenido de YouTube!
echo.
echo 💡 Consejo: Si encuentras problemas, ejecuta:
echo    pip install --upgrade yt-dlp
pause
