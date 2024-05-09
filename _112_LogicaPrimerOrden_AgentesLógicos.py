
# Definir la función para el agente lógico
def agente_logico(persona, lugar, hora):
    # Reglas lógicas para determinar la acción del agente
    if persona == "Juan" and lugar == "parque" and hora == "tarde":
        return "Jugar al fútbol"  # Si Juan está en el parque por la tarde, juega al fútbol
    elif persona == "María" and lugar == "casa" and hora == "noche":
        return "Ver una película"  # Si María está en casa por la noche, ve una película
    elif persona == "Pedro" and lugar == "biblioteca" and hora == "mañana":
        return "Estudiar"  # Si Pedro está en la biblioteca por la mañana, estudia
    else:
        return "No se puede determinar la acción"  # Si no se cumplen las condiciones anteriores, no se puede determinar la acción

# Función principal
def main():
    # Ejemplos de consultas al agente lógico
    print(agente_logico("Juan", "parque", "tarde"))  # Consulta para Juan en el parque por la tarde
    print(agente_logico("María", "casa", "noche"))  # Consulta para María en casa por la noche
    print(agente_logico("Pedro", "biblioteca", "mañana"))  # Consulta para Pedro en la biblioteca por la mañana

if __name__ == "__main__":
    main()
