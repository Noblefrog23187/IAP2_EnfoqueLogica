import numpy as np  # Importa numpy para operaciones numéricas
import skfuzzy as fuzz  # Importa skfuzzy para lógica difusa
from skfuzzy import control as ctrl  # Importa control de skfuzzy para el sistema de control

# Definir las variables de entrada y salida
temperatura = ctrl.Antecedent(np.arange(0, 101, 1), 'temperatura')  # Variable de entrada: temperatura
velocidad = ctrl.Consequent(np.arange(0, 101, 1), 'velocidad')  # Variable de salida: velocidad

# Definir las funciones de membresía para la temperatura
temperatura['baja'] = fuzz.trimf(temperatura.universe, [0, 0, 50])  # Membresía baja
temperatura['media'] = fuzz.trimf(temperatura.universe, [0, 50, 100])  # Membresía media
temperatura['alta'] = fuzz.trimf(temperatura.universe, [50, 100, 100])  # Membresía alta

# Definir las funciones de membresía para la velocidad
velocidad['baja'] = fuzz.trimf(velocidad.universe, [0, 0, 50])  # Membresía baja
velocidad['media'] = fuzz.trimf(velocidad.universe, [0, 50, 100])  # Membresía media
velocidad['alta'] = fuzz.trimf(velocidad.universe, [50, 100, 100])  # Membresía alta

# Visualizar las funciones de membresía
temperatura.view()
velocidad.view()

# Definir las reglas del sistema de control
regla1 = ctrl.Rule(temperatura['baja'], velocidad['alta'])  # Si la temperatura es baja, la velocidad es alta
regla2 = ctrl.Rule(temperatura['media'], velocidad['media'])  # Si la temperatura es media, la velocidad es media
regla3 = ctrl.Rule(temperatura['alta'], velocidad['baja'])  # Si la temperatura es alta, la velocidad es baja

# Crear el controlador
controlador = ctrl.ControlSystem([regla1, regla2, regla3])  # Combinar las reglas en un sistema de control

# Simular el controlador con una temperatura específica
control = ctrl.ControlSystemSimulation(controlador)  # Crear una instancia de simulación del controlador
control.input['temperatura'] = 75  # Establecer la temperatura
control.compute()  # Calcular la salida del controlador

# Imprimir el resultado
print("Velocidad del ventilador:", control.output['velocidad'])  # Imprimir la velocidad calculada
velocidad.view(sim=control)  # Visualizar la velocidad en el universo de salida

