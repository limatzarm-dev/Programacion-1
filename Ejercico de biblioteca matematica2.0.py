import math
import os

def area_circulo(radio):
    """
    Calcula el área de un círculo.

    Args:
        radio (float): Radio del círculo.

    Returns:
        float: Área del círculo calculada con π * r².
    """
    return math.pi * radio ** 2


def es_primo(n):
    """
    Determina si un número es primo.

    Args:
        n (int): Número a evaluar.

    Returns:
        bool: True si el número es primo, False si no lo es.
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
        int: Resultado del factorial de n.
    """
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def fibonacci(n):
    """
    Genera los primeros n números de Fibonacci.

    Args:
        n (int): Cantidad de números a generar.

    Returns:
        list: Lista con los primeros n números de Fibonacci.
    """
    serie = []
    a, b = 0, 1

    for _ in range(n):
        serie.append(a)
        a, b = b, a + b

    return serie


def celsius_a_fahrenheit(c):
    """
    Convierte temperatura de Celsius a Fahrenheit.

    Args:
        c (float): Temperatura en grados Celsius.

    Returns:
        float: Temperatura convertida a grados Fahrenheit.
    """
    return (c * 9/5) + 32


def maximo(lista):
    """
    Encuentra el valor máximo de una lista sin usar max().

    Args:
        lista (list): Lista de números.

    Returns:
        int or float: El número mayor encontrado en la lista.
    """
    mayor = lista[0]

    for num in lista:
        if num > mayor:
            mayor = num

    return mayor


while True:

    print("\nFUNCIONES DISPONIBLES")
    print("1. Área de círculo")
    print("2. Número primo")
    print("3. Factorial")
    print("4. Fibonacci")
    print("5. Celsius a Fahrenheit")
    print("6. Máximo de una lista")
    print("0. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 0:
        print("Programa terminado")
        break

    elif opcion == 1:
        radio = float(input("Ingrese el radio: "))
        print("Área:", area_circulo(radio))

    elif opcion == 2:
        n = int(input("Ingrese un número: "))
        print("¿Es primo?:", es_primo(n))

    elif opcion == 3:
        n = int(input("Ingrese un número: "))
        print("Factorial:", factorial(n))

    elif opcion == 4:
        n = int(input("¿Cuántos números de Fibonacci quiere?: "))
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

    input("\nPresione ENTER para continuar...")
    os.system("cls" if os.name == "nt" else "clear")