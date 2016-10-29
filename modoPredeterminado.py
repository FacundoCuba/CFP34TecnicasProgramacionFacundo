import nivelesPredeterminado
import menu
def predeterminado():
    turnos = 15
    while turnos > 0:
        print("")
        print("Turnos restantes: ", turnos)
        print("")
        for fila in enumerate(nivelesPredeterminado.nivel1):
            print(str(fila))
        print("")
        print("Ingrese su movimiento (de A1 a E5), Reinicie el nivel (R) o Regrese al menu principal (M): ")
        movimiento = list(input().upper())
        if movimiento[0] in nivelesPredeterminado.columnas and movimiento[1] in nivelesPredeterminado.filas:
            turnos -= 1
            print("")
        elif movimiento == ["R"]:
            predeterminado()
        elif movimiento == ["M"]:
            print("")
            menu.menu()
        else:
            print("Ingrese un movimiento valido!")
            print("")
    print("Se le ha acabado los turnos. Intentelo de nuevo!")
    print("")
    menu.menu()