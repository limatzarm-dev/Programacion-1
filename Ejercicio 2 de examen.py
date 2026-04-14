# EJERCICIO 2 - VALIDAR PASSWORD

def tiene_mayuscula(texto):
    for c in texto:
        if c.isupper():
            return True
    return False

def tiene_digito(texto):
    for c in texto:
        if c.isdigit():
            return True
    return False

def tiene_especial(texto):
    especiales = "!@#$%"
    for c in texto:
        if c in especiales:
            return True
    return False

# BONUS: evitar 3 caracteres iguales seguidos
def tres_iguales(texto):
    for i in range(len(texto)-2):
        if texto[i] == texto[i+1] == texto[i+2]:
            return True
    return False

def validar_password(password):
    if len(password) < 8:
        return False
    if not tiene_mayuscula(password):
        return False
    if not tiene_digito(password):
        return False
    if not tiene_especial(password):
        return False
    if tres_iguales(password):
        return False
    return True

def diagnosticar_password(password):

    if len(password) < 8:
        print("Faltan caracteres")

    if not tiene_mayuscula(password):
        print("Falta mayúscula")

    if not tiene_digito(password):
        print("Falta número")

    if not tiene_especial(password):
        print("Falta carácter especial")

    if tres_iguales(password):
        print("Tiene 3 caracteres iguales seguidos")


# Programa principal
pwd = input("Ingrese contraseña: ")

if validar_password(pwd):
    print("Password válida")
else:
    diagnosticar_password(pwd)