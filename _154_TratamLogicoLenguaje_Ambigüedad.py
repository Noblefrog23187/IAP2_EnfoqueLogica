# Definición de la función para evaluar una expresión aritmética
def evaluar_expresion(expresion):
    # Expresión aritmética ambigua: 2 + 3 * 4
    resultado1 = 2 + 3 * 4  # Primero se multiplica y luego se suma: 2 + (3 * 4) = 14

    # Expresión aritmética ambigua: (2 + 3) * 4
    resultado2 = (2 + 3) * 4  # Primero se suma y luego se multiplica: (2 + 3) * 4 = 20

    if expresion == "2 + 3 * 4":
        return resultado1
    elif expresion == "(2 + 3) * 4":
        return resultado2
    else:
        return "Expresión no válida"

# Función principal
def main():
    print("Evaluación de expresiones aritméticas ambiguas:")
    print("Expresión 1: 2 + 3 * 4 = ", evaluar_expresion("2 + 3 * 4"))
    print("Expresión 2: (2 + 3) * 4 = ", evaluar_expresion("(2 + 3) * 4"))

if __name__ == "__main__":
    main()

