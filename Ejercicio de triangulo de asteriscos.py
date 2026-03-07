# Triángulo de asteriscos
n = 5
for i in range(1, n + 1):
    print("*" * i)

# Triángulo invertido
for i in range(n, 0, -1):
    print("*" * i)

# Pirámide centrada
for i in range(1, n + 1):
    espacios = " " * (n - i)
    estrellas = "*" * (2 * i - 1)
    print(espacios + estrellas)

    # Parte inferior del diamante
for i in range(n - 1, 0, -1):
    espacios = " " * (n - i)
    estrellas = "*" * (2 * i - 1)
    print(espacios + estrellas)


