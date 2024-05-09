# Definir una función para la resolución de Skolem
def resolver_skolem(formula):
    # Aplicar la transformación de Skolem
    skolemizada = formula.replace('∃x', 'Skolem(x)')  # Reemplazar cada cuantificador existencial con Skolem(x)
    return skolemizada

# Función principal
def main():
    # Ejemplo de fórmula en lógica de primer orden con cuantificador existencial
    formula = '∃x (P(x) ∧ Q(x))'

    print("Fórmula original:", formula)
    formula_skolemizada = resolver_skolem(formula)
    print("Fórmula skolemizada:", formula_skolemizada)

if __name__ == "__main__":
    main()


