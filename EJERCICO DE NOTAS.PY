notas = [85, 42, 92, 55, 78, 30, 95]
aprobados = []
reprobados = []

tareas = []
completadas = []

while True:
    print("\n--- MENÚ ---")
    print("1. Ver aprobados y reprobados")
    print("2. Agregar tarea")
    print("3. Ver tareas")
    print("4. Marcar tarea como completada")
    print("5. Eliminar tarea")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        aprobados = []
        reprobados = []

        for nota in notas:
            if nota >= 60:
                aprobados.append(nota)
            else:
                reprobados.append(nota)

        print("Aprobados:", aprobados)
        print("Reprobados:", reprobados)
        print("Tasa:", len(aprobados), "/", len(notas))

    elif opcion == "2":
        tarea = input("Escribe la tarea: ")
        tareas.append(tarea)

    elif opcion == "3":
        print("\nTareas pendientes:")
        for i, tarea in enumerate(tareas):
            print(i, "-", tarea)

    elif opcion == "4":
        for i, tarea in enumerate(tareas):
            print(i, "-", tarea)

        indice = int(input("Número de tarea: "))
        completadas.append(tareas.pop(indice))
        print("Tarea completada.")

    elif opcion == "5":
        for i, tarea in enumerate(tareas):
            print(i, "-", tarea)

        indice = int(input("Número de tarea a eliminar: "))
        tareas.pop(indice)

    elif opcion == "6":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida.")