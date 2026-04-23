def main():
    tareas = []
    while True:
        print("\nMenú")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Salir")
        opcion = input("Selecciona una opción (1-3): ").strip()

        if opcion == "1":
            tarea = input("Escribe la tarea: ").strip()
            if tarea:
                tareas.append(tarea)
                print("Tarea agregada.")
            else:
                print("No se ingresó tarea.")
        elif opcion == "2":
            if tareas:
                print("Tareas:")
                for i, t in enumerate(tareas, 1):
                    print(f"{i}. {t}")
            else:
                print("No hay tareas.")
        elif opcion == "3":
            print("Saliendo.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()