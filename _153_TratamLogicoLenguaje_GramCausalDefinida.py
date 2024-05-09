# Definici�n de la funci�n para validar la oraci�n
def validar_oracion(oracion):
    # Definici�n de palabras clave que indican una relaci�n causal
    palabras_clave = ["porque", "debido a", "ya que"]

    # Verificar si alguna palabra clave est� presente en la oraci�n
    for palabra in palabras_clave:
        if palabra in oracion:
            return True  # Si se encuentra una palabra clave, la oraci�n es v�lida

    return False  # Si no se encuentra ninguna palabra clave, la oraci�n no es v�lida

# Funci�n principal
def main():
    oracion = input("Ingrese una oraci�n: ")  # Solicitar al usuario que ingrese una oraci�n
    if validar_oracion(oracion):  # Llamar a la funci�n para validar la oraci�n
        print("La oraci�n sigue la estructura de una gram�tica causal definida.")  # La oraci�n sigue una estructura causal
    else:
        print("La oraci�n no sigue la estructura de una gram�tica causal definida.")  # La oraci�n no sigue una estructura causal

if __name__ == "__main__":
    main()

