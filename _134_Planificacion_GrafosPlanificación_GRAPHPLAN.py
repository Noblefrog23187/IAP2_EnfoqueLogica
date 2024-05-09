from collections import deque

# Definición de la clase GrafoPlanificacion
class GrafoPlanificacion:
    def __init__(self):
        self.nodos = set()  # Conjunto de nodos en el grafo
        self.arcos = {}  # Diccionario de arcos en el grafo
        self.factores = {}  # Diccionario de factores en el grafo

    # Método para agregar un nodo al grafo
    def agregar_nodo(self, nodo):
        self.nodos.add(nodo)

    # Método para agregar un arco al grafo
    def agregar_arco(self, inicio, fin):
        if inicio not in self.arcos:
            self.arcos[inicio] = []
        self.arcos[inicio].append(fin)

    # Método para agregar un factor al grafo
    def agregar_factor(self, factor):
        self.factores[factor] = set()

    # Método para conectar un nodo a un factor en el grafo
    def conectar_nodo_factor(self, nodo, factor):
        if nodo in self.nodos and factor in self.factores:
            self.factores[factor].add(nodo)
        else:
            raise ValueError("El nodo o el factor no existen en el grafo")

    # Algoritmo GRAPHPLAN
    def graphplan(self, objetivos, acciones):
        # Inicializar niveles de planificación
        niveles = [set(objetivos)]
        aplicables = [acciones]

        # Bucle principal
        while True:
            nuevos_niveles = set()
            nuevos_aplicables = []

            for nivel, aplicable in zip(niveles, aplicables):
                nuevos_niveles.add(nivel)
                nuevos_aplicables.append(aplicable)

                # Expandir cada acción en el nivel
                for accion in aplicable:
                    precondiciones_satisfechas = all(precondicion in nivel for precondicion in accion.precondiciones)
                    if precondiciones_satisfechas:
                        nuevo_nivel = nivel | set(accion.efectos)
                        nuevos_niveles.add(nuevo_nivel)
                        nuevos_aplicables.append(acciones)

            if nuevos_niveles == niveles and nuevos_aplicables == aplicables:
                return niveles, aplicables
            else:
                niveles = nuevos_niveles
                aplicables = nuevos_aplicables

# Definición de la clase Accion
class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre
        self.precondiciones = precondiciones
        self.efectos = efectos

# Definición de la función principal
def main():
    # Crear un grafo de planificación
    grafo = GrafoPlanificacion()

    # Definir nodos
    objetivos = {"A", "B"}
    acciones = {Accion("accion1", {"A"}, {"B"}), Accion("accion2", {"B"}, {"A"})}

    # Agregar nodos al grafo
    for objetivo in objetivos:
        grafo.agregar_nodo(objetivo)

    # Agregar acciones al grafo
    for accion in acciones:
        grafo.agregar_nodo(accion.nombre)

    # Conectar nodos y factores
    for accion in acciones:
        for precondicion in accion.precondiciones:
            grafo.conectar_nodo_factor(accion.nombre, precondicion)
        for efecto in accion.efectos:
            grafo.conectar_nodo_factor(efecto, accion.nombre)

    # Ejecutar algoritmo GRAPHPLAN
    niveles, aplicables = grafo.graphplan(objetivos, acciones)

    # Mostrar resultado
    print("Niveles de planificación:")
    for i, nivel in enumerate(niveles):
        print(f"Nivel {i}: {nivel}")
    print("Acciones aplicables:")
    for i, aplicable in enumerate(aplicables):
        print(f"Nivel {i}: {aplicable}")

if __name__ == "__main__":
    main()

