# Programa para generar una tabla de verdad de una expresion logica
# Funcion para evaluar una expresion logica dada una lista de valores de verdad para las variables
def evaluar_expresion(expresion, valores):
    resultado = eval(expresion, valores)  # Evalua la expresion logica con los valores dados
    return int(resultado)  # Convierte el resultado booleano a un entero (0 o 1)

# Funcion para generar todas las combinaciones posibles de valores de verdad para las variables
def generar_combinaciones(variables):
    n = len(variables)  # Obten el numero de variables
    combinaciones = []  # Inicializa la lista de combinaciones

    # Itera sobre todas las combinaciones binarias posibles de n variables
    for i in range(2 ** n):
        combinacion = {}  # Inicializa un diccionario para almacenar los valores de verdad de las variables
        for j in range(n):
            combinacion[variables[j]] = (i >> j) & 1  # Asigna los valores de verdad a las variables
        combinaciones.append(combinacion)  # Agrega la combinacion a la lista de combinaciones

    return combinaciones

# Funcion para mostrar la tabla de verdad
def mostrar_tabla_verdad(expresion, variables):
    # Genera todas las combinaciones posibles de valores de verdad para las variables
    combinaciones = generar_combinaciones(variables)

    # Imprime el encabezado de la tabla
    encabezado = " | ".join(variables + [expresion])
    print(encabezado)
    print("-" * len(encabezado))

    # Itera sobre cada combinacion de valores de verdad y evalua la expresion
    for combinacion in combinaciones:
        valores = combinacion.copy()  # Crea una copia de la combinacion actual
        resultado = evaluar_expresion(expresion, valores)  # Evalua la expresion con los valores actuales
        valores_str = " | ".join(str(valores[variable]) for variable in variables)  # Convierte los valores a cadena
        print(valores_str + " | " + str(resultado))  # Imprime la fila de la tabla

# Funcion principal
def main():
    expresion = input("Ingrese una expresion logica (utilice 'and', 'or', 'not', '(', ')', y variables): ")
    variables = list(set(caracter for caracter in expresion if caracter.isalpha()))  # Extrae las variables de la expresion
    mostrar_tabla_verdad(expresion, variables)  # Muestra la tabla de verdad para la expresion dada

if __name__ == "__main__":
    main()

