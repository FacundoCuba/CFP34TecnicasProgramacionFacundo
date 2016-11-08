import niveles
import usuario

def aleatorio():
    print("")
    print("Ingrese la dimension del tablero que desee (de 5 a 10): ")
    dimension = input()
    dimensionesValidas = ("5", "6", "7", "8", "9", "10")
    print("")
    turnos = int(dimension) * 3
    while turnos > 0:
        print("")
        print("Turnos restantes: ", turnos)
        print("")
        if dimension in dimensionesValidas:
            for fila in enumerate(niveles.getNivelAleatorio(usuario.nivelActual, int(dimension))):
                print(fila)
            print("")
        else:
            print("La opcion ingresada no es valida. Intentelo de nuevo!")
            aleatorio()