# Definir la clase para las tareas
class Tarea:
    def __init__(self, nombre, duracion):
        self.nombre = nombre  # Nombre de la tarea
        self.duracion = duracion  # Duración estimada de la tarea
        self.subtareas = []  # Lista para almacenar las subtareas

    # Método para agregar subtareas a la tarea actual
    def agregar_subtarea(self, subtarea):
        self.subtareas.append(subtarea)  # Agregar una subtarea a la lista

    # Método para calcular la duración total de la tarea considerando las subtareas
    def calcular_duracion_total(self):
        duracion_total = self.duracion  # Inicializar la duración total con la duración de la tarea actual
        for subtarea in self.subtareas:
            duracion_total += subtarea.calcular_duracion_total()  # Sumar la duración total de las subtareas recursivamente
        return duracion_total

# Función principal
def main():
    # Crear las tareas principales
    tarea_principal_1 = Tarea("Tarea Principal 1", 5)
    tarea_principal_2 = Tarea("Tarea Principal 2", 8)

    # Crear las subtareas y agregarlas a las tareas principales
    subtarea_1_1 = Tarea("Subtarea 1.1", 2)
    subtarea_1_2 = Tarea("Subtarea 1.2", 3)
    subtarea_2_1 = Tarea("Subtarea 2.1", 4)
    subtarea_2_2 = Tarea("Subtarea 2.2", 5)

    tarea_principal_1.agregar_subtarea(subtarea_1_1)
    tarea_principal_1.agregar_subtarea(subtarea_1_2)
    tarea_principal_2.agregar_subtarea(subtarea_2_1)
    tarea_principal_2.agregar_subtarea(subtarea_2_2)

    # Calcular la duración total de cada tarea principal
    duracion_total_tarea_1 = tarea_principal_1.calcular_duracion_total()
    duracion_total_tarea_2 = tarea_principal_2.calcular_duracion_total()

    # Mostrar la duración total de cada tarea principal
    print("Duración total de", tarea_principal_1.nombre, ":", duracion_total_tarea_1, "horas")
    print("Duración total de", tarea_principal_2.nombre, ":", duracion_total_tarea_2, "horas")

if __name__ == "__main__":
    main()

