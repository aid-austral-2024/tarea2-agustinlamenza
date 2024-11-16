# Análisis de Datos de Soda Stereo y Análisis Textual de sus Letras

Este proyecto se enfoca en el análisis de datos relacionados con la banda **Soda Stereo**, incluyendo el análisis de sus canciones y un estudio textual de sus letras. Los datos se procesan y visualizan utilizando **Quarto** para generar gráficos e informes, mientras que el análisis textual examina las letras de sus canciones.

## Enunciado

Puedes encontrar el enunciado del proyecto en el archivo [enunciado.md](./enunciado.md).

## Descripción

Este trabajo se basa en dos componentes principales:

1. **Análisis de Datos de Soda Stereo**: Procesamos los datos de la banda, incluyendo sus álbumes, canciones y características acústicas.
2. **Análisis Textual de las Letras**: Analizamos las letras de las canciones utilizando técnicas de procesamiento de texto para extraer patrones, frecuencias de palabras, y más.

## Requisitos

Este proyecto utiliza Poetry para la gestión de dependencias y entornos virtuales. Para instalar Poetry, por favor consulta la [documentación oficial de Poetry](https://python-poetry.org/docs/#installation).

## Ejecutar el Proyecto
1. **Instalar dependencias:**
Ejecuta el siguiente comando para instalar todas las dependencias del proyecto:
    ```bash
    poetry install
    ```
2. **Activar el entorno virtual:**
    ```bash
    poetry shell
    ```
3. **Renderizar quarto:**
    ```bash
    quarto render code/analysis.qmd
    ```
4. **Mover el archivo HTML generado al root:**
Para visualizar el resultado en github pages
    ```bash
    mv code/index.html ./index.html
    ```
