# 1. Crear una tupla con las coordenadas de tu ciudad (ejemplo: Antigua Guatemala)
coordenadas = (14.5586, -90.7339)

# 2. Desempaquetar en variables lat, lon
lat, lon = coordenadas
print("Latitud:", lat)
print("Longitud:", lon)

# 3. Función que retorna (min, max, promedio) de una lista
def estadisticas(lista):
    minimo = min(lista)
    maximo = max(lista)
    promedio = sum(lista) / len(lista)
    return (minimo, maximo, promedio)

# Probando la función
numeros = [10, 20, 30, 40, 50]
resultado = estadisticas(numeros)
print("Resultados (min, max, promedio):", resultado)

# 4. Usar tuplas como claves de un diccionario
distancias = {
    ("Guate", "Escuintla"): 58,
    ("Guate", "Antigua"): 45
}

print("Distancia Guate - Antigua:", distancias[("Guate", "Antigua")])

# 5. Intentar modificar un elemento de la tupla
try:
    coordenadas[0] = 15.0  # Esto dará error
except TypeError as e:
    print("Error:", e)
    # Comentario: Las tuplas son inmutables, no se pueden modificar después de creadas.