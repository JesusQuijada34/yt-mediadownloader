#!/usr/bin/env python3
"""
Setup script for YouTube Media Downloader
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("lib/requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="yt-mediadownloader",
    version="1.0.0",
    author="influent",
    description="Una aplicación de escritorio moderna para descargar contenido de YouTube",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/tu-usuario/yt-mediadownloader",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Multimedia :: Video",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "yt-mediadownloader=yt_mediadownloader:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.ico", "*.png"],
    },
    keywords="youtube, downloader, media, video, audio, gui, pyqt5",
    project_urls={
        "Bug Reports": "https://github.com/tu-usuario/yt-mediadownloader/issues",
        "Source": "https://github.com/tu-usuario/yt-mediadownloader",
        "Documentation": "https://github.com/tu-usuario/yt-mediadownloader#readme",
    },
)
