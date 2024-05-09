# Funci�n para generar patrones de texto utilizando inducci�n gramatical
def generar_patron(indice):
    if indice == 0:  # Caso base: �ndice 0
        return "A"
    else:
        return generar_patron(indice - 1) + "B" + generar_patron(indice - 1)  # Regla de inducci�n

# Funci�n principal
def main():
    indice = int(input("Ingrese el �ndice para generar el patr�n de texto: "))  # Solicitar al usuario que ingrese un �ndice
    patron = generar_patron(indice)  # Llamar a la funci�n para generar el patr�n de texto
    print("El patr�n de texto generado para el �ndice", indice, "es:", patron)  # Imprimir el patr�n generado

if __name__ == "__main__":
    main()

