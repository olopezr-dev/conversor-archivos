# Programa encargado de reconocer el formato del archivo y llamar al módulo de conversión correspondiente.

import os
# Importamos nuestros "plugins" de conversión
from conversores.word_a_pdf import procesar_word
from conversores.pdf_a_word import procesar_pdf


def enrutar_archivo(ruta_archivo):
    """
    Analiza la extensión del archivo y lo envía al conversor adecuado.
    """
    # Verificamos que la ruta no esté vacía
    if not ruta_archivo:
        print("❌ No has introducido ninguna ruta.")
        return False
    
    # os.path.splitext divide la ruta en dos: el nombre y la extensión
    # Ejemplo: "documento.docx" -> nombre="documento", extension=".docx"
    nombre, extension = os.path.splitext(ruta_archivo)

    # Pasamos a minúsculas por si el archivo es ".DOCX" en mayúsculas
    extension = extension.lower()


    # --- EL RUTEADOR ---

    # Comprobamos la extensión y llamamos al conversor correspondiente
    
    # Word a PDF
    if extension == ".docx":
        return procesar_word(ruta_archivo)
    
    # PDF a Word
    elif extension == ".pdf":
        return procesar_pdf(ruta_archivo)


    else:
        print(f"⚠️ Manager: El formato '{extension}' todavía no está soportado en esta versión.")
        return False