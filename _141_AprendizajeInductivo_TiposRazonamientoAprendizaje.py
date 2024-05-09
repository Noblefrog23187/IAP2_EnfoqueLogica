

datos = [
    (30, 80, False, 'soleado'),
    (22, 40, True, 'lluvioso'),
    (25, 65, True, 'nublado'),
    (18, 50, False, 'lluvioso'),
]

# Función para predecir el clima basada en el aprendizaje inductivo
def predecir_clima(datos_entrenamiento, nueva_lectura):
    # Iterar sobre los datos de entrenamiento
    for lectura in datos_entrenamiento:
        # Si la nueva lectura coincide con algún dato de entrenamiento, devolver el clima
        if lectura[:-1] == nueva_lectura:
            return lectura[-1]
    # Si no se encuentra una coincidencia, devolver un mensaje de error
    return "No se puede predecir el clima"

# Función principal
def main():
    # Nueva lectura de temperatura, humedad y viento
    nueva_lectura = (28, 70, False)
    # Predecir el clima para la nueva lectura
    prediccion = predecir_clima(datos, nueva_lectura)
    # Imprimir la predicción del clima
    print("La predicción del clima para la nueva lectura es:", prediccion)

if __name__ == "__main__":
    main()

