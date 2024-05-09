# Definir una función de orden superior que aplica una función dada a cada elemento de una lista
def aplicar_funcion_a_lista(funcion, lista):
    # Inicializar una lista vacía para almacenar los resultados
    resultados = []
    # Iterar sobre cada elemento de la lista
    for elemento in lista:
        # Aplicar la función dada al elemento y agregar el resultado a la lista de resultados
        resultados.append(funcion(elemento))
    # Devolver la lista de resultados
    return resultados

# Función de ejemplo que eleva al cuadrado un número
def cuadrado(x):
    return x ** 2

# Función de ejemplo que duplica un número
def duplicar(x):
    return x * 2

# Función principal
def main():
    # Lista de números de ejemplo
    numeros = [1, 2, 3, 4, 5]

    # Aplicar la función cuadrado a la lista de números
    resultado_cuadrado = aplicar_funcion_a_lista(cuadrado, numeros)
    print("Aplicar cuadrado a la lista:", resultado_cuadrado)

    # Aplicar la función duplicar a la lista de números
    resultado_duplicar = aplicar_funcion_a_lista(duplicar, numeros)
    print("Aplicar duplicar a la lista:", resultado_duplicar)

if __name__ == "__main__":
    main()

