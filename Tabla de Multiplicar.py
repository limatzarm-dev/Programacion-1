# Tabla de multiplicar
num = int(input("¿Tabla del? "))

print(f"\n--- Tabla del {num} ---")
for i in range(1, 13):
    resultado = num * i
    print(f"{num} x {i:2d} = {resultado:3d}")

# Salida para num = 7:
# --- Tabla del 7 ---
# 7 x 1 =  7
# 7 x 2 = 14
# ...
# 7 x 12 = 84

# Programa de tablas de multiplicar

while True:
    num = int(input("¿Qué tabla quieres ver? "))

    print("\n--- Tabla del", num, "---")
    
    i = 1
    while i <= 12:
        print(num, "x", i, "=", num * i)
        i += 1

    input("\nPresiona Enter para pedir otra tabla...")
