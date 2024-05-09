
class Accion:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre  # Nombre de la acción
        self.descripcion = descripcion  # Descripción de la acción

    def __str__(self):
        return f"Accion: {self.nombre}, Descripcion: {self.descripcion}"


# Definir un marco para una situación
class Situacion:
    def __init__(self, lugar, hora, clima):
        self.lugar = lugar  # Lugar de la situación
        self.hora = hora  # Hora de la situación
        self.clima = clima  # Clima de la situación

    def __str__(self):
        return f"Situacion: Lugar={self.lugar}, Hora={self.hora}, Clima={self.clima}"


# Definir un marco para un evento
class Evento:
    def __init__(self, accion, situacion):
        self.accion = accion  # Acción relacionada con el evento
        self.situacion = situacion  # Situación en la que ocurre el evento

    def __str__(self):
        return f"Evento: {self.accion}, {self.situacion}"


# Función principal
def main():
    # Crear instancias de acciones
    accion1 = Accion("Jugar al fútbol", "Divertirse con amigos en el campo")
    accion2 = Accion("Estudiar", "Prepararse para un examen importante")

    # Crear instancias de situaciones
    situacion1 = Situacion("Parque", "Tarde", "Soleado")
    situacion2 = Situacion("Biblioteca", "Mañana", "Nublado")

    # Crear instancias de eventos
    evento1 = Evento(accion1, situacion1)
    evento2 = Evento(accion2, situacion2)

    # Imprimir los eventos creados
    print(evento1)
    print(evento2)


if __name__ == "__main__":
    main()

