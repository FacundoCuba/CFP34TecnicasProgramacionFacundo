import niveles
import usuario
import logicasDeJuegoCompartidas

tableroDelJugador = None

def predeterminado():
    turnosActuales = 15
    global tableroDelJugador
    tableroDelJugador = nivelEnJuego()
    logicasDeJuegoCompartidas.logicaDeMovimiento(condicionNivelGanador, turnosActuales, tableroDelJugador, predeterminado)
    logicasDeJuegoCompartidas.pasajeDeNivel(condicionNivelGanador, impresionDelNivelEnJuego, predeterminado)

def nivelEnJuego():
    nivel = [niveles.columnas[:5]]
    if usuario.nivelActual <= 5:
        for fila in niveles.getNivelPredeterminado(usuario.nivelActual):
            nivel.append(fila)
    return nivel

def condicionNivelGanador():
    global tableroDelJugador
    return logicasDeJuegoCompartidas.condicionNivelGanado(tableroDelJugador, impresionDelNivelEnJuego())

def impresionDelNivelEnJuego():
    global tableroDelJugador
    return logicasDeJuegoCompartidas.impresionDelTablero(tableroDelJugador)