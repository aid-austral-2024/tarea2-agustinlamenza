# Análisis de datos de Soda Stereo y análisis textual de sus Letras

## Descripción general

Este proyecto tiene como objetivo realizar un análisis de datos de la banda **Soda Stereo**, incluyendo el estudio de sus canciones y un análisis textual de sus letras. Los datos se obtienen de [Spotify](https://developer.spotify.com/) y [lyricsondemand](https://lyricsondemand.com/).

**[Enlace al sitio web del proyecto](https://aid-austral-2024.github.io/tarea2-agustinlamenza/)**

## Estructura del proyecto

Este trabajo se basa en dos componentes principales:

1. **Análisis de Datos de Soda Stereo**: Incluye el procesamiento de datos relacionados con los álbumes, canciones y características acústicas de la banda.
2. **Análisis Textual de las Letras**: Utiliza técnicas de procesamiento de texto para analizar las letras de las canciones, extrayendo patrones y frecuencias de palabras.

## Ejecutar el proyecto

Este proyecto utiliza Poetry para la gestión de dependencias y entornos virtuales. Para instalar Poetry, por favor consulta la [documentación oficial de Poetry](https://python-poetry.org/docs/#installation).

### Archivo .env con Variables de Entorno
Para que el proyecto funcione correctamente, necesitarás configurar algunas variables de entorno, como tu client_id y client_secret de Spotify. Esto se hace creando un archivo .env en el directorio raíz del proyecto.

El archivo .env debe tener el siguiente formato:
```
SPOTIFY_CLIENT_ID=""
SPOTIFY_CLIENT_SECRET=""
```

### Pasos para reproducir resultados (Linux, macOS)
1. **Instalar dependencias:** Para instalar todas las dependencias necesarias, ejecuta:
    ```bash
    make install
    ```
    
2. **Scraping de datos:** Para obtener los datos desde las fuentes externas (Spotify y Lyricsondemand), ejecuta el script de scraping:
    ```bash
    make scrape
    ```

3. **Renderizar analisis y mover resultado al root:** Finalmente, para renderizar el análisis y mover el archivo resultante al directorio raíz del proyecto, ejecuta:
    ```bash
    make render
    ```
4. **Reproducir todo el proceso** (instalar, activar entorno, scraping y análisis):
    ```bash
    make reproducir
    ```