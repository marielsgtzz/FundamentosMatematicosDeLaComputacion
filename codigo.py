
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


#print(variables)
#hasta aqui se hace la lectura del archivo, lo hace por medio de una ventana de dialogo de abrir archivo. Queda en el arreglo variables
#esta se utiliza para expresiones regulares 
#proporciona operaciones de coincidencia de expresiones regulares
import re

# Definir las expresiones regulares para cada tipo
patterns = {
    'int': re.compile(r'\bint\s+\w+'),
    'double': re.compile(r'\bdouble\s+\w+'),
    'byte': re.compile(r'\bbyte\s+\w+'),
    'short': re.compile(r'\bshort\s+\w+'),
    'long': re.compile(r'\blong\s+\w+'),
    'float': re.compile(r'\bfloat\s+\w+'),
    'char': re.compile(r'\bchar\s+\w+'),
    'boolean': re.compile(r'\bboolean\s+\w+'),
    'int[]': re.compile(r'\bint\[\]\s+\w+'),
    'double[]': re.compile(r'\bdouble\[\]\s+\w+'),
    'byte[]': re.compile(r'\bbyte\[\]\s+\w+'),
    'short[]': re.compile(r'\bshort\[\]\s+\w+'),
    'long[]': re.compile(r'\blong\[\]\s+\w+'),
    'float[]': re.compile(r'\bfloat\[\]\s+\w+'),
    'char[]': re.compile(r'\bchar\[\]\s+\w+'),
    'boolean[]': re.compile(r'\bboolean\[\]\s+\w+')
}


def buscar_tipos(variables):
    resultados = {tipo: [] for tipo in patterns}

    for linea in variables:
        for tipo, pattern in patterns.items():
            if pattern.search(linea):
                resultados[tipo].append(linea)
    
    return resultados

# resultados es un diccionario con la clasificacion de las expresiones y las que estaban en el archivo
resultados = buscar_tipos(variables)

print(resultados)



#salidas
'''Numero total de variables declaradas.
Numero total de tipos utilizados en las declaraciones encontradas.
Numero total de variables declaradas de cada tipo.
Numero total de variables inicializadas.
Numero total de variables de tipo arreglo.
Número total de declaraciones constantes (es decir, el valor no se puede cambiar después de la inicialización).
Clasificación de todos los nombres de variables por tipo declarado.'''