import niveles
import usuario
import logicasDeJuegoCompartidas

tableroDelJugador = None

def predeterminado():
    global tableroDelJugador
    tableroDelJugador = nivelEnJuego()
    turnosActuales = 15
    logicasDeJuegoCompartidas.logicaDeMovimiento(condicionNivelGanador, turnosActuales, tableroDelJugador, predeterminado)
    logicasDeJuegoCompartidas.pasajeDeNivel(condicionNivelGanador, impresionDelNivelEnJuego, predeterminado, turnosActuales)

def nivelEnJuego():
    nivel = [niveles.columnas[:5]]
    if usuario.nivelActual <= 5:
        for fila in niveles.getNivelPredeterminado(usuario.nivelActual):
            nivel.append(fila)
    return nivel

def condicionNivelGanador(turnos):
    global tableroDelJugador
    return logicasDeJuegoCompartidas.condicionNivelGanado(tableroDelJugador, impresionDelNivelEnJuego, turnos)

def impresionDelNivelEnJuego(turnos):
    global tableroDelJugador
    logicasDeJuegoCompartidas.impresionNivelYTurnosRestantes(turnos)
    return logicasDeJuegoCompartidas.impresionDelTablero(tableroDelJugador)