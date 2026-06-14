"""Launcher for the SPI simulation server.

Run from project root (preferred):
    venv\\Scripts\\python.exe scripts\\run_spi_server.py

This script uses package import semantics so `utils` package is resolved correctly.
"""
import sys
from pathlib import Path

# Ensure working directory is project root
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from utils.spi_server import start_spi_server

if __name__ == '__main__':
    start_spi_server()
