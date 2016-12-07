import menu
import niveles
import usuario
import switcher
import juegoModoPredeterminado
import logicasDeJuegoCompartidas

tableroDelJugador = None
dimensionEscogida = None

def aleatorio():
    global dimensionEscogida
    turnosActuales = dimensionEscogida * 3
    global tableroDelJugador
    tableroDelJugador = nivelEnJuegoAleatorio()
    logicasDeJuegoCompartidas.impresionInicial(turnosActuales)
    while not condicionNivelGanadorAleatorio() and juegoModoPredeterminado.turnosDisponibles(turnosActuales) and usuario.nivelActual <= 5:
        print("")
        # TODO modificar la impresion de la maximo movimiento posible
        print("Ingrese su movimiento (de A1 a E5), Reinicie el nivel (R) o Regrese al menu principal (M):")
        movimiento = input().upper()
        if movimiento[0] in niveles.columnas and movimiento[1] in niveles.filas:
            tableroDelJugador = switcher.swich(movimiento)
            turnosActuales -= 1
        elif movimiento == "R":
            usuario.seguimientoDePuntaje(movimiento, turnosActuales)
            aleatorio()
        elif movimiento == "M":
            menu.mostrarMenu()
        else:
            print("Ingrese un movimiento valido!")
        print("")
        print("NIVEL: " + str(usuario.nivelActual))
        print("Turnos restantes: ", turnosActuales)
    logicasDeJuegoCompartidas.pasajeDeNivel(condicionNivelGanadorAleatorio, impresionDelNivelEnJuegoAleatorio, aleatorio)

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

def condicionNivelGanadorAleatorio():
    global tableroDelJugador
    return logicasDeJuegoCompartidas.condicionNivelGanado(tableroDelJugador, impresionDelNivelEnJuegoAleatorio())

def impresionDelNivelEnJuegoAleatorio():
    global tableroDelJugador
    return logicasDeJuegoCompartidas.impresionDelTablero(tableroDelJugador)