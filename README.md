# FundamentosMatematicosDeLaComputacion
### Tipos de variables en Java
#### Tipos Numéricos

##### Enteros
- byte: 8 bits, rango de -128 a 127.
   - ejemplo: byte diasMes = 31; 
- short: 16 bits, rango de -32,768 a 32,767.
   - ejemplo: short diasLustro = (12 * 31) * 5;
- int: 32 bits, rango de -2^31 a 2^31-1.
   - ejemplo: int edad = 30;
- long: 64 bits, rango de -2^63 a 2^63-1.
   -ejemplo:long añoLuz = velocidadLuz * 365;
  
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
