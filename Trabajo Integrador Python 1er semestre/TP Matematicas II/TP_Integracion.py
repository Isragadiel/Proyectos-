# Generación automática de los conjuntos de dígitos únicos.
exp_log = "X’ != ∅,  donde X=union de los conjuntos generados y U={x∣x ∈ Z y 0 ≤ x ≤ 9}." \
"En lenguaje natural: El complemento del conjunto X, siendo X la unión de los conjuntos generados a partir de los DNI ingresados," \
" respecto al conjunto universal definido como U={0,1,2,3,4,5,6,7,8,9}, no es un conjunto vacío."

exp_log2="∣A∣=1. En lenguaje natural: Siendo el conjunto A la intersección de los todos los conjuntos formados con los DNI " \
"ingresados, existe un único dígito representativo"

def generador_de_conjuntos(dni: int):
    conjuntos: list[int] = []
    for i in range(10):
        if str(i) in str(dni):
            conjuntos.append(i)
    return conjuntos

# Suma total de los dígitos de cada DNI.
def suma_dni(dni: int):
    if dni == 0:
        return 0
    else:
        return dni % 10 + suma_dni(dni // 10)

def es_bisiesto(anio):
    """
    Determina si un año es bisiesto.
    Un año es bisiesto si es divisible por 4, 
    excepto los divisibles por 100, a menos que también sean divisibles por 400.
    """
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

# Operaciones con años de nacimiento
def nacimientos():
    print("Ingrese los años de nacimiento de los integrantes (ingrese 'fin' para terminar):")
    anios = []

    while True:
        entrada = input("Año de nacimiento (o 'fin' para terminar): ")
        if entrada.lower() == 'fin':
            if len(anios) < 2:
                print("Debe ingresar al menos dos años de nacimiento.")
                continue
            break

        anio = int(entrada)
        if anio < 1925 or anio > 2025:
            print("Por favor ingrese un año válido (entre 1925 y 2025).")
            continue
        anios.append(anio)

    pares = 0
    impares = 0

    for anio in anios:
        if anio % 2 == 0:
            pares += 1
        else:
            impares += 1

    print(f"\nNacieron {pares} personas en años pares y {impares} en años impares.")

    if all(anio > 2000 for anio in anios):
        print("Grupo Z")

    bisiestos = [anio for anio in anios if es_bisiesto(anio)]
    if bisiestos:
        print(f"Tenemos un año especial: {', '.join(map(str, bisiestos))} es/son bisiesto(s).")

    print("\nProducto cartesiano (año de nacimiento, edad en 2025):")
    for anio in anios:
        edad = 2025 - anio
        print(f"({anio}, {edad})", end=" ")
    print("\n")

# Union de conjuntos 
def union(dnis: list[int]) -> list[int]:
    if not dnis:
        return []

    conjunto_unico = set()
    for dni in dnis:
        conjunto_unico.update(generador_de_conjuntos(dni))

    return list(conjunto_unico)

# Diferencia de dos conjuntos A - B
def diferencia(lista_dni: list) -> list:
    """
    Realiza la diferencia de dos conjuntos A y B

    Args:
        List: Con los documentos ingresados por el usuario.

    Returns:
          List: conjunto formado por la diferencia de A - B
    """

    a = generador_de_conjuntos(lista_dni[0])  # Tomo el indice 0 de la lista y se lo paso a la función gnerador_de_conjuntos
    b = generador_de_conjuntos(lista_dni[1])  # Tomo el indice 1 de la lista y se lo paso a la función gnerador_de_conjuntos
    d = []  # Creamos una lista vacia para almacenar los valores del conjunto que será la diferencia entre A y B
    for i in range(len(a)):
        if a[i] not in b:  # Este condicional me selecciona los elementos de A que no están en B, y los guarda en la lista d
            d.append(a[i])
    return d

# Complemento del conjunto Union.
def complemento_U(lista_dni) -> bool:
    """
    Realiza el complemento del conjunto X, siendo X una union de conjuntos formados por dígitos del 0 al 9 
    a partir de los DNI de los usuarios, respecto al conjunto universal definido como x/x ∈ Z y 0<= x <= 9.

    Args:
        List: Con los documentos ingresados por el usuario.

    Returns:
          Bool: True si no es un conjunto vacio y False si es un conjunto vacio.
    """
    x = union(lista_dni) 
    c = []
    for i in range(10):
        if i not in x:
            c.append(i)

    if c == []:
        return False
    else:
        return True

# Interseccion
def interseccion(dnis: list[int]) -> list[int]:
    if not dnis:
        return []

    conjunto_comun = set(generador_de_conjuntos(dnis[0]))

    for dni in dnis[1:]:
        conjunto_comun.intersection_update(generador_de_conjuntos(dni))

    return list(conjunto_comun)

# Funcion: Conteo de frecuencia de dígitos en un DNI
def frecuencia_digitos(dni: int) -> dict:
    """
    Cuenta la frecuencia de cada dígito (0-9) en el DNI dado.

    Args:
        dni (int): DNI a analizar

    Returns:
        dict: Diccionario con la frecuencia de cada dígito
    """
    frecuencia = {str(i): 0 for i in range(10)}  # inicializo con 0 para todos los dígitos como strings
    for digito in str(dni):
        frecuencia[digito] += 1
    return frecuencia

# Ejemplo simple para mostrar frecuencias de un DNI
def mostrar_frecuencia(dni: int):
    freq = frecuencia_digitos(dni)
    print(f"Frecuencia de dígitos en el DNI {dni}:")
    for digito, cantidad in freq.items():
        print(f"Dígito {digito}: {cantidad} vez/veces")
    print()

# FUNCIÓN: Diferencia Simétrica
def diferencia_simetrica(lista_dni: list) -> list:
    """
    Realiza la diferencia simétrica de dos conjuntos A y B.
    La diferencia simétrica incluye elementos que están en A o en B, pero no en ambos.

    Args:
        lista_dni (list): Lista con los documentos ingresados por el usuario (se toman los dos primeros).

    Returns:
        list: Conjunto formado por la diferencia simétrica de A y B.
    """
    #Verifica si hay al menos dos DNI en la lista. Si no, retorna una lista vacía
    if len(lista_dni) < 2:
        return []
#Se utilizan los dos primeros DNIs de lista_dni para generar sus respectivos conjuntos de dígitos 
# únicos usando función generador_de_conjuntos.
    conjunto_a = set(generador_de_conjuntos(lista_dni[0]))
    conjunto_b = set(generador_de_conjuntos(lista_dni[1]))

    # La diferencia simétrica se puede calcular como (A - B) U (B - A)
    # O de forma más eficiente con el método .symmetric_difference() de los conjuntos
    diferencia_simetrica_set = conjunto_a.symmetric_difference(conjunto_b)

    return sorted(list(diferencia_simetrica_set))

# Pedimos una lista de DNIs para trabajar
def pedir_dnis(opcion):
    dnis = []
    print("Ingrese los DNIs de los integrantes (ingrese 'fin' para terminar):")
    if opcion == "1" or opcion == "2":
        while True:
            entrada = input("DNI (o 'fin' para terminar): ")
            if entrada.lower() == 'fin':
                if len(dnis) < 2:
                    print("Debe ingresar al menos dos DNIs.")
                    continue
                break
            if not entrada.isdigit():
                print("Por favor ingrese solo números.")
                continue
            dnis.append(int(entrada))
    else:
        while len(dnis) < 2:
            entrada = input("Ingrese el DNI: ")
            if not entrada.isdigit():
                print("Por favor ingrese solo números.")
                continue
            dnis.append(int(entrada))

    return dnis

def main():
    while True:
        print("\n--- MENÚ DE OPERACIONES CON CONJUNTOS ---")
        print("1. Unión")
        print("2. Intersección")
        print("3. Diferencia (A - B)")
        print("4. Diferencia simétrica (A ∆ B)")
        print("5. Operaciones con años de nacimiento")
        print("6. Salir\n---")
        opcion = input("Seleccione una opción: ")

        if opcion in {"1", "2", "3", "4"}:
            dnis = pedir_dnis(opcion)

            print("\n--- CONJUNTOS GENERADOS ---")
            for dni in dnis:
                conjunto = generador_de_conjuntos(dni)
                print(f"El DNI {dni}, forma el conjunto: {conjunto}")
                print(f"\nFrecuencia de dígitos:\n")
                mostrar_frecuencia(dni)
                print(f"Suma total de dígitos: {suma_dni(dni)}")

            if opcion == "1":
                resultado = union(dnis)
                print("\nUnión de todos los conjuntos:", resultado)
                print("\nExpresion lógica\n")
                print(exp_log)
                print(f"\nEl resultado de la expresion es: {complemento_U(dnis)}")

            elif opcion == "2":
                resultado = interseccion(dnis)
                print("\nIntersección de los conjuntos:", resultado)
                print("\nExpresion lógica\n")
                print(exp_log2)
                if len(resultado) == 1:
                    print(f"\nEl resultado de la expresion es: Verdadero.")
                else:
                    print(f"\nEl resultado de la expresion es: Falso.")

            elif opcion == "3":
                resultado = diferencia(dnis)
                print(f"Diferencia de {dnis[0]} - {dnis[1]}:", resultado)
                
            elif opcion == "4":
                resultado = diferencia_simetrica(dnis)
                print(f"Diferencia simétrica entre {dnis[0]} y {dnis[1]}:", resultado)
                
        elif opcion == "5":
            nacimientos()
            
        elif opcion == "6":
            print("Fin del programa.")
            break
        else:
            print("Opción inválida. Intentalo nuevamente.")

if __name__ == "__main__":
    main()
