# =====================================================
# EJERCICIO 4 - ANALISIS DE NOTAS
# =====================================================

def promedio(notas):
    suma = 0
    for n in notas:
        suma += n
    return suma / len(notas)

def mayor(notas):
    m = notas[0]
    for n in notas:
        if n > m:
            m = n
    return m

def menor(notas):
    m = notas[0]
    for n in notas:
        if n < m:
            m = n
    return m

def contar_aprobados(notas, minimo=61):
    cont = 0
    for n in notas:
        if n >= minimo:
            cont += 1
    return cont

# BONUS histograma
def histograma(notas):
    for n in notas:
        print(n,":","*"*(n//10))

def reporte(notas):
    print("Promedio:", promedio(notas))
    print("Mayor:", mayor(notas))
    print("Menor:", menor(notas))
    print("Aprobados:", contar_aprobados(notas))
    histograma(notas)


# Programa principal
notas = [85,42,73,61,55,90,38,77,95,60]
reporte(notas)