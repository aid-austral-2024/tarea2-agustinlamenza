# Makefile para reproducir el proyecto
# Este archivo está diseñado para sistemas Unix-like (Linux, macOS). 
# En Windows, se recomienda usar WSL o un entorno similar.

# Variables
ENV_FILE = .env
VENV_NAME = .venv

# Instalar dependencias
install:
	poetry install --no-root

# Activar entorno virtual
shell:
	poetry shell

# Ejecutar el script de scraping
scrape:
	poetry run python code/01_scraping.py

# Renderizar el análisis y mover el resultado
render:
	quarto render code/02_analysis.qmd && mv code/index.html ./index.html

# Comando principal para reproducir todo
reproducir: install shell scrape render
