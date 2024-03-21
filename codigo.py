
#que pedir en la terminal: python codigo.py C:/Users/aslia/OneDrive/Documents/8 SEMESTRE/Fundamentos MatematicosComputacion/FundamentosMatematicosDeLaComputacion/Variables.txt
#tienes que tener cuidado que el archivo no tenga espacios al final

import sys
import tkinter as tk
from tkinter import filedialog

def leer_archivo_en_lista(ruta):
    with open(ruta, 'r') as archivo:
        # Leer todas las líneas del archivo y almacenarlas en una lista
        lineas = archivo.readlines()
        # Limpiar las líneas para eliminar los saltos de línea al final
        lineas = [linea.strip() for linea in lineas]
    return lineas

def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()  # No queremos una ventana de Tk completa, solo la de diálogo
    ruta_archivo = filedialog.askopenfilename()  # Mostrar la ventana de diálogo de abrir archivo
    root.destroy()  # Cerrar la ventana de Tk después de abrir el archivo
    return ruta_archivo

# Lista que contendrá las variables del archivo
variables = []

if len(sys.argv) > 1:
    # Si se proporciona la ruta del archivo a través de la línea de comandos.
    ruta_archivo = sys.argv[1]
    variables = leer_archivo_en_lista(ruta_archivo)
else:
    # Si no hay argumentos en la línea de comandos, usar la ventana de diálogo.
    ruta_archivo = seleccionar_archivo()
    if ruta_archivo:  # Si se selecciona un archivo, leer su contenido.
        variables = leer_archivo_en_lista(ruta_archivo)
    else:
        print("No se seleccionó ningún archivo.")


print(variables)
#hasta aqui se hace la lectura del archivo, lo hace por medio de una ventana de dialogo de abrir archivo