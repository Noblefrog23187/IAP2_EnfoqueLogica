def evaluar_hecho(hecho, factor_certeza):
    if factor_certeza > 0.5:
        print(f"El hecho '{hecho}' es cierto con un factor de certeza del {factor_certeza * 100}%.")
    elif factor_certeza == 0.5:
        print(f"No se puede determinar la certeza del hecho '{hecho}'.")
    else:
        print(f"El hecho '{hecho}' es falso con un factor de certeza del {(1 - factor_certeza) * 100}%.")

# Función principal
def main():
    # Ejemplos de hechos con sus respectivos factores de certeza
    evaluar_hecho("Llueve hoy", 0.8)
    evaluar_hecho("Hace sol", 0.2)
    evaluar_hecho("El cielo está despejado", 0.5)

if __name__ == "__main__":
    main()


