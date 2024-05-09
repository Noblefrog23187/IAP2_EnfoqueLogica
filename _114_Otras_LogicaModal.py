

# Definir una clase para los mundos posibles
class MundoPosible:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del mundo posible
        self.proposiciones = set()  # Conjunto de proposiciones verdaderas en este mundo posible

    def agregar_proposicion(self, proposicion):
        self.proposiciones.add(proposicion)  # Agregar una proposición a este mundo posible

    def __str__(self):
        return self.nombre  # Devuelve el nombre del mundo posible como una cadena

# Función para verificar si una proposición es verdadera en un mundo posible
def es_verdadera(mundo, proposicion):
    return proposicion in mundo.proposiciones  # Verifica si la proposición está en el conjunto de proposiciones verdaderas del mundo

# Función principal
def main():
    # Crear mundos posibles
    mundo1 = MundoPosible("Mundo 1")  # Crear el primer mundo posible
    mundo1.agregar_proposicion("p")  # Agregar la proposición "p" al primer mundo
    mundo1.agregar_proposicion("q")  # Agregar la proposición "q" al primer mundo

    mundo2 = MundoPosible("Mundo 2")  # Crear el segundo mundo posible
    mundo2.agregar_proposicion("q")  # Agregar la proposición "q" al segundo mundo

    # Verificar proposiciones en diferentes mundos
    print("p es verdadera en Mundo 1:", es_verdadera(mundo1, "p"))  # Verificar si "p" es verdadera en el Mundo 1
    print("q es verdadera en Mundo 1:", es_verdadera(mundo1, "q"))  # Verificar si "q" es verdadera en el Mundo 1
    print("p es verdadera en Mundo 2:", es_verdadera(mundo2, "p"))  # Verificar si "p" es verdadera en el Mundo 2
    print("q es verdadera en Mundo 2:", es_verdadera(mundo2, "q"))  # Verificar si "q" es verdadera en el Mundo 2

if __name__ == "__main__":
    main()  # Llamar a la función principal si el script se ejecuta directamente