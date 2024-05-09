
# Definir la base de conocimientos con reglas
base_conocimientos = {
    "experiencia": {
        "Juan": 5,
        "María": 3,
        "Pedro": 2
    },
    "educacion": {
        "Juan": "Licenciatura",
        "María": "Maestría",
        "Pedro": "Bachillerato"
    },
    "edad": {
        "Juan": 30,
        "María": 35,
        "Pedro": 25
    }
}

# Función para evaluar si alguien está calificado para el trabajo
def sistema_experto(nombre):
    experiencia = base_conocimientos["experiencia"][nombre]
    educacion = base_conocimientos["educacion"][nombre]
    edad = base_conocimientos["edad"][nombre]

    if experiencia >= 3 and educacion in ["Licenciatura", "Maestría"] and edad >= 25:
        return f"{nombre} está calificado para el trabajo."
    else:
        return f"{nombre} no está calificado para el trabajo."

# Función principal
def main():
    # Ejemplos de consultas al sistema experto
    print(sistema_experto("Juan"))  # Consulta para Juan
    print(sistema_experto("María"))  # Consulta para María
    print(sistema_experto("Pedro"))  # Consulta para Pedro

if __name__ == "__main__":
    main()
