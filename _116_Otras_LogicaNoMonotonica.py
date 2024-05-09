# Definir la base de conocimientos
base_conocimientos = {
    "ave(vencejo)": True,     # Los vencejos son aves
    "vuela(vencejo)": True,   # Los vencejos vuelan
    "vuela(pinguino)": False, # Los pingüinos no vuelan
    "ave(pinguino)": True     # Los pingüinos son aves
}

# Definir el razonador no monotónico
def razonador_no_monotonico(consulta):
    # Verificar si la consulta está en la base de conocimientos
    if consulta in base_conocimientos:
        return base_conocimientos[consulta] # Si la consulta está en la base de conocimientos, devuelve el valor asociado
    else:
        # Regla de predicción no monotónica: Si no hay información explícita, asumir que un ave vuela
        if "ave" in consulta:
            return True # Si la consulta implica que un animal es un ave, asume que vuela
        else:
            return "No se puede determinar" # Si no se puede determinar, devuelve un mensaje indicando que no se puede determinar

# Función principal
def main():
    # Ejemplos de consultas al razonador no monotónico
    print("¿El vencejo vuela?", razonador_no_monotonico("vuela(vencejo)")) # Consulta si el vencejo vuela
    print("¿El pingüino vuela?", razonador_no_monotonico("vuela(pinguino)")) # Consulta si el pingüino vuela
    print("¿El pingüino es un ave?", razonador_no_monotonico("ave(pinguino)")) # Consulta si el pingüino es un ave
    print("¿El gorrión vuela?", razonador_no_monotonico("vuela(gorrion)")) # Consulta sobre un gorrión no presente en la base de conocimientos

if __name__ == "__main__":
    main()


