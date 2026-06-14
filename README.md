# AI Test Dashboard

## 📌 Overview
This project integrates **Robot Framework + Selenium** with **Python + Flask** to build an AI‑driven test automation toolkit.  
It automates requirement analysis, test plan creation, script execution, and log/report visualization.

## 🚀 Features
- Robot Framework test cases (`tests/`)
- Page Object model (`page_objects/`)
- Python scripts for requirement analysis & log parsing (`scripts/`)
- Flask dashboard for visualization (`dashboards/`)
- AI/NLP integration for requirement → test case automation

## 🛠️ Setup
```bash
git clone https://github.com/sampathkmurthy/ai-test-dashboard.git
cd ai-test-dashboard
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt

## SPI Simulation Server

Run the SPI simulation server (from project root):

Using the module entrypoint (recommended):
```powershell
venv\Scripts\python.exe -m utils.spi_server
```

Or use the launcher script:
```powershell
venv\Scripts\python.exe scripts\run_spi_server.py
```

Quick client test (Python):
```python
import socket
with socket.create_connection(('127.0.0.1', 65432), timeout=2) as s:
	s.sendall(b'READ_TEMP')
	print(s.recv(1024).decode())
```

Notes:
- `utils.spi_server` uses package-relative imports; run it as a module or via the launcher so `utils` is resolved correctly.
- The server listens on `127.0.0.1:65432` by default.

