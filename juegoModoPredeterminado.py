import niveles
import menu
import usuario
import switcher
import logicasDeJuegoCompartidas

tableroDelJugador = None

def predeterminado():
    turnosActuales = 15
    global tableroDelJugador
    tableroDelJugador = nivelEnJuego()
    logicasDeJuegoCompartidas.impresionInicial(turnosActuales)
    while not condicionNivelGanador() and turnosDisponibles(turnosActuales) and usuario.nivelActual <= 5:
        print("")
        print("Ingrese su movimiento (de A1 a E5), Reinicie el nivel (R) o Regrese al menu principal (M):")
        movimiento = input().upper()
        if movimiento[0] in niveles.columnas and movimiento[1] in niveles.filas:
            tableroDelJugador = switcher.swich(movimiento)
            turnosActuales -= 1
        elif movimiento == "R":
            usuario.seguimientoDePuntaje(movimiento, turnosActuales)
            predeterminado()
        elif movimiento == "M":
            menu.mostrarMenu()
        else:
            print("Ingrese un movimiento valido!")
        print("")
        print("NIVEL: " + str(usuario.nivelActual))
        print("Turnos restantes: ", turnosActuales)
    logicasDeJuegoCompartidas.pasajeDeNivel(condicionNivelGanador, impresionDelNivelEnJuego, predeterminado)

def nivelEnJuego():
    nivel = [niveles.columnas[:5]]
    if usuario.nivelActual <= 5:
        for fila in niveles.getNivelPredeterminado(usuario.nivelActual):
            nivel.append(fila)
    return nivel

def turnosDisponibles(turnosActuales):
    return turnosActuales > 0

def condicionNivelGanador():
    global tableroDelJugador
    return logicasDeJuegoCompartidas.condicionNivelGanado(tableroDelJugador, impresionDelNivelEnJuego())

def impresionDelNivelEnJuego():
    global tableroDelJugador
    return logicasDeJuegoCompartidas.impresionDelTablero(tableroDelJugador)