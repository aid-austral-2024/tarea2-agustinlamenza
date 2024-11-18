# Análisis de datos de Soda Stereo y análisis textual de sus Letras

## Descripción general

Este proyecto se enfoca en el análisis de datos relacionados con la banda **Soda Stereo**, incluyendo el análisis de sus canciones y un estudio textual de sus letras. Los datos se obtienen de [Spotify](https://developer.spotify.com/) y [lyricsondemand](https://lyricsondemand.com/).

**[Link a web site](https://aid-austral-2024.github.io/tarea2-agustinlamenza/)**

## Estructura del proyecto

Este trabajo se basa en dos componentes principales:

1. **Análisis de Datos de Soda Stereo**: Procesamos los datos de la banda, incluyendo sus álbumes, canciones y características acústicas.
2. **Análisis Textual de las Letras**: Analizamos las letras de las canciones utilizando técnicas de procesamiento de texto para extraer patrones, frecuencias de palabras.

## Ejecutar el proyecto

Este proyecto utiliza Poetry para la gestión de dependencias y entornos virtuales. Para instalar Poetry, por favor consulta la [documentación oficial de Poetry](https://python-poetry.org/docs/#installation).

### Archivo .env con Variables de Entorno
Para ejecutar el proyecto correctamente, necesitarás configurar algunas variables de entorno, como tu client_id y client_secret de Spotify. Esto se hace creando un archivo .env en el root del proyecto.

El archivo .env debe tener el siguiente formato:
```
SPOTIFY_CLIENT_ID=""
SPOTIFY_CLIENT_SECRET=""
```

### Pasos para reproducir resultados
1. **Instalar dependencias:**
Ejecuta el siguiente comando para instalar todas las dependencias del proyecto:

    ```bash
    poetry install
    ```

2. **Activar el entorno virtual:**

    ```bash
    poetry shell
    ```

3. **Scraping de datos:**

    ```bash
    poetry run python code/01_scraping.py
    ```

4. **Renderizar analisis y mover resultado al root:**

    ```bash
    quarto render code/02_analysis.qmd &&  mv code/index.html ./index.html
    ```