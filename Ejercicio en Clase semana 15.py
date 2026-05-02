class Estudiante:
    def _init_(self, nombre, carnet, carrera):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def aprobado(self):
        return self.promedio() >= 61


# --- PROGRAMA PRINCIPAL ---

nombre = input("Ingrese nombre: ")
carnet = input("Ingrese carnet: ")
carrera = input("Ingrese carrera: ")

est = Estudiante(nombre, carnet, carrera)

cantidad = int(input("¿Cuántas notas desea ingresar?: "))

for i in range(cantidad):
    nota = float(input(f"Ingrese nota {i+1}: "))
    est.agregar_nota(nota)

print("\n--- RESULTADOS ---")
print("Nombre:", est.nombre)
print("Carnet:", est.carnet)
print("Carrera:", est.carrera)
print("Promedio:", est.promedio())
print("¿Aprobado?:", est.aprobado())