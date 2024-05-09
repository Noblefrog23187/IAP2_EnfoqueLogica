# Definir una función para verificar si es mañana
def es_manana(hora):
    return hora < 12  # Devuelve True si la hora es antes del mediodía, False en caso contrario

# Definir una función para verificar si es tarde
def es_tarde(hora):
    return 12 <= hora < 18  # Devuelve True si la hora está entre el mediodía y las 6 p.m., False en caso contrario

# Función principal
def main():
    # Ejemplos de consultas para la lógica temporal
    hora_actual = 10  # Hora actual, por ejemplo, 10 a.m.
    
    if es_manana(hora_actual):
        print("Es mañana.")
    elif es_tarde(hora_actual):
        print("Es tarde.")
    else:
        print("Es noche.")

if __name__ == "__main__":
    main()


