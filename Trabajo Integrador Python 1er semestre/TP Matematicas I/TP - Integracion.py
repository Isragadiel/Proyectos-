# Calculadora binaria
import sys

def son_todos_digitos(numero: str) -> bool: 
    """
    Verifica si el número pasado como argumento contiene solo dígitos.

    Args:
        numero (str): Cadena a verificar.

    Returns:
        bool: True si la cadena contiene solo dígitos, False en caso contrario.
    """
    return numero.isdigit()

def tiene_longitud(numero: str) -> bool:
    """
    Verifica que el número pasado como argumento tiene longitud.

    Args:
        numero (str): Cadena a verificar.

    Returns:
        bool: True si la cadena tiene al menos un carácter, False si está vacía.
    """
    return len(numero) != 0

def es_binario(numero: str) -> bool:
    """
    Verifica si el número pasado como argumento es un número binario.

    Args:
        numero (str): Cadena a verificar.

    Returns:
        bool: True si la cadena es un número binario, False en caso contrario.
    """
    for i in range(0, len(numero)):
        if int(numero[i]) < 0 or int(numero[i]) > 1:
            return False
    return True

def validar_numero_binario(mensaje: str) -> str:
    """
    Solicita al usuario un número binario y válida:
    * que la cadena no esté vacía.
    * que la cadena contenga solo digitos.
    * que la cadena contenga números 0 y 1

    Args:
        mensaje (str): Mensaje que se muestra al usuario para solicitar el número.

    Returns:
        str: El número binario válido ingresado por el usuario.
    """
    num: str = input(mensaje)

    if not (tiene_longitud(num) and son_todos_digitos(num)):
        return validar_numero_binario("El numero ingresado no es valido, ingrese otro: ")

    if not (es_binario(num)):
        return validar_numero_binario("El numero ingresado no es binario, ingrese otro: ")

    return num

def convertir_a_decimal(numero: str) -> int:
    """
    Convierte una cadena binaria a su valor decimal.

    Args:
        numero (str): Cadena que representa un número binario.

    Returns:
        int: Valor decimal equivalente.
    """
    decimal: int = 0

    for i in range(len(numero), 0, -1):
        decimal += int(numero[i-1]) * (2 ** (len(numero)-i))
    return decimal

def convertir_a_dec_binario_neg(binario: str) -> int:
    """
    Convierte una cadena binaria negativo, a su valor decimal.

    Args:
        numero (str): Cadena que representa un número binario negativo.

    Returns:
        int: Valor decimal equivalente.
    """
    decimal: int = 0
    binario = complementoA2(binario)

    for i in range(len(binario), 0, -1):
        decimal += int(binario[i-1]) * (2 ** (len(binario)-i))
    return decimal * -1



def rellenar_con_ceros_izquierda(numero: str, longitud: int) -> str:
    """
    Rellena con ceros a la izquierda para igualar la longitud de los números binarios.

    Args:
        numero (str): Número binario como cadena.
        longitud (int): Cantidad de ceros a agregar.

    Returns:
        str: Número binario con ceros agregados a la izquierda.
    """
    numero_invertido = numero[::-1]
    numero_invertido += longitud * "0"
    return numero_invertido[::-1]

def igualar_numeros(binario1: str, binario2: str):
    """
    Verifica si los dos numeros ingresados por el usuario tienen la misma cantidad de bits 
    caso contrario, los iguala.

    Args: binario1(str) y binario2(str) numeros binarios como cadenas

    Returns:
        str: Los dos número binario recibidos, igualados en cantidad de bits.
    """
    longitud = abs(len(binario1) - len(binario2))
    if len(binario1) > len(binario2):
        binario2 = rellenar_con_ceros_izquierda(binario2, longitud)
    else:
        binario1 = rellenar_con_ceros_izquierda(binario1, longitud)
    return (binario1, binario2)

def sumar(numeros: list[str]):
    """
    Suma dos números binarios representados como cadenas.

    Args:
        numeros (list[str]): Lista con dos cadenas que representan números binarios.

    Returns:
        str: Resultado de la suma en binario.
    """
    binario1: str = numeros[0]
    binario2: str = numeros[1]
    resultado : str = ""
    carry: int = 0

    binario1, binario2 = igualar_numeros(binario1, binario2)

    def sumando(num1: str, num2: str) -> None:
        """
        Suma dos dígitos binarios (como caracteres) y actualiza el resultado y el carry globales.

        Args:
            num1 (str): Primer dígito binario a sumar ('0' o '1').
            num2 (str): Segundo dígito binario a sumar ('0' o '1').

        Returns:
            None: Modifica las variables 'resultado' y 'carry' no locales.
        """
        nonlocal carry
        nonlocal resultado 

        if int(num1) == 0 and int(num2) == 0:
            carry -= 1
            resultado  += "0"
        elif (int(num1) == 0 and int(num2) == 1) or (int(num1) == 1 and int(num2) == 0):
            carry -= 1
            resultado  += "1"
        else:
            carry += 1
            resultado  += "0"

    def sumando_con_carry(num1: str, num2: str) -> str:
        """
        Suma dos dígitos binarios considerando el acarreo previo y devuelve el resultado como carácter.

        Args:
            num1 (str): Primer dígito binario a sumar ('0' o '1').
            num2 (str): Segundo dígito binario a sumar ('0' o '1').

        Returns:
            str: Resultado de la suma considerando el acarreo ('0' o '1').
        """
        nonlocal carry

        if (int(num1) == 0 and int(num2) == 1) or (int(num1) == 1 and int(num2) == 0):
            carry -= 1
            return "1"
        else:
            carry += 1
            return "0"

    for i in range(len(binario1)-1, -1, -1):
        # Reiniciamos el carry en caso negativo
        if carry < 0:
            carry = 0

        if carry > 0:
            sumando(sumando_con_carry(binario1[i], "1"), binario2[i]) 
        else:
            sumando(binario1[i], binario2[i])

    # Añadimos el carry final si es 1
    if carry > 0:
        resultado += "1"

    # Verificación
    decimal1 = convertir_a_decimal(binario1)
    decimal2 = convertir_a_decimal(binario2)
    total = decimal1 + decimal2
    resultado_decimal = convertir_a_decimal(resultado[::-1])
    if total == resultado_decimal:
        print("Suma verificada...")

    return resultado[::-1]

def complementoA2(binario2: str):
    """
    Recibe un binario como cadena, lo invierte y suma 1 

    Arg: binario2(str) numero binario como cadena

    Returns:
            str: El complemento A2 del numero dado.
    """
    binarioA1 = ""
    for i in range(len(binario2)):
        if int(binario2[i]) == 0:
            binarioA1 += "1"
        else:
            binarioA1 += "0"

    binarioA2 = sumar([binarioA1, "1"])
    return binarioA2

def restar(numeros: list[str]):
    """
    Resta dos números binarios representados como cadenas.

    Args:
        numeros (list[str]): Lista con dos cadenas que representan números binarios.

    Returns:
        str: Resultado de la resta en binario y en caso de resultado negativo, su expresion en valor absoluto.
    """

    binario1: str = numeros[0]
    binario2: str = numeros[1]
    resultado : str = ""

    binario1, binario2 = igualar_numeros(binario1, binario2)

    def comprobar(binario1,binario2, resultado):
        decimal1 = convertir_a_decimal(binario1)
        decimal2 = convertir_a_decimal(binario2)
        total = decimal1 - decimal2
        if decimal1 >= decimal2:
            resultado_decimal = convertir_a_decimal(resultado)
        else:
            resultado_decimal = convertir_a_dec_binario_neg(resultado)
        if total == resultado_decimal:
                return "Resta verificada..."    

    if binario1 >= binario2:
        resultado = sumar([binario1, complementoA2(binario2)])
        if len(resultado) > len(binario2):
            resultado = resultado[1:]
            print(comprobar(binario1,binario2,resultado))
            return resultado.lstrip('0') or "0"
    else:
        resultado = sumar([binario1, complementoA2(binario2)])
        if len(resultado) > len(binario2):
            resultado1 = complementoA2(resultado[1:])
            print(comprobar(binario1,binario2,resultado))
            return resultado1.lstrip('0') or "0"
        else:
           resultado1 = complementoA2(resultado)
           print(comprobar(binario1,binario2,resultado))
           return resultado1.lstrip('0') or "0"

        

def multiplicar(numeros: list[str]) -> str:
    """
    Multiplica dos números binarios representados como cadenas.

    Args:
        numeros (list[str]): Lista con dos cadenas que representan números binarios.

    Returns:
        str: Resultado de la multiplicación en binario.
    """
    binario1, binario2 = numeros

    # Inicializar el resultado con ceros
    resultado = "0"

    # Para cada bit del segundo número
    # for i, bit in enumerate(binario2):
    for i in range(len(binario2)-1, -1, -1):
        if binario2[i] == '1':
            # Si el bit es 1, multiplicamos el primer número por 2^i
            # Esto es equivalente a desplazar el primer número i posiciones a la izquierda
            shifted = binario1 + "0" * (len(binario2) - 1 - i)
            # 1010 -> 0101 000
            # Sumamos el resultado parcial al total
            resultado = sumar([resultado, shifted])

    # Verificación
    binario1: str = numeros[0]
    binario2: str = numeros[1]
    decimal1: int = convertir_a_decimal(binario1)
    decimal2: int = convertir_a_decimal(binario2)
    total: int = decimal1 * decimal2
    resultado_decimal = convertir_a_decimal(resultado)
    if total == resultado_decimal:
        print("Multiplicacion verificada...")

    # Sacar el cero a la izquierda
    return resultado.lstrip("0") or "0"

def comparar_binarios(bin1: str, bin2: str) -> bool:
    """
    Compara dos binarios como cadenas.
    Devuelve True si bin1 es mayor o igual a bin2.
    """
    bin1, bin2 = igualar_numeros(bin1, bin2)  # Igualamos las longitudes agregando ceros a la izquierda
    return bin1 >= bin2  # Comparamos alfabéticamente (en binarios funciona)

def dividir(numeros: list[str]) -> str:
    """
    Divide dos números binarios directamente sin convertir a decimal.
    
    Args:
        numeros (list[str]): Lista con dos cadenas que representan números binarios.

    Returns:
        str: Resultado de la división en binario.
    """
    dividendo = numeros[0]  # Primer número binario
    divisor = numeros[1]    # Segundo número binario

    if divisor == "0":
        return "Error: No se puede dividir por cero"  # Error si intentan dividir por cero

    cociente = ""  # Iniciamos el cociente vacío
    resto = ""     # Iniciamos el resto vacío

    # Recorremos cada bit del dividendo
    for bit in dividendo:
        resto += bit  # Agregamos el bit actual al resto
        resto = resto.lstrip('0') or "0"  # Quitamos ceros a la izquierda

        if comparar_binarios(resto, divisor):
            cociente += "1"  # Si el resto >= divisor, agregamos 1 al cociente
            resto = restar([resto, divisor])  # Y restamos divisor al resto
        else:
            cociente += "0"  # Si no alcanza, agregamos 0 al cociente

    # Verificación
    dividendo_decimal: int = convertir_a_decimal(dividendo)
    divisor_decimal: int = convertir_a_decimal(divisor)
    resultado_decimal = convertir_a_decimal(cociente)
    if dividendo_decimal // divisor_decimal == resultado_decimal:
        print("División verificada...")

    # Limpiamos ceros a la izquierda del cociente
    return cociente.lstrip('0') or "0"

def calculadora():
    """
    Menú principal de la calculadora binaria.
    Permite seleccionar la operación y solicita los números binarios al usuario.
    """
    print("\nElije la operacion a realizar del siguiente menu:\n ")
    print("1 - Sumar \n2 - Resta \n3 - Multiplicar \n4 - Dividir\n5 - Salir")
    operacion: int = int(input("\nIngrese la operacion elegida: "))
    lista_de_operadores: tuple = (1, 2, 3, 4, 5)
    if operacion not in lista_de_operadores:
        print("Opcion no valida, intente de nuevo")
        return
    elif operacion == lista_de_operadores[4]:
        sys.exit()

    numeros: list = []
    for i in range(0, 2):
        numeros.append(validar_numero_binario(f"Ingrese el numero binario {i+1}: "))

    if operacion == lista_de_operadores[0]:
        print(f"El resultado de la suma es: {sumar(numeros)}")
    elif operacion == lista_de_operadores[1]:
        print(f"{restar(numeros)}")
    elif operacion == lista_de_operadores[2]:
        print(f"El resultado es: {multiplicar(numeros)}")
    elif operacion == lista_de_operadores[3]:
        print(f"El resultado es: {dividir(numeros)}")

calculadora()



"""
# TEST CASES

# Caso 1: Suma básica
print("Caso 1: Suma básica")
numeros = ["1010", "0101"]  # 10 + 5 = 15
resultado = sumar(numeros)
assert resultado == "1111", f"Error: Se esperaba '1111' pero obtuvo '{resultado}'"

# Caso 2: Suma con carry
print("Caso 2: Suma con carry")
numeros = ["1111", "01"]  # 15 + 1 = 16
resultado = sumar(numeros)
assert resultado == "10000", f"Error: Se esperaba '10000' pero obtuvo '{resultado}'"

# ---------------------- #

# Caso 1: Resta básica
print("Caso 1: Resta básica")
numeros = ["1010", "0101"]  # 10 - 5 = 5
resultado = restar(numeros)
print(resultado)
assert resultado == "101", f"Error: Se esperaba '101' pero obtuvo '{resultado}'"

# Caso 2: Resta con resultado en valor absoluto
print("Caso 2: Resta con resultado en valor absoluto")
numeros = ["0011", "1001"]  # 3 - 9 = -6 (resultado en valor absoluto)
resultado = restar(numeros)
print(resultado)
assert resultado == "110", f"Error: Se esperaba '110' pero obtuvo '{resultado}'"
# assert resultado == "0110", f"Error: Se esperaba '0110' pero obtuvo '{resultado}'"

# ---------------------- #

# Caso 1: Multiplicación básica
print("Caso 1: Multiplicación básica")
numeros = ["1010", "0101"]  # 10 * 5 = 50
resultado = multiplicar(numeros)
print(resultado)
assert resultado == "110010", f"Error: Se esperaba '110010' pero obtuvo '{resultado}'"

# Caso 2: Multiplicación por 0
print("Caso 2: Multiplicación por 0")
numeros = ["1111", "0000"]  # 15 * 0 = 0
resultado = multiplicar(numeros)
print(resultado)
assert resultado == "0", f"Error: Se esperaba '0' pero obtuvo '{resultado}'"

# ---------------------- #

# Caso 1: División básica
print("Caso 1: División básica")
numeros = ["1010", "101"]  # 10 / 5 = 2
resultado = dividir(numeros)
print(resultado)
assert resultado == "10", f"Error: Se esperaba '10' pero obtuvo '{resultado}'"

# Caso 2: División con residuo
print("Caso 2: División con residuo")
numeros = ["1101", "0101"]  # 13 / 5 = 2 (resultado entero)
resultado = dividir(numeros)
print(resultado)
assert resultado == "10", f"Error: Se esperaba '10' pero obtuvo '{resultado}'"

# Caso 3: Divisor mas grande que dividendo
print("Caso 3: Divisor mas grande que dividendo")
numeros = ["1101", "111101"]  # 13 / 61 = 0,2131147540983607 (resultado entero)
resultado = dividir(numeros)
print(resultado)
assert resultado == "0", f"Error: Se esperaba '0' pero obtuvo '{resultado}'"
"""