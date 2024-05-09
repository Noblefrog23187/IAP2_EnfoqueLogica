# Definir la función de planificación para un agente
def planificacion_agente(agente, tarea):
    # Simulación de la planificación del agente para la tarea
    print(f"El agente {agente} está planificando la tarea: {tarea}")

# Función principal
def main():
    # Lista de agentes y tareas
    agentes = ["Agente1", "Agente2", "Agente3"]
    tareas = ["Tarea1", "Tarea2", "Tarea3"]

    # Planificación para cada agente y tarea
    for agente in agentes:
        for tarea in tareas:
            planificacion_agente(agente, tarea)  # Llama a la función de planificación para cada combinación de agente y tarea

if __name__ == "__main__":
    main()

