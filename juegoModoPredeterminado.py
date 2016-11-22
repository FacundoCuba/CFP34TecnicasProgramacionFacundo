import niveles
import menu
import usuario
import switcher

nivelActual = [niveles.columnas[:5]]
for fila in niveles.getNivelPredeterminado(usuario.nivelActual):
    nivelActual.append(fila)

def predeterminado():
    turnosActuales = 15
    print("Turnos restantes: ", turnosActuales)
    while not busquedaDeNivelGanador() and turnosDisponibles(turnosActuales):
        print("Ingrese su movimiento (de A1 a E5), Reinicie el nivel (R) o Regrese al menu principal (M): ")
        movimiento = input().upper()
        if movimiento[0] in niveles.columnas and movimiento[1] in niveles.filas:
            nivelActual = switcher.swich(movimiento)
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

def nivelGanado():
    letras = nivelActual[0]
    panelDeJuego = nivelActual[1:]
    filaDeLetras = "   "
    for letra in letras:
        filaDeLetras += " " + letra
    print(filaDeLetras)
    numeroDeFila = 1
    for fila in panelDeJuego:
        filaEntera = "%d |" % numeroDeFila
        numeroDeFila += 1
        for caracter in fila:
            filaEntera += " " + caracter
        print(filaEntera)

def busquedaDeNivelGanador():
    nivelActualTruncado = nivelActual[1:]
    for fila in nivelActualTruncado:
        for caracter in fila:
            if caracter != ".":
                nivelGanado()
                return False
    return True



