# Makefile para reproducir el proyecto
# Este archivo está diseñado para sistemas Unix-like (Linux, macOS). 
# En Windows, se recomienda usar WSL o un entorno similar.

# Variables
ENV_FILE = .env
VENV_NAME = .venv

# Instalar dependencias
install:
	poetry install --no-root && Rscript scripts/02_packages.R

# Ejecutar el script de scraping
scrape:
	poetry run python scripts/01_scraping.py

# Renderizar el análisis y mover el resultado
render:
	quarto render reports/01_analysis.qmd && mv reports/index.html ./index.html

# Comando principal para reproducir todo
reproducir: install scrape render
