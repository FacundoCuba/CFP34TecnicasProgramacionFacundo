import niveles
import usuario
import menu

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
            # print("Ingrese su movimiento (de A1 a E5), Reinicie el nivel (R) o Regrese al menu principal (M): ")
            # movimiento = list(input().upper())
            # if movimiento[0] in niveles.columnas and movimiento[1] in niveles.filas:
            #   turnos -= 1
            #    print("")
            # elif movimiento == ["R"]:
            #    aleatorio()
            # elif movimiento == ["M"]:
            #    print("")
            #    menu.mostrarMenu()
            # else:
            #    print("Ingrese un movimiento valido!")
            #    print("")
            # print("Se le ha acabado los turnos. Intentelo de nuevo!")
            # print("")
            # menu.mostrarMenu()
        else:
            print("La opcion ingresada no es valida. Intentelo de nuevo!")
            aleatorio()