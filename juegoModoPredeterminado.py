import niveles
import menu
import usuario
import switcher

def predeterminado():
    turnosActuales = 15
    while not nivelGanado(nivelActual) and turnosDisponibles(turnosActuales):
        print("Ingrese su movimiento (de A1 a E5), Reinicie el nivel (R) o Regrese al menu principal (M): ")
        movimiento = input().upper()
        if movimiento[0] in niveles.columnas and movimiento[1] in niveles.filas:
            switcher.buscaVecinos(movimiento)
            turnosActuales -= 1
        elif movimiento == "R":
            predeterminado()
        elif movimiento == "M":
            menu.mostrarMenu()
        else:
            print("Ingrese un movimiento valido!")
        print("")
        print("Turnos restantes: ", turnosActuales)
    #TODO ojo que puede que haya ganado
    print("Se le ha acabado los turnos. Intentelo de nuevo!")
    print("")
    menu.mostrarMenu()

def turnosDisponibles(turnosActuales):
    return turnosActuales > 0

nivelActual = [niveles.columnas[:5]]
for fila in niveles.getNivelPredeterminado(usuario.nivelActual):
    nivelActual.append(fila)

def nivelGanado(nivelActual):
    for fila in enumerate(nivelActual):
        print(str(fila))
    busquedaDeNivelGanador(nivelActual)

def busquedaDeNivelGanador(nivel):
    nivel = nivel[1:]
    for fila in nivel:
        for caracter in fila:
            if caracter != ".":
                return False
    return True



