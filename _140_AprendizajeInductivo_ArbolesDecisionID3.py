from collections import Counter

# Definir la función para calcular la entropía
def calcular_entropia(datos):
    total = len(datos)  # Número total de muestras
    contador_clases = Counter(datos)  # Contar la cantidad de cada clase
    entropia = 0  # Inicializar la entropía

    # Calcular la entropía
    for clase, count in contador_clases.items():
        probabilidad = count / total  # Probabilidad de la clase
        entropia -= probabilidad * (probabilidad and log(probabilidad, 2))  # Calcular la contribución a la entropía

    return entropia

# Definir la función para dividir los datos en grupos basados en un atributo
def dividir_datos(datos, atributo):
    grupos = {}  # Inicializar el diccionario de grupos

    # Agrupar los datos según el valor del atributo
    for muestra in datos:
        valor_atributo = muestra[atributo]  # Obtener el valor del atributo para la muestra
        if valor_atributo not in grupos:
            grupos[valor_atributo] = []  # Inicializar la lista de muestras para ese valor de atributo
        grupos[valor_atributo].append(muestra)  # Agregar la muestra al grupo correspondiente

    return grupos

# Definir la función para seleccionar el mejor atributo para dividir los datos
def seleccionar_mejor_atributo(datos, atributos):
    mejor_atributo = None  # Inicializar el mejor atributo
    mejor_ganancia_informacion = float('-inf')  # Inicializar la mejor ganancia de información

    entropia_inicial = calcular_entropia(datos)  # Calcular la entropía inicial

    # Calcular la ganancia de información para cada atributo
    for atributo in atributos:
        grupos = dividir_datos(datos, atributo)  # Dividir los datos según el atributo
        ganancia_informacion = entropia_inicial  # Inicializar la ganancia de información para este atributo

        # Calcular la entropía después de dividir los datos
        for grupo in grupos.values():
            ganancia_informacion -= len(grupo) / len(datos) * calcular_entropia([muestra[-1] for muestra in grupo])

        # Actualizar el mejor atributo si se encuentra una ganancia de información mayor
        if ganancia_informacion > mejor_ganancia_informacion:
            mejor_ganancia_informacion = ganancia_informacion
            mejor_atributo = atributo

    return mejor_atributo

# Definir la función para construir el árbol de decisión
def construir_arbol_decision(datos, atributos):
    valores_clase = [muestra[-1] for muestra in datos]  # Obtener los valores de clase de las muestras

    # Caso base: si todos los ejemplos tienen la misma clase, devolver ese valor de clase
    if len(set(valores_clase)) == 1:
        return valores_clase[0]

    # Caso base: si no hay atributos restantes para dividir, devolver la clase mayoritaria
    if len(atributos) == 0:
        clase_mayoritaria = max(set(valores_clase), key=valores_clase.count)
        return clase_mayoritaria

    mejor_atributo = seleccionar_mejor_atributo(datos, atributos)  # Seleccionar el mejor atributo para dividir los datos
    grupos = dividir_datos(datos, mejor_atributo)  # Dividir los datos según el mejor atributo
    sub_arbol = {mejor_atributo: {}}  # Inicializar el sub-árbol con el mejor atributo como nodo

    # Eliminar el mejor atributo de la lista de atributos restantes
    atributos_restantes = [atributo for atributo in atributos if atributo != mejor_atributo]

    # Construir recursivamente el sub-árbol para cada valor del mejor atributo
    for valor_atributo, datos_grupo in grupos.items():
        sub_arbol[mejor_atributo][valor_atributo] = construir_arbol_decision(datos_grupo, atributos_restantes)

    return sub_arbol

# Función principal
def main():
    # Ejemplo de datos y atributos
    datos = [
        {'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'},
        {'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Strong', 'PlayTennis': 'No'},
        {'Outlook': 'Overcast', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
        {'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
        {'Outlook': 'Rain', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
        {'Outlook': 'Rain', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Strong', 'PlayTennis': 'No'},
        {'Outlook': 'Overcast', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Strong', 'PlayTennis': 'Yes'},
        {'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'},
        {'Outlook': 'Sunny', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
        {'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
        {'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Wind': 'Strong', 'PlayTennis': 'Yes'},
        {'Outlook': 'Overcast', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Strong', 'PlayTennis': 'Yes'},
        {'Outlook': 'Overcast', 'Temperature': 'Hot', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'},
        {'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Strong', 'PlayTennis': 'No'},
    ]
    atributos = ['Outlook', 'Temperature', 'Humidity', 'Wind']  # Lista de atributos

    # Construir el árbol de decisión
    arbol_decision = construir_arbol_decision(datos, atributos)

    # Mostrar el árbol de decisión
    print("Árbol de Decisión:")
    print(arbol_decision)

if __name__ == "__main__":
    main()

