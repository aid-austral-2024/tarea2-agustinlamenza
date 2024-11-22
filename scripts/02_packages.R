# Lista de paquetes a instalar
packages <- c(
  "tidyverse", "ggplot2", "wordcloud", "tidytext", "textdata",
  "stopwords", "here", "pastecs", "psych"
)

# Instalar los paquetes que no estén ya instalados
install_missing_packages <- packages[!(packages %in% installed.packages()[, "Package"])]
if (length(install_missing_packages)) {
  install.packages(install_missing_packages)
}
