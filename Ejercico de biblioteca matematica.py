import math

def area_circulo(radio):
    """
    Calcula el área de un círculo.

    Args:
        radio (float): Radio del círculo.

    Returns:
        float: Área del círculo.
    """
    return math.pi * radio ** 2


def es_primo(n):
    """
    Determina si un número es primo.

    Args:
        n (int): Número a evaluar.

    Returns:
        bool: True si es primo, False si no.
    """
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def factorial(n):
    """
    Calcula el factorial de un número.

    Args:
        n (int): Número entero.

    Returns:
        int: Factorial del número.
    """
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def fibonacci(n):
    """
    Retorna los primeros n números de Fibonacci.

    Args:
        n (int): Cantidad de números.

    Returns:
        list: Lista con la serie de Fibonacci.
    """
    serie = []
    a, b = 0, 1

    for _ in range(n):
        serie.append(a)
        a, b = b, a + b

    return serie


def celsius_a_fahrenheit(c):
    """
    Convierte Celsius a Fahrenheit.

    Args:
        c (float): Temperatura en Celsius.

    Returns:
        float: Temperatura en Fahrenheit.
    """
    return (c * 9/5) + 32


def maximo(lista):
    """
    Encuentra el número máximo de una lista.

    Args:
        lista (list): Lista de números.

    Returns:
        int: Número máximo.
    """
    mayor = lista[0]

    for num in lista:
        if num > mayor:
            mayor = num

    return mayor


print("FUNCIONES DISPONIBLES")
print("1. Área de círculo")
print("2. Número primo")
print("3. Factorial")
print("4. Fibonacci")
print("5. Celsius a Fahrenheit")
print("6. Máximo de una lista")

opcion = int(input("Elige una opción (1-6): "))


if opcion == 1:
    radio = float(input("Ingrese el radio: "))
    print("Área:", area_circulo(radio))

elif opcion == 2:
    n = int(input("Ingrese un número: "))
    print("¿Es primo?:", es_primo(n))

elif opcion == 3:
    n = int(input("Ingrese un número: "))
    print("Factorial:", factorial(n))

elif opcion == 4:
    n = int(input("Cuántos números de Fibonacci quiere?: "))
    print("Serie:", fibonacci(n))

elif opcion == 5:
    c = float(input("Ingrese grados Celsius: "))
    print("Fahrenheit:", celsius_a_fahrenheit(c))

elif opcion == 6:
    numeros = input("Ingrese números separados por espacio: ")
    lista = [int(x) for x in numeros.split()]
    print("Máximo:", maximo(lista))

else:
    print("Opción no válida")