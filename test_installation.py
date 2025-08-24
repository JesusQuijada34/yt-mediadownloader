#!/usr/bin/env python3
"""
Script de prueba para verificar la instalación de YouTube Media Downloader
"""

import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Verifica la versión de Python"""
    print("🐍 Verificando versión de Python...")
    version = sys.version_info
    print(f"   Versión actual: {version.major}.{version.minor}.{version.micro}")
    
    if version.major == 3 and version.minor >= 7:
        print("   ✅ Versión de Python compatible")
        return True
    else:
        print("   ❌ Se requiere Python 3.7 o superior")
        return False

def check_dependencies():
    """Verifica que las dependencias estén instaladas"""
    print("\n📦 Verificando dependencias...")
    
    dependencies = [
        ("PyQt5", "PyQt5"),
        ("PyQtWebEngine", "PyQtWebEngine"),
        ("yt-dlp", "yt-dlp")
    ]
    
    all_ok = True
    
    for dep_name, import_name in dependencies:
        try:
            __import__(import_name)
            print(f"   ✅ {dep_name} instalado")
        except ImportError:
            print(f"   ❌ {dep_name} NO instalado")
            all_ok = False
    
    return all_ok

def check_yt_dlp_command():
    """Verifica que yt-dlp esté disponible como comando"""
    print("\n🔧 Verificando comando yt-dlp...")
    
    try:
        result = subprocess.run(["yt-dlp", "--version"], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            version = result.stdout.strip()
            print(f"   ✅ yt-dlp disponible (versión: {version})")
            return True
        else:
            print("   ❌ yt-dlp no responde correctamente")
            return False
    except (subprocess.TimeoutExpired, FileNotFoundError):
        print("   ❌ yt-dlp no encontrado en PATH")
        return False

def check_main_script():
    """Verifica que el script principal exista"""
    print("\n📁 Verificando archivos del proyecto...")
    
    main_script = Path("yt-mediadownloader.py")
    requirements = Path("lib/requirements.txt")
    readme = Path("README.md")
    
    files_ok = True
    
    if main_script.exists():
        print("   ✅ yt-mediadownloader.py encontrado")
    else:
        print("   ❌ yt-mediadownloader.py NO encontrado")
        files_ok = False
    
    if requirements.exists():
        print("   ✅ requirements.txt encontrado")
    else:
        print("   ❌ requirements.txt NO encontrado")
        files_ok = False
    
    if readme.exists():
        print("   ✅ README.md encontrado")
    else:
        print("   ❌ README.md NO encontrado")
        files_ok = False
    
    return files_ok

def main():
    """Función principal de verificación"""
    print("🎬 YouTube Media Downloader - Verificación de Instalación")
    print("=" * 60)
    
    checks = [
        check_python_version(),
        check_dependencies(),
        check_yt_dlp_command(),
        check_main_script()
    ]
    
    print("\n" + "=" * 60)
    
    if all(checks):
        print("🎉 ¡Todas las verificaciones pasaron exitosamente!")
        print("\n🚀 Puedes ejecutar la aplicación con:")
        print("   python3 yt-mediadownloader.py")
        print("\n💡 O usar los scripts de instalación automática:")
        print("   Linux/macOS: ./autorun")
        print("   Windows: autorun.bat")
    else:
        print("❌ Algunas verificaciones fallaron.")
        print("\n🔧 Para resolver los problemas:")
        print("   1. Ejecuta: pip3 install -r lib/requirements.txt")
        print("   2. O ejecuta: ./autorun (Linux/macOS) o autorun.bat (Windows)")
        print("   3. Verifica que tienes Python 3.7+ instalado")
    
    print("\n📖 Para más información, consulta README.md")

if __name__ == "__main__":
    main()
