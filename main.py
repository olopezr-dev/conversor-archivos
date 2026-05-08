# Archivo main del programa. Aquí se importan los módulos de conversión y se maneja la lógica principal del programa.

from conversores.word_a_pdf import procesar_word


def iniciar_consola():
    """
    Función principal que inicia la consola y maneja la interacción con el usuario.
    """

    print("\n--- 📄 Conversor de Archivos Universal 📄 ---")
    
    ruta_archivo = input("Arrastra aquí tu archivo de Word (.docx) y pulsa Enter: ")

    # Limpiamos la ruta por si Windows añade comillas invisibles o espacios extra
    ruta_archivo = ruta_archivo.replace('"', '').replace("'", "").strip()

    print(f"\nProcesando: {ruta_archivo}")


    if ruta_archivo.lower().endswith('.docx'):
        procesar_word(ruta_archivo)
    else:
        print("Formato no soportado. Por favor, ingresa un archivo .docx")
    

    # Función main que inicia la consola
    if __name__ == "__main__":
        iniciar_consola()