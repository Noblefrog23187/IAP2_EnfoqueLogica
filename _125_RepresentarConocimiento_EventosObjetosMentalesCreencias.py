# Definir la clase para representar un evento
class Evento:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del evento

# Definir la clase para representar un objeto mental
class ObjetoMental:
    def __init__(self, nombre, creencia):
        self.nombre = nombre  # Nombre del objeto mental
        self.creencia = creencia  # Creencia asociada al objeto mental

# Función principal
def main():
    # Crear eventos
    evento1 = Evento("Fiesta")
    evento2 = Evento("Conferencia")

    # Crear objetos mentales con sus creencias asociadas
    objeto_mental1 = ObjetoMental("Juan", evento1)
    objeto_mental2 = ObjetoMental("María", evento2)

    # Mostrar las creencias de los objetos mentales
    print(objeto_mental1.nombre, "cree que habrá", objeto_mental1.creencia.nombre)
    print(objeto_mental2.nombre, "cree que habrá", objeto_mental2.creencia.nombre)

if __name__ == "__main__":
    main()


