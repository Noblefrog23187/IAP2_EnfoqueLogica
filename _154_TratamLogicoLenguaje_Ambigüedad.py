# Definici�n de la funci�n para evaluar una expresi�n aritm�tica
def evaluar_expresion(expresion):
    # Expresi�n aritm�tica ambigua: 2 + 3 * 4
    resultado1 = 2 + 3 * 4  # Primero se multiplica y luego se suma: 2 + (3 * 4) = 14

    # Expresi�n aritm�tica ambigua: (2 + 3) * 4
    resultado2 = (2 + 3) * 4  # Primero se suma y luego se multiplica: (2 + 3) * 4 = 20

    if expresion == "2 + 3 * 4":
        return resultado1
    elif expresion == "(2 + 3) * 4":
        return resultado2
    else:
        return "Expresi�n no v�lida"

# Funci�n principal
def main():
    print("Evaluaci�n de expresiones aritm�ticas ambiguas:")
    print("Expresi�n 1: 2 + 3 * 4 = ", evaluar_expresion("2 + 3 * 4"))
    print("Expresi�n 2: (2 + 3) * 4 = ", evaluar_expresion("(2 + 3) * 4"))

if __name__ == "__main__":
    main()

