# Definir la base de conocimiento como una lista de reglas
base_conocimiento = [
    {"regla": "padre(juan, maria)", "hecho": ""},  # Regla: Juan es padre de Maria
    {"regla": "padre(pedro, juan)", "hecho": ""},  # Regla: Pedro es padre de Juan
    {"regla": "abuelo(X, Y) :- padre(X, Z), padre(Z, Y)", "hecho": ""}  # Regla: X es abuelo de Y si X es padre de Z y Z es padre de Y
]

# Función para verificar si una regla se cumple
def verificar_regla(regla):
    if regla["regla"]:  # Verifica si la regla existe
        print("Se cumple la regla:", regla["regla"])  # Imprime la regla que se está evaluando
        if regla["hecho"]:  # Verifica si hay un hecho asociado a la regla
            print("Se infiere el hecho:", regla["hecho"])  # Imprime el hecho inferido
            return regla["hecho"]  # Devuelve el hecho inferido
        else:
            print("La regla no produce ningún hecho.")  # Imprime un mensaje si la regla no produce un hecho
            return None  # Devuelve None si no hay hecho inferido
    else:
        print("No se cumple la regla.")  # Imprime un mensaje si la regla no se cumple
        return None  # Devuelve None si no se cumple la regla

# Función principal
def main():
    # Consultar cada regla en la base de conocimiento
    for regla in base_conocimiento:
        verificar_regla(regla)  # Llama a la función verificar_regla() para cada regla en la base de conocimiento

if __name__ == "__main__":
    main()  # Llama a la función principal si el script es ejecutado directamente

