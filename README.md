# FundamentosMatematicosDeLaComputacion

Este proyecto consiste en construir un sencillo reconocedor de declaraciones de variables de un lenguaje de programación.

El programa lee datos de entrada, una serie de declaraciones de variables y arroja como resultado una serie de estadísticas relacionadas con las variables declaradas y sus tipos.

## Especificaciones

El programa lee los datos de entrada de un archivo, el cual se le pasa por medio de la línea de comandos o se carga por medio de una ventana de dialogo de abrir archivo.

El programa utiliza expresiones regulares para realizar el análisis de la entrada.

El programa reconoce todos los tipos de declaraciones de variables del lenguaje Java, al menos en su versión 1.8 (SE 8).

La salida del programa contiene los siguientes datos:

- Numero total de variables declaradas.
- Numero total de tipos utilizados en las declaraciones encontradas.
- Numero total de variables declaradas de cada tipo.
- Numero total de variables inicializadas.
- Numero total de variables de tipo arreglo.
- Número total de declaraciones constantes (es decir, el valor no se puede cambiar después de la inicialización).
- Clasificación de todos los nombres de variables por tipo declarado.
- El formato de la salida es ###

## Uso del proyecto

1. Correr el programa [codigo.py](codigo.py)
2. Abrir la carpeta `FundamentosMatematicosDeLaComputacion`
3. Seleccionar el archivo [Variables.txt](Variables.txt)

### Tipos de variables en Java

#### Tipos Numéricos

##### Enteros

- byte: 8 bits, rango de -128 a 127.
  - ejemplo: byte diasMes = 31;
- short: 16 bits, rango de -32,768 a 32,767.
  - ejemplo: short diasLustro = (12 _ 31) _ 5;
- int: 32 bits, rango de -2^31 a 2^31-1.
  - ejemplo: int edad = 30;
- long: 64 bits, rango de -2^63 a 2^63-1.
  -ejemplo:long añoLuz = velocidadLuz \* 365;

##### Punto Flotante

- float: 32 bits, rango de aproximadamente ±1.4E-45 a ±3.4028235E38.
  - ejemplo: float pi = 3.1415926535f;
- double: 64 bits, rango de aproximadamente ±4.9E-324 a ±1.7976931348623157E308.
  - ejemplo: double e = 2.718281828459045235360

#### Tipos No Numéricos

##### Carácter

- char: 16 bits, utilizado para almacenar caracteres Unicode, rango de '\u0000' (0) a '\uffff' (65,535).
  - ejemplos:
    -char letraA = 'a';
    -char letraANumerico = 61;

##### Booleano

- boolean: representa dos valores: true y false.
  - ejemplo: boolean verdadero = true;

##### Declaraciones de Arrays

- ejemplos:
  - int[] numeros = {1, 2, 3};
  - String[] nombres = {"Ana", "Luis", "Carlos"};
  - boolean[] valores = {true, false, true};
  - byte[] byteArray = {10, 20, 30, 40, 50};
  - short[] shortArray = {1000, 2000, 3000, 4000, 5000};
  - long[] longArray = {10000000000L, 20000000000L, 30000000000L, 40000000000L, 50000000000L};
  - float[] floatArray = {1.2f, 3.4f, 5.6f, 7.8f, 9.0f};
  - double[] doubleArray = {1.23, 4.56, 7.89, 0.12, 3.45};
  - char[] charArray = {'H', 'o', 'l', 'a', '!'};
  - boolean[] booleanArray = {true, false, true, false, true};
