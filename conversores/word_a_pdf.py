# Conversor de Word a PDF utilizando la biblioteca python-docx y reportlab

import os
from docx2pdf import convert


def procesar_word(ruta_entrada):
    """
    Toma la ruta de un archivo Word y lo convierte a PDF en la misma carpeta.
    """

    # Verificar que el archivo existe
    if not os.path.isfile(ruta_entrada):
        print(f"El archivo {ruta_entrada} no existe.")
        return
    
    # Convertir el archivo Word a PDF
    try:
        print("⏳ Abriendo Microsoft Word en segundo plano... (esto puede tardar unos segundos)")

        # Utilizar docx2pdf para convertir el archivo Word a PDF
        convert(ruta_entrada)

        print(f"Archivo convertido exitosamente: {ruta_entrada.replace('.docx', '.pdf')}")
        return True

    except Exception as e:
        print(f"Error al convertir el archivo: {e}")
        return False