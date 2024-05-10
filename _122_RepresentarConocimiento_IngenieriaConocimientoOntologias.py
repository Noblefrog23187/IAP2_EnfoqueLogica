class Conocimiento:
    def __init__(self):
        self.Enciclopedia = {}  # Inicializar el diccionario para almacenar el conocimiento

    # Se agregan relaciones entre los datos
    def Anexar(self, Cosa, Relacion, Valor):
        if Cosa not in self.Enciclopedia:
            self.Enciclopedia[Cosa] = {}  # Inicializar un diccionario para la definición si no existe
        self.Enciclopedia[Cosa][Relacion] = Valor  # Agregar la relación y su valor al diccionario de la definicion

    # Método para consultar relaciones en la ontología
    def Consulta(self, Cosa, Relacion):
        if Cosa in self.Enciclopedia and Relacion in self.Enciclopedia[Cosa]:
            return self.Enciclopedia[Cosa][Relacion]  # Devolver el valor de la relación si existe
        else:
            return "No se encontro la relacion"  # Devolver un mensaje si la relacion no existe

def main():
    conocimiento = Conocimiento()   

    # Agregar relaciones a la base
    conocimiento.Anexar("Barco", "es_un", "Vehiculo")
    conocimiento.Anexar("Barco", "tiene", "Casco")
    conocimiento.Anexar("Auto", "es_un", "Vehiculo")
    conocimiento.Anexar("Auto", "es_un", "Vehiculo")
    conocimiento.Anexar("Vehiculo", "transporta", "Cosas")

    # Consultar relaciones en la base
    print("Un barco es un: ", conocimiento.Consulta("Barco", "es_un")) 
    print("Un barco tiene: ", conocimiento.Consulta("Barco", "tiene")) 
    print("Un auto es un: ", conocimiento.Consulta("Auto", "es_un"))
    print("Un avion es un: ", conocimiento.Consulta("Avion", "es_un"))   

if __name__ == "__main__":
    main()

