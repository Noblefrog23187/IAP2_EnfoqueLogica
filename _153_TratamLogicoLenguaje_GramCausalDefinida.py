# Definición de la función para validar la oración
def validar_oracion(oracion):
    # Definición de palabras clave que indican una relación causal
    palabras_clave = ["porque", "debido a", "ya que"]

    # Verificar si alguna palabra clave está presente en la oración
    for palabra in palabras_clave:
        if palabra in oracion:
            return True  # Si se encuentra una palabra clave, la oración es válida

    return False  # Si no se encuentra ninguna palabra clave, la oración no es válida

# Función principal
def main():
    oracion = input("Ingrese una oración: ")  # Solicitar al usuario que ingrese una oración
    if validar_oracion(oracion):  # Llamar a la función para validar la oración
        print("La oración sigue la estructura de una gramática causal definida.")  # La oración sigue una estructura causal
    else:
        print("La oración no sigue la estructura de una gramática causal definida.")  # La oración no sigue una estructura causal

if __name__ == "__main__":
    main()

