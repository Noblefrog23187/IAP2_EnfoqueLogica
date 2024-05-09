# Importar la biblioteca necesaria para la lógica difusa
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definir las variables de entrada y salida del sistema difuso
calidad = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad')
servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'servicio')
propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')

# Definir las funciones de membresía para cada variable
calidad.automf(3)  # Define automáticamente 3 funciones de membresía para la variable calidad
servicio.automf(3)  # Define automáticamente 3 funciones de membresía para la variable servicio
propina['bajo'] = fuzz.trimf(propina.universe, [0, 0, 13])  # Función de membresía triangular para propina baja
propina['medio'] = fuzz.trimf(propina.universe, [0, 13, 25])  # Función de membresía triangular para propina media
propina['alto'] = fuzz.trimf(propina.universe, [13, 25, 25])  # Función de membresía triangular para propina alta

# Definir las reglas del sistema difuso
regla1 = ctrl.Rule(calidad['poor'] | servicio['poor'], propina['bajo'])
regla2 = ctrl.Rule(servicio['average'], propina['medio'])
regla3 = ctrl.Rule(servicio['good'] | calidad['good'], propina['alto'])

# Crear el sistema de control difuso
sistema_propina = ctrl.ControlSystem([regla1, regla2, regla3])
asignacion_propina = ctrl.ControlSystemSimulation(sistema_propina)

# Entrada de ejemplo para el sistema difuso
asignacion_propina.input['calidad'] = 6.5
asignacion_propina.input['servicio'] = 9.8

# Calcula la salida del sistema de control difuso
asignacion_propina.compute()

# Imprime el resultado
print("Propina:", asignacion_propina.output['propina'])
propina.view(sim=asignacion_propina)


