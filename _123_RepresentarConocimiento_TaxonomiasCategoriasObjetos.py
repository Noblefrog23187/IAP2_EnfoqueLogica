taxonomia = {
    "Animales": ["Perro", "Gato", "Elefante"],
    "Frutas": ["Manzana", "Banana", "Naranja"],
    "Colores": ["Rojo", "Verde", "Azul"]
}

# Función para imprimir la taxonomía
def imprimir_taxonomia(taxonomia):
    for categoria, objetos in taxonomia.items():  # Iterar sobre las claves y valores del diccionario
        print(categoria + ":")  # Imprimir el nombre de la categoría
        for objeto in objetos:  # Iterar sobre los objetos dentro de la categoría
            print("- " + objeto)  # Imprimir cada objeto con un guion al inicio

# Función principal
def main():
    print("Taxonomía:")  # Imprimir encabezado
    imprimir_taxonomia(taxonomia)  # Llamar a la función para imprimir la taxonomía

if __name__ == "__main__":
    main()


