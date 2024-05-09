
# Definición de la base de conocimiento de hechos
base_conocimiento = {
    "Padre": [("Juan", "Pedro"), ("Pedro", "Carlos"), ("Carlos", "Jorge")],
    "Hijo": [("Pedro", "Juan"), ("Carlos", "Pedro"), ("Jorge", "Carlos")],
    "Abuelo": [("Juan", "Carlos"), ("Pedro", "Jorge")]
}

# Encadenamiento hacia adelante
def encadenamiento_adelante(regla, base):
    for hecho in base[regla]:
        print(f"Se ha inferido: {regla}{hecho}")

# Encadenamiento hacia atrás
def encadenamiento_atras(meta, base):
    for regla in base.keys():
        for hecho in base[regla]:
            if hecho[1] == meta:
                print(f"Se ha inferido: {regla}{hecho[0]}")
                encadenamiento_atras(hecho[0], base)

# Programa principal
if __name__ == "__main__":
    print("Encadenamiento hacia adelante:")
    encadenamiento_adelante("Abuelo", base_conocimiento)
    
    print("\nEncadenamiento hacia atrás:")
    encadenamiento_atras("Jorge", base_conocimiento)

