
def unificacion(predicado1, predicado2):
    unificacion = {}  # Inicializar el diccionario de unificación

    # Verificar si los predicados tienen la misma longitud
    if len(predicado1) != len(predicado2):
        return None  # Retornar None si los predicados no tienen la misma longitud

    # Realizar la unificación de cada elemento de los predicados
    for i in range(len(predicado1)):
        # Si el elemento de predicado1 es una variable y el de predicado2 es una constante
        if predicado1[i].islower() and predicado2[i].isupper():
            unificacion[predicado1[i]] = predicado2[i]  # Unificar la variable con la constante
        # Si el elemento de predicado2 es una variable y el de predicado1 es una constante
        elif predicado2[i].islower() and predicado1[i].isupper():
            unificacion[predicado2[i]] = predicado1[i]  # Unificar la variable con la constante
        # Si ambos elementos son iguales
        elif predicado1[i] != predicado2[i]:
            return None  # Retornar None si los elementos son diferentes

    return unificacion  # Retornar el diccionario de unificación si se completó con éxito

# Función principal
def main():
    # Predicados de ejemplo
    predicado1 = ['P', 'x', 'y', 'z']
    predicado2 = ['P', 'a', 'b', 'c']

    # Realizar la unificación
    resultado_unificacion = unificacion(predicado1, predicado2)

    # Mostrar el resultado de la unificación
    if resultado_unificacion is not None:
        print("Unificación exitosa:")
        print(resultado_unificacion)
    else:
        print("No se puede unificar los predicados.")

if __name__ == "__main__":
    main()

