from pysat.solvers import Minisat22 # Importar el solucionador Minisat22 desde la biblioteca PySAT

# Función para resolver un problema de SAT utilizando SATPLAN
def satplan(problem):
    solver = Minisat22() # Crear una instancia del solucionador Minisat22
    for clause in problem:
        solver.add_clause(clause) # Agregar cláusulas al solucionador

    # Buscar una solución al problema SAT
    if solver.solve():
        solution = solver.get_model() # Obtener el modelo de la solución
        return solution
    else:
        return "No hay solución" # Devolver un mensaje si no se encuentra una solución

# Función principal
def main():
    # Definir el problema de SAT como una lista de cláusulas
    problem = [[1, 2, -3], [-1, 2], [2, 3]]

    # Resolver el problema utilizando SATPLAN
    solution = satplan(problem)

    # Imprimir la solución encontrada
    if solution != "No hay solución":
        print("Solución encontrada:", solution)
    else:
        print("No se encontró una solución para el problema SAT.")

if __name__ == "__main__":
    main()


