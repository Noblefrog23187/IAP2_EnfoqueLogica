import random  # Importa la biblioteca random para generar números aleatorios

# Definición de la clase del modelo probabilista racional
class ModeloProbabilistaRacional:
    def __init__(self, opciones):
        self.opciones = opciones  # Inicializa las opciones disponibles
        self.probabilidades = {opcion: 1 / len(opciones) for opcion in opciones}  # Inicializa las probabilidades uniformemente

    # Método para actualizar las probabilidades basadas en la evidencia
    def actualizar_probabilidades(self, evidencia):
        total = sum(self.probabilidades[opcion] for opcion in self.opciones)  # Calcula la suma total de las probabilidades
        for opcion in self.opciones:
            if opcion == evidencia:
                self.probabilidades[opcion] /= total  # Actualiza la probabilidad de la opción con la evidencia
            else:
                self.probabilidades[opcion] = 0  # Establece la probabilidad de las otras opciones a cero

    # Método para tomar una decisión basada en las probabilidades actuales
    def tomar_decision(self):
        return random.choices(self.opciones, weights=self.probabilidades.values())[0]  # Elige una opción basada en las probabilidades actuales

# Función principal
def main():
    opciones = ["A", "B", "C"]  # Definir las opciones disponibles
    modelo = ModeloProbabilistaRacional(opciones)  # Crear una instancia del modelo probabilista racional

    # Actualizar las probabilidades basadas en una evidencia y tomar una decisión
    evidencia = "A"
    modelo.actualizar_probabilidades(evidencia)
    decision = modelo.tomar_decision()
    print("Decisión tomada:", decision)

if __name__ == "__main__":
    main()

