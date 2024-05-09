# Función para generar patrones de texto utilizando inducción gramatical
def generar_patron(indice):
    if indice == 0:  # Caso base: índice 0
        return "A"
    else:
        return generar_patron(indice - 1) + "B" + generar_patron(indice - 1)  # Regla de inducción

# Función principal
def main():
    indice = int(input("Ingrese el índice para generar el patrón de texto: "))  # Solicitar al usuario que ingrese un índice
    patron = generar_patron(indice)  # Llamar a la función para generar el patrón de texto
    print("El patrón de texto generado para el índice", indice, "es:", patron)  # Imprimir el patrón generado

if __name__ == "__main__":
    main()

