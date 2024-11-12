# Análisis de Discografía y Letras de Canciones
Este proyecto tiene como objetivo realizar un análisis de la discografía de un artista y de las letras de sus canciones. Los datos se obtienen mediante la API de Spotify para la discografía y web scraping de las letras usando la página Genius. El análisis incluye estadísticas descriptivas, visualización de datos y análisis textual de las letras.

Estructura del Proyecto
El proyecto está organizado en varias carpetas y archivos, cada uno con una función específica:

```bash
./
│
├── data/
│   ├── raw/                  # Datos crudos obtenidos de APIs (Spotify y Genius)
│   ├── processed/            # Datos procesados listos para el análisis
│   └── figures/              # Imágenes generadas por el análisis
│
├── scripts/                  # Código fuente en Python
│   ├── get_data.py           # Obtiene los datos de Spotify y Genius
│   ├── text_analysis.py      # Realiza el análisis textual de las letras
│   ├── descriptive_analysis.py # Análisis descriptivo de las canciones
│   └── save_data.py          # Guarda los datos procesados en CSV
│
├── notebooks/                # Reportes en Quarto o Jupyter
│   └── analysis.qmd          # Reporte generado con Quarto
│
├── requirements.txt          # Dependencias necesarias para el proyecto
├── poetry.lock               # Archivo de bloqueo de dependencias (si usas Poetry)
└── README.md                 # Este archivo
````

## Requisitos
Python 3.8 o superior
Poetry para gestionar las dependencias
Cuenta en Spotify (para obtener acceso a la API de Spotify)
Cuenta en Genius (para obtener las letras de las canciones)
Instalación
Sigue los siguientes pasos para configurar el proyecto y sus dependencias en tu entorno local.

## 1. Clonar el repositorio
Primero, clona este repositorio en tu máquina:

```bash
git clone https://github.com/usuario/tarea2.git
cd tarea2
```

## 2. Instalar dependencias
Este proyecto utiliza Poetry para la gestión de dependencias. Si no tienes Poetry instalado, sigue las instrucciones de instalación desde su sitio web oficial.

Una vez tengas Poetry instalado, instala las dependencias del proyecto:

```bash
poetry install
````

Poetry creará un entorno virtual y descargará todas las librerías necesarias, incluyendo:

- `spotipy` (para interactuar con la API de Spotify)
- `requests` (para hacer scraping de Genius)
- `beautifulsoup4` (para analizar HTML)
- `pandas` (para la manipulación de datos)
- `matplotlib`, seaborn (para visualización de datos)
- `nltk` (para procesamiento de texto)

## 3. Configurar las claves de las APIs

Para acceder a los datos de Spotify y Genius, necesitas configurar las credenciales de las APIs.

Spotify
Crea una aplicación en el Spotify Developer Dashboard y obtén tu Client ID y Client Secret.
Añade las credenciales en el archivo scripts/get_data.py donde se realiza la autenticación:
python
Copy code
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="your_client_id", client_secret="your_client_secret"))
Genius
Regístrate en Genius API y obtén tu API Key.
Utiliza esta API Key para hacer solicitudes y obtener las letras de las canciones.

## 4. Ejecutar el código

Una vez configurado el entorno, puedes ejecutar los scripts para obtener los datos y realizar el análisis.

Paso 1: Obtener los datos
Ejecuta el siguiente script para obtener la discografía del artista y las letras de sus canciones:

bash
Copy code
poetry run python scripts/get_data.py
Este script interactúa con la API de Spotify para obtener la discografía del artista y usa scraping de Genius para obtener las letras de las canciones. Los datos se guardarán en la carpeta data/processed/ en formato CSV.

Paso 2: Realizar el análisis textual
Para analizar las letras de las canciones y generar estadísticas sobre las palabras, ejecuta el siguiente script:

```bash
poetry run python scripts/text_analysis.py
```
Este script realiza un análisis de las palabras más comunes en las letras y genera una visualización de las palabras más frecuentes.

Paso 3: Realizar el análisis descriptivo
Ejecuta este script para obtener estadísticas descriptivas sobre las canciones (como la longitud de las letras, la cantidad de palabras, etc.):

bash
Copy code
poetry run python scripts/descriptive_analysis.py
Este script genera visualizaciones sobre la distribución de la longitud de las letras de las canciones.

5. Guardar los resultados
Los resultados de los análisis se guardarán en los archivos CSV en la carpeta data/processed/. Las visualizaciones se guardarán en la carpeta data/figures/.

6. Generar el reporte con Quarto
Una vez que hayas ejecutado los análisis, puedes generar un reporte utilizando Quarto. Ejecuta el siguiente comando para renderizar el reporte en formato HTML:

bash
Copy code
quarto render notebooks/analysis.qmd
Este comando generará un archivo HTML con el análisis completo, incluyendo gráficos y explicaciones.

Descripción de los Archivos
scripts/get_data.py: Este script obtiene los datos de la API de Spotify y realiza scraping de las letras de las canciones desde Genius. Los resultados se guardan en archivos CSV en la carpeta data/processed/.

scripts/text_analysis.py: Este script analiza las letras de las canciones (frecuencia de palabras, tokenización, etc.) y genera visualizaciones sobre las palabras más comunes.

scripts/descriptive_analysis.py: Realiza un análisis descriptivo de las canciones, como la longitud de las letras y otras métricas relacionadas.

scripts/save_data.py: Guarda los datos procesados (discografía, letras) en archivos CSV.

notebooks/analysis.qmd: Documento Quarto donde se presenta todo el análisis, incluyendo visualizaciones y conclusiones.

data/processed/: Contiene los archivos CSV con los datos procesados de las canciones y letras.

data/figures/: Contiene las imágenes generadas durante el análisis.

Contribuciones
Si deseas contribuir a este proyecto, por favor crea un "pull request" con tus cambios. Asegúrate de que tu código esté bien documentado y siga las convenciones de estilo de Python.

Licencia
Este proyecto está bajo la licencia MIT. Ver el archivo LICENSE para más detalles.

Notas adicionales
Si prefieres trabajar en un entorno de desarrollo diferente, puedes exportar las dependencias a un archivo requirements.txt y luego instalarlas utilizando pip.
bash
Copy code
poetry export -f requirements.txt > requirements.txt
pip install -r requirements.txt
