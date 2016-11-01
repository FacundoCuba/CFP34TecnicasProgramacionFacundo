import niveles
def aleatorio():
    print("")
    print("Ingrese la dimension del tablero que desee (de 5 a 10): ")
    dimension = input()
    dimensionesValidas = ("5", "6", "7", "8", "9", "10")
    print("")
    if dimension in dimensionesValidas:
        for fila in enumerate(niveles.nivelAleatorio(int(dimension))):
            print(fila)
    else:
        print("La opcion ingresada no es valida. Intentelo de nuevo!")
        aleatorio()