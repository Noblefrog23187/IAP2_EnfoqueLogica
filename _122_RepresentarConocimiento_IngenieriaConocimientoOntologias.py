class Ontologia:
    def __init__(self):
        self.conocimiento = {}  # Inicializar el diccionario para almacenar el conocimiento

    # Método para agregar relaciones a la ontología
    def agregar_relacion(self, concepto, relacion, valor):
        if concepto not in self.conocimiento:
            self.conocimiento[concepto] = {}  # Inicializar un diccionario para el concepto si no existe
        self.conocimiento[concepto][relacion] = valor  # Agregar la relación y su valor al diccionario del concepto

    # Método para consultar relaciones en la ontología
    def consultar_relacion(self, concepto, relacion):
        if concepto in self.conocimiento and relacion in self.conocimiento[concepto]:
            return self.conocimiento[concepto][relacion]  # Devolver el valor de la relación si existe
        else:
            return "No se encontró la relación"  # Devolver un mensaje si la relación no existe

# Función principal
def main():
    ontologia = Ontologia()  # Crear una instancia de la ontología

    # Agregar relaciones a la ontología
    ontologia.agregar_relacion("Perro", "es_un", "Animal")
    ontologia.agregar_relacion("Gato", "es_un", "Animal")
    ontologia.agregar_relacion("Animal", "tiene", "Patas")
    ontologia.agregar_relacion("Perro", "tiene", "Cola")

    # Consultar relaciones en la ontología
    print(ontologia.consultar_relacion("Perro", "es_un"))  # Consulta si "Perro" es un "Animal"
    print(ontologia.consultar_relacion("Gato", "tiene"))   # Consulta si "Gato" tiene algo
    print(ontologia.consultar_relacion("Ave", "es_un"))    # Consulta si "Ave" es un "Animal" (no está en la ontología)

if __name__ == "__main__":
    main()


