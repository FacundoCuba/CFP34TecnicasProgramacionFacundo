import niveles
def aleatorio():
    print("")
    print("Ingrese la dimension del tablero que desee (de 5 a 10): ")
    dimension = int(input())
    print("")
    if dimension >= 5 and dimension <= 10:
        for fila in enumerate(niveles.nivelAleatorio(dimension)):
            print(fila)
    elif dimension < 5 or dimension > 10:
        print("Ingrese una dimension valida. Intentelo de nuevo!")
        aleatorio()