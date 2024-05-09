
# Función para simular la ejecución de una tarea
def ejecutar_tarea(tarea):
    print("Ejecutando la tarea:", tarea)

# Función para simular la vigilancia de ejecución y replanificación
def vigilancia_replanificacion():
    while True:
        tarea_actual = input("Ingrese la tarea actual: ")  # Solicitar al usuario la tarea actual
        if tarea_actual == "terminar":
            print("Programa finalizado.")
            break  # Salir del bucle si se ingresa "terminar"
        
        # Simular la ejecución de la tarea actual
        ejecutar_tarea(tarea_actual)
        
        # Verificar si hay algún problema durante la ejecución
        problema = input("Hubo algún problema durante la ejecución (s/n)? ")
        if problema.lower() == "s":
            print("Replanificando...")
            # Simular la replanificación
            nueva_tarea = input("Ingrese la nueva tarea: ")
            print("Replanificación completada. Ejecutando la nueva tarea:", nueva_tarea)
        else:
            print("La ejecución de la tarea fue exitosa.")

# Función principal
def main():
    print("Bienvenido a la vigilancia de ejecución y replanificación.")
    vigilancia_replanificacion()  # Llamar a la función de vigilancia de ejecución y replanificación

if __name__ == "__main__":
    main()

