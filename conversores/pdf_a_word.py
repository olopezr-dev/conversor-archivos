# Conversor de PDF a Word utilizando la biblioteca pdf2docx.

import os
from pdf2docx import Converter


def procesar_pdf(ruta_entrada):
    """
    Toma la ruta de un archivo PDF y lo convierte a Word (.docx) en la misma carpeta.
    """

    # Verificar que el archivo existe
    if not os.path.isfile(ruta_entrada):
        print(f"El archivo {ruta_entrada} no existe.")
        return
    
    # Convertir el archivo PDF a Word
    try:
        print("⏳ Abriendo el PDF en segundo plano... (esto puede tardar unos segundos)")

        # A diferencia de docx2pdf, esta librería nos pide que le digamos 
        # exactamente cómo se va a llamar el archivo de salida.
        # Así que cogemos la ruta original y cambiamos la extensión:
        ruta_salida = ruta_entrada.replace('.pdf', '.docx')

       # Iniciamos el conversor
        cv = Converter(ruta_entrada)
        # Hacemos la conversión
        cv.convert(ruta_salida)
        # Cerramos el archivo para liberar memoria
        cv.close()

        print(f"Archivo convertido exitosamente: {ruta_salida}")
        return True

    except Exception as e:
        print(f"Error al convertir el archivo: {e}")
        return False