# Definir la clase para representar una regla
class Regla:
    def __init__(self, antecedente, consecuente):
        self.antecedente = antecedente  # Define el antecedente de la regla
        self.consecuente = consecuente  # Define el consecuente de la regla

# Definir la función para aplicar una regla
def aplicar_regla(regla, hechos):
    if all(fact in hechos for fact in regla.antecedente):
        hechos.extend(regla.consecuente)  # Agrega el consecuente al conjunto de hechos si el antecedente se cumple

# Función principal
def main():
    # Definir las reglas y los hechos iniciales
    reglas = [
        Regla(["gato"], ["animal"]),
        Regla(["perro"], ["animal"]),
        Regla(["animal"], ["ser vivo"])
    ]
    hechos = ["gato", "perro"]  # Hechos iniciales: hay un gato y un perro

    # Aplicar las reglas a los hechos
    for regla in reglas:
        aplicar_regla(regla, hechos)

    # Mostrar los hechos resultantes
    print("Hechos después de aplicar las reglas:", hechos)

if __name__ == "__main__":
    main()

