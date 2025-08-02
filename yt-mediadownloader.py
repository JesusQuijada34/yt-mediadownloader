import os
import sys
import subprocess
import platform
import argparse
from pathlib import Path
import questionary
from rich.console import Console
from rich.progress import Progress, BarColumn, DownloadColumn, TransferSpeedColumn, TimeRemainingColumn

console = Console()

def obtener_ruta_destino(audio=False):
    sistema = platform.system()
    if sistema == "Windows":
        carpeta = "My Music" if audio else "Videos"
        return Path(os.environ["USERPROFILE"]) / carpeta
    else:
        carpeta = "Música" if audio else "Vídeos"
        return Path.home() / carpeta

def verificar_yt_dlp():
    from shutil import which
    if which("yt-dlp") is None:
        console.print("[bold red]❌ yt-dlp no está instalado o no está en el PATH.[/]")
        sys.exit(1)

def descargar_video(url, solo_audio=False):
    destino = obtener_ruta_destino(audio=solo_audio)
    destino.mkdir(parents=True, exist_ok=True)

    comando = [
        "yt-dlp",
        url,
        "-o", str(destino / "%(title)s.%(ext)s")
    ]

    if solo_audio:
        comando += ["-x", "--audio-format", "mp3"]

    with Progress(
        "[progress.description]{task.description}",
        BarColumn(),
        DownloadColumn(),
        TransferSpeedColumn(),
        TimeRemainingColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("📥 Descargando...", start=False)
        proceso = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        for linea in proceso.stdout:
            if "[download]" in linea and "%" in linea:
                progress.start_task(task)
                try:
                    porcentaje = float(linea.split()[1].replace("%", ""))
                    progress.update(task, completed=porcentaje)
                except:
                    pass
            console.print(linea.strip())

        proceso.wait()
        if proceso.returncode == 0:
            console.print(f"[bold green]✅ Descarga completada en:[/] [cyan]{destino}[/]")
        else:
            console.print("[bold red]❌ Error durante la descarga.[/]")

def descargar_lista(path_txt, solo_audio=False):
    if not Path(path_txt).exists():
        console.print(f"[bold red]❌ Archivo no encontrado:[/] {path_txt}")
        return

    with open(path_txt, "r") as archivo:
        urls = [line.strip() for line in archivo if line.strip()]

    for url in urls:
        console.rule(f"[bold blue]Descargando: {url}")
        descargar_video(url, solo_audio=solo_audio)

def modo_interactivo():
    console.print(f"""[cyan]════════════════════════════════════════════════════════════
🎧 Youtube Media Downloader
════════════════════════════════════════════════════════════
""")
    url = questionary.text("🔗 Youtube Link URL:").ask()

    opcion = questionary.select(
        "¿Qué deseas descargar?",
        choices=["🎵 AUDIO (MP3)", "🎥 VIDEO (MP4/WEBM)", "❌ Cancelar"]
    ).ask()

    if opcion == "🎵 AUDIO (MP3)":
        descargar_video(url, solo_audio=True)
    elif opcion == "🎥 VIDEO (MP4/WEBM)":
        descargar_video(url, solo_audio=False)
    else:
        console.print(f"""[blue]═══ INFO ═══════════════════════════════════════════════════
[bold]Operación cancelada.[/][blue]
════════════════════════════════════════════════════════════""")

def main():
    verificar_yt_dlp()

    parser = argparse.ArgumentParser(description="Descargador de video/música de Influent")
    parser.add_argument("--durl", help="Descargar un solo enlace")
    parser.add_argument("--plist", help="Ruta a archivo .txt con enlaces")
    parser.add_argument("--mp3", action="store_true", help="Descargar solo audio en MP3")
    parser.add_argument("--mp4", action="store_true", help="Descargar video completo (por defecto)")

    args = parser.parse_args()

    # Prioridad: si se especifica --mp3, se fuerza solo_audio=True
    solo_audio = args.mp3

    if args.durl:
        descargar_video(args.durl, solo_audio=solo_audio)
    elif args.plist:
        descargar_lista(args.plist, solo_audio=solo_audio)
    else:
        modo_interactivo()

if __name__ == "__main__":
    main()

