# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import filedialog
import re

def seleccionar_archivo():
    """
    Crea una ventana oculta de Tkinter para seleccionar un archivo y devuelve la ruta del archivo seleccionado.
    """
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de tkinter
    ruta_archivo = filedialog.askopenfilename()  # Muestra el diálogo para seleccionar archivo
    root.destroy()  # Cierra la ventana de tkinter
    return ruta_archivo

def leer_archivo_en_lista(ruta):
    """
    Lee el contenido de un archivo y lo devuelve como una cadena.
    Si ocurre un error durante la lectura, imprime el error y devuelve None.
    """
    try:
        with open(ruta, 'r') as archivo:
            content = archivo.read()
        return content
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

def tokenizar_contenido(content):
    """
    Tokeniza el contenido del archivo utilizando una expresión regular y devuelve una lista de tokens.
    """
    token_regex = re.compile(r"while|\(|\)|\{|\}|[a-z]|[0-9]|==|!=|<=|>=|<|>")
    tokens = token_regex.findall(content)
    return tokens

def validar_whiles(tokens):
    """
    Valida la estructura de los bloques 'while' en la lista de tokens.
    Cuenta y devuelve:
    - Si los bloques 'while' están correctamente balanceados
    - El número de variables distintas utilizadas
    - El número de operadores de comparación
    - El número de bloques 'while'
    """
    stack = []  # Pila para rastrear los bloques 'while' y corchetes
    i = 0
    variables_distinct = set()  # Conjunto para rastrear variables distintas
    operadores_comp = 0  # Contador de operadores de comparación
    whiles = 0  # Contador de bloques 'while'

    # Contar variables distintas y operadores de comparación en los tokens
    for token in tokens:
        if re.match(r"^[a-z]$", token):  # Si el token es una variable (una letra minúscula)
            variables_distinct.add(token)
        elif token in ("<", ">", "==", ">=", "<=", "!="):  # Si el token es un operador de comparación
            operadores_comp += 1

    # Validar la estructura de los bloques 'while'
    while i < len(tokens):
        token = tokens[i]

        if token == "while":
            stack.append(token)
            whiles += 1
        elif token == "{":
            stack.append(token)
        elif token == "}":
            if len(stack) > 1 and stack[-1] == "{" and stack[-2] == "while":
                stack.pop()  # Eliminar el corchete de apertura
                stack.pop()  # Eliminar el 'while' correspondiente
            else:
                return (False, 0, 0, 0)  # Estructura inválida
        elif token == "(":
            stack.append(token)
        elif token == ")":
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            else:
                return (False, 0, 0, 0)  # Estructura inválida
        else:
            # Validar la estructura del condicional del 'while'
            if not re.match(r"[a-z]|[0-9]|==|!=|<=|>=|<|>", token):
                return (False, 0, 0, 0)  # Token inválido
            if len(stack) > 0 and stack[-1] == "while":
                if (len(stack) == 1 and len(tokens) > i + 2 and 
                    re.match(r"^[a-z]$", token) and 
                    re.match(r"^[0-9]$", tokens[i + 2]) and 
                    tokens[i + 1] in ("<", ">", "==", ">=", "<=", "!=")):
                    i += 2  # Saltar sobre el condicional del 'while'
                else:
                    return (False, 0, 0, 0)  # Condicional inválido
        i += 1

    # Devolver los resultados
    return (len(stack) == 0, len(variables_distinct), operadores_comp, whiles)

# Ejecución del programa
ruta_archivo = seleccionar_archivo()  # Seleccionar el archivo
if ruta_archivo:
    content = leer_archivo_en_lista(ruta_archivo)  # Leer el contenido del archivo
    if content:
        tokens = tokenizar_contenido(content)  # Tokenizar el contenido
        resultado = validar_whiles(tokens)  # Validar los bloques 'while'
        # Imprimir los resultados
        print(f"Bloques válidos: {resultado[0]}")
        print(f"Variables distintas: {resultado[1]}")
        print(f"Operadores de comparación: {resultado[2]}")
        print(f"Bloques while: {resultado[3]}")
    else:
        print("No se pudo leer el archivo.")  # Error al leer el archivo
else:
    print("No se seleccionó ningún archivo.")  # No se seleccionó un archivo
