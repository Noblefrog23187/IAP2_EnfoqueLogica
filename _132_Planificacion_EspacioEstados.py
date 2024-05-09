 Acciones disponibles para el agente
acciones = ['ir_a_clase', 'estudiar', 'tomar_un_descanso', 'salir_con_amigos']

# Definición del espacio de estados como un diccionario
espacio_estados = {
    'clase': ['estudiar', 'tomar_un_descanso'],
    'casa': ['ir_a_clase', 'estudiar', 'tomar_un_descanso'],
    'biblioteca': ['estudiar', 'tomar_un_descanso'],
    'cafeteria': ['salir_con_amigos']
}

# Función para imprimir el espacio de estados
def imprimir_espacio_estados():
    print("Espacio de Estados:")
    for lugar, acciones_posibles in espacio_estados.items():
        print(f"- En {lugar}, puedes hacer: {', '.join(acciones_posibles)}")

# Función principal
def main():
    imprimir_espacio_estados()  # Imprime el espacio de estados inicial

if __name__ == "__main__":
    main()


