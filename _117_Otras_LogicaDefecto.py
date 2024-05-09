# Base de conocimiento inicial
base_conocimiento = {
    "puede_volar": ["pájaro", "avión"],
    "puede_nadar": ["pez", "ballena"],
    "es_mamifero": ["ballena", "perro"]
}

# Función para verificar si un hecho está en la base de conocimiento
def verificar_hecho(hecho, base_conocimiento):
    for atributo, valores in base_conocimiento.items():
        if hecho in valores:
            return True
    return False

# Función para inferir nuevos hechos basados en la lógica por defecto
def inferir_hechos(hecho):
    if verificar_hecho(hecho, base_conocimiento):
        print(f"¡Claro que {hecho} es cierto!")
    else:
        print(f"No estoy seguro si {hecho} es cierto.")

# Consultas
inferir_hechos("pájaro")
inferir_hechos("pez")
inferir_hechos("perro")
inferir_hechos("avión")
inferir_hechos("serpiente")

