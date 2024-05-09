
# Definir una función para verificar si un ave es un pingüino
def es_pinguino(ave):
    # Lista de características comunes de los pingüinos
    caracteristicas_comunes = ["nadar", "plumas", "pico corto"]

    # Si todas las características comunes están presentes en el ave, entonces es un pingüino
    if all(caracteristica in ave for caracteristica in caracteristicas_comunes):
        return True
    else:
        return False

# Definir una función para verificar si un ave es un águila
def es_aguila(ave):
    # Lista de características comunes de las águilas
    caracteristicas_comunes = ["volar", "garras", "pico afilado"]

    # Si todas las características comunes están presentes en el ave, entonces es un águila
    if all(caracteristica in ave for caracteristica in caracteristicas_comunes):
        return True
    else:
        return False

# Definir una función para identificar el ave desconocida
def identificar_ave(ave):
    if es_pinguino(ave):  # Verificar si el ave tiene características de pingüino
        return "El ave es un pingüino."
    elif es_aguila(ave):  # Verificar si el ave tiene características de águila
        return "El ave es un águila."
    else:
        return "No se puede identificar el tipo de ave."

# Función principal
def main():
    # Ejemplos de aves para identificar
    ave1 = ["nadar", "plumas", "pico corto"]  # Pingüino
    ave2 = ["volar", "garras", "pico afilado"]  # Águila
    ave3 = ["nadar", "garras"]  # Ave desconocida

    # Identificar las aves
    print(identificar_ave(ave1))
    print(identificar_ave(ave2))
    print(identificar_ave(ave3))

if __name__ == "__main__":
    main()
