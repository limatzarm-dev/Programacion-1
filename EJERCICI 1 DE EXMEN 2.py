# =====================================================
# EJERCICIO 1 - CAJERO AUTOMATICO
# =====================================================

def calcular_billetes(monto):

    # Validar múltiplo de 5 (bonus incluido)
    if monto % 5 != 0:
        print("Error: el monto debe ser múltiplo de 5")
        return None

    # Billetes
    b200 = monto // 200
    monto %= 200

    b100 = monto // 100
    monto %= 100

    b50 = monto // 50
    monto %= 50

    b20 = monto // 20
    monto %= 20

    b10 = monto // 10
    monto %= 10

    b5 = monto // 5

    # Resultado
    print("\nBilletes entregados:")
    print(b200,"Q200,",b100,"Q100,",b50,"Q50,",b20,"Q20,",b10,"Q10,",b5,"Q5")


# Programa principal
monto = int(input("Ingrese monto: Q"))
calcular_billetes(monto)