import menu
import niveles
import usuario
import switcher
import juegoModoPredeterminado

tableroDelJugador = None
dimensionEscogida = None

def aleatorio():
    global dimensionEscogida
    turnosActuales = dimensionEscogida * 3
    global tableroDelJugador
    tableroDelJugador = nivelEnJuegoAleatorio()
    juegoModoPredeterminado.impresionInicial(turnosActuales)
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
    pasajeDeNivelAleatorio()

def pasajeDeNivelAleatorio():
    if condicionNivelGanadorAleatorio() is True and usuario.nivelActual <= 5:
        usuario.seguimientoDePuntaje(None, 1)
        impresionDelNivelEnJuegoAleatorio()
        print("")
        usuario.puntajeDelNivel(usuario.nivelActual)
        usuario.nivelActual = usuario.pasarDeNivel(usuario.nivelActual)
        print("")
        aleatorio()
    elif condicionNivelGanadorAleatorio() is True and usuario.nivelActual > 5:
        print("")
        print("Ud a completado el juego. Felicitaciones!!!")
        print("")
        usuario.puntajeTotal()
        print("")
        menu.mostrarMenu()
    else:
        print("")
        print("Se le ha acabado los turnos. Intentelo de nuevo!")
        print("")
        usuario.seguimientoDePuntaje(None, 0)
        usuario.puntajeDelNivel(usuario.nivelActual)
        print("")
        usuario.puntajeTotal()
        print("")
        menu.mostrarMenu()

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
    nivelActualTruncado = tableroDelJugador[1:]
    for fila in nivelActualTruncado:
        for caracter in fila:
            if caracter != ".":
                impresionDelNivelEnJuegoAleatorio()
                return False
    return True

def impresionDelNivelEnJuegoAleatorio():
    global tableroDelJugador
    letras = tableroDelJugador[0]
    panelDeJuego = tableroDelJugador[1:]
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