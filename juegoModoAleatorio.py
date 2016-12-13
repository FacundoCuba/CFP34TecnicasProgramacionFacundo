import niveles
import usuario
import logicasDeJuegoCompartidas

dimensionEscogida = None
tableroDelJugador = None

def aleatorio():
    global dimensionEscogida
    turnosActuales = dimensionEscogida * 3
    global tableroDelJugador
    tableroDelJugador = nivelEnJuegoAleatorio()
    logicasDeJuegoCompartidas.logicaDeMovimiento(condicionNivelGanadorAleatorio, turnosActuales, tableroDelJugador, aleatorio)
    logicasDeJuegoCompartidas.pasajeDeNivel(condicionNivelGanadorAleatorio, impresionDelNivelEnJuegoAleatorio, aleatorio, turnosActuales)

def eleccionDeLaDimension():
    print("Ingrese la dimension del tablero que desee (de 5 a 10):")
    global dimensionEscogida
    dimension = input()
    dimensionesValidas = ("5", "6", "7", "8", "9", "10")
    if dimension in dimensionesValidas:
        dimensionEscogida = int(dimension)
        aleatorio()
    else:
        print("La opcion ingresada no es valida. Intentelo de nuevo!")
        eleccionDeLaDimension()

def nivelEnJuegoAleatorio():
    global dimensionEscogida
    nivel = [niveles.columnas[:dimensionEscogida]]
    if usuario.nivelActual <= 5:
        for fila in niveles.getNivelAleatorio(usuario.nivelActual, dimensionEscogida):
            nivel.append(fila)
    return nivel

def condicionNivelGanadorAleatorio(turnos):
    global tableroDelJugador
    return logicasDeJuegoCompartidas.condicionNivelGanado(tableroDelJugador, impresionDelNivelEnJuegoAleatorio, turnos)

def impresionDelNivelEnJuegoAleatorio(turnos):
    global tableroDelJugador
    logicasDeJuegoCompartidas.impresionNivelYTurnosRestantes(turnos)
    return logicasDeJuegoCompartidas.impresionDelTablero(tableroDelJugador)