# --------------------------------------------
# EJERCICIO 3 - CONVERSOR DE TEMPERATURA
# --------------------------------------------

# Convierte Celsius → Fahrenheit
def celsius_a_fahrenheit(c):
    # Fórmula: F = C * 9/5 + 32
    return c * 9/5 + 32


# Convierte Fahrenheit → Celsius
def fahrenheit_a_celsius(f):
    # Fórmula: C = (F - 32) * 5/9
    return (f - 32) * 5/9


# Convierte Celsius → Kelvin
def celsius_a_kelvin(c):
    # Fórmula: K = C + 273.15
    return c + 273.15


# BONUS: Fahrenheit → Rankine
def fahrenheit_a_rankine(f):
    # Fórmula: R = F + 459.67
    return f + 459.67


# --------------------------------------------
# FUNCION PRINCIPAL DE CONVERSION
# --------------------------------------------
def convertir(valor, origen, destino):

    # Convertimos a mayúsculas por seguridad
    origen = origen.upper()
    destino = destino.upper()

    # Si origen y destino son iguales
    # no hay conversión
    if origen == destino:
        return valor

    # ------------------------------------
    # PASO 1: TODAS LAS ESCALAS → CELSIUS
    # ------------------------------------

    if origen == "F":
        # F → C usando función existente
        valor = fahrenheit_a_celsius(valor)

    elif origen == "K":
        # K → C (despejando fórmula)
        valor = valor - 273.15

    elif origen == "R":
        # R → F → C
        valor = valor - 459.67
        valor = fahrenheit_a_celsius(valor)

    elif origen != "C":
        # Escala inválida
        return None

    # Ahora SIEMPRE estamos en Celsius

    # ------------------------------------
    # PASO 2: CELSIUS → DESTINO
    # ------------------------------------

    if destino == "C":
        return valor

    elif destino == "F":
        return celsius_a_fahrenheit(valor)

    elif destino == "K":
        return celsius_a_kelvin(valor)

    elif destino == "R":
        f = celsius_a_fahrenheit(valor)
        return fahrenheit_a_rankine(f)

    else:
        return None


# --------------------------------------------
# PROGRAMA PRINCIPAL
# --------------------------------------------

# Pedimos datos al usuario
v = float(input("Valor: "))
o = input("Origen (C/F/K/R): ")
d = input("Destino (C/F/K/R): ")

# Mostramos resultado
print("Resultado:", convertir(v, o, d))