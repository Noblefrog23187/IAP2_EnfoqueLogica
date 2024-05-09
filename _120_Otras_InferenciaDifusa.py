
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definir variables de entrada
calidad = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad')
servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'servicio')

# Definir variable de salida
propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')

# Definir funciones de pertenencia para las variables de entrada y salida
calidad['baja'] = fuzz.trimf(calidad.universe, [0, 0, 5])
calidad['media'] = fuzz.trimf(calidad.universe, [0, 5, 10])
calidad['alta'] = fuzz.trimf(calidad.universe, [5, 10, 10])

servicio['pobre'] = fuzz.trimf(servicio.universe, [0, 0, 5])
servicio['aceptable'] = fuzz.trimf(servicio.universe, [0, 5, 10])
servicio['excelente'] = fuzz.trimf(servicio.universe, [5, 10, 10])

propina['baja'] = fuzz.trimf(propina.universe, [0, 0, 13])
propina['media'] = fuzz.trimf(propina.universe, [0, 13, 25])
propina['alta'] = fuzz.trimf(propina.universe, [13, 25, 25])

# Definir reglas difusas
regla1 = ctrl.Rule(calidad['baja'] | servicio['pobre'], propina['baja'])
regla2 = ctrl.Rule(servicio['aceptable'], propina['media'])
regla3 = ctrl.Rule(servicio['excelente'] | calidad['alta'], propina['alta'])

# Crear sistema de control
sistema_ctrl = ctrl.ControlSystem([regla1, regla2, regla3])
sistema = ctrl.ControlSystemSimulation(sistema_ctrl)

# Entrada del usuario
sistema.input['calidad'] = 6.5
sistema.input['servicio'] = 9.8

# Calcula el resultado
sistema.compute()

# Imprime el resultado
print("Propina:", sistema.output['propina'])
