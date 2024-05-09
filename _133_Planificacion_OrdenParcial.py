# Definir una función para la planificación de orden parcial
def planificacion_orden_parcial(tareas):
    plan = []  # Inicializar el plan vacío

    # Iterar sobre todas las tareas
    for tarea in tareas:
        # Verificar si todas las tareas previas de la tarea actual están en el plan
        if all(tarea_previa in plan for tarea_previa in tarea["previas"]):
            plan.append(tarea)  # Agregar la tarea al plan si todas las tareas previas están en el plan

    return plan  # Devolver el plan resultante

# Función principal
def main():
    # Definir las tareas con sus respectivas tareas previas
    tareas = [
        {"nombre": "Tarea A", "previas": []},
        {"nombre": "Tarea B", "previas": ["Tarea A"]},
        {"nombre": "Tarea C", "previas": ["Tarea A", "Tarea B"]},
        {"nombre": "Tarea D", "previas": ["Tarea C"]},
        {"nombre": "Tarea E", "previas": ["Tarea B"]},
    ]

    # Realizar la planificación de orden parcial
    plan = planificacion_orden_parcial(tareas)

    # Mostrar el plan resultante
    print("Planificación de Orden Parcial:")
    for tarea in plan:
        print(tarea["nombre"])

if __name__ == "__main__":
    main()

