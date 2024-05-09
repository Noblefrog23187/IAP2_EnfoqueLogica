# Programa para realizar an�lisis l�xico b�sico

# Definir tokens
PALABRAS_CLAVE = ['if', 'else', 'while', 'for']
OPERADORES = ['+', '-', '*', '/']
DELIMITADORES = ['(', ')', '{', '}', ';']

# Funci�n para realizar an�lisis l�xico
def analisis_lexico(codigo):
    tokens = []  # Lista para almacenar los tokens encontrados
    palabra_actual = ''  # Variable para construir una palabra
    for caracter in codigo:  # Iterar sobre cada caracter del c�digo
        if caracter.isspace():  # Si es un espacio, verificar si se complet� una palabra
            if palabra_actual:  # Si hay una palabra actual
                tokens.append(palabra_actual)  # Agregar la palabra a la lista de tokens
                palabra_actual = ''  # Reiniciar la palabra actual
        elif caracter in DELIMITADORES or caracter in OPERADORES:  # Si es un delimitador u operador
            if palabra_actual:  # Si hay una palabra actual
                tokens.append(palabra_actual)  # Agregar la palabra a la lista de tokens
                palabra_actual = ''  # Reiniciar la palabra actual
            tokens.append(caracter)  # Agregar el delimitador u operador como token
        else:  # Si es un caracter alfanum�rico
            palabra_actual += caracter  # Construir la palabra actual
    if palabra_actual:  # Verificar si hay una palabra pendiente al final del c�digo
        tokens.append(palabra_actual)  # Agregar la palabra a la lista de tokens
    return tokens  # Devolver la lista de tokens

# Funci�n principal
def main():
    codigo = input("Ingrese el c�digo a analizar: ")  # Solicitar al usuario que ingrese el c�digo
    tokens = analisis_lexico(codigo)  # Realizar el an�lisis l�xico del c�digo
    print("Tokens encontrados:", tokens)  # Imprimir los tokens encontrados

if __name__ == "__main__":
    main()

