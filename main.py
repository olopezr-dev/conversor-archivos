# Archivo main del programa. Aquí se importa el módulo de gestión y se inicia la consola para que el usuario interactúe.

from core.manager import enrutar_archivo


def iniciar_consola():
    """
    Función principal que inicia la consola y maneja la interacción con el usuario.
    """

    print("\n--- 📄 Conversor de Archivos Universal 📄 ---")
    
    ruta_archivo = input("Escribe la dirección o arrastra aquí tu archivo de Word (.docx) y pulsa Enter: ")

    # Limpiamos la ruta por si Windows añade comillas invisibles o espacios extra
    ruta_archivo = ruta_archivo.replace('"', '').replace("'", "").strip()

    print(f"\nProcesando: {ruta_archivo}")
    
    # Le pasamos el archivo al manager y que él decida qué hacer
    resultado = enrutar_archivo(ruta_archivo)



# Función main que inicia la consola
if __name__ == "__main__":
    iniciar_consola()