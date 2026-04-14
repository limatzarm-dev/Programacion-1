# 1. Crear diccionario con información personal
persona = {
    "nombre": "Leonardo",
    "edad": 18,
    "ciudad": "Antigua Guatemala",
    "lenguaje_favorito": "Python"
}

# 2. Agregar nueva clave 'universidad'
persona["universidad"] = "Universidad de San Pablo"

# 3. Modificar el valor de 'edad'
persona["edad"] = 19

# 4. Iterar con .items() e imprimir cada par
print("Información personal:")
for clave, valor in persona.items():
    print(clave, ":", valor)

# 5. Verificar si 'email' existe con 'in'
if "email" in persona:
    print("El email existe")
else:
    print("El email NO existe")

# 6. Usar .get() para acceder a 'telefono' sin error
telefono = persona.get("telefono", "4784 6729")
print("Teléfono:", telefono)