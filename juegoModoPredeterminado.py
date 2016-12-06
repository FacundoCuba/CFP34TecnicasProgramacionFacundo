import niveles
import menu
import usuario
import switcher

def nivelEnJuego():
    nivel = [niveles.columnas[:5]]
    if usuario.nivelActual <= 5:
        for fila in niveles.getNivelPredeterminado(usuario.nivelActual):
            nivel.append(fila)
    return nivel


tableroDelJugador = None

def predeterminado():
    turnosActuales = 15
    global tableroDelJugador
    tableroDelJugador = nivelEnJuego()
    impresionInicial(turnosActuales)
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
    pasajeDeNivel()

def pasajeDeNivel():
    if condicionNivelGanador() is True and usuario.nivelActual <= 5:
        usuario.seguimientoDePuntaje(None, 1)
        impresionDelNivelEnJuego()
        print("")
        usuario.puntajeDelNivel(usuario.nivelActual)
        usuario.nivelActual = usuario.pasarDeNivel(usuario.nivelActual)
        print("")
        predeterminado()
    elif condicionNivelGanador() is True and usuario.nivelActual > 5:
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

def impresionInicial(turnos):
    if usuario.nivelActual < niveles.getNivelMax():
        print("NIVEL: " + str(usuario.nivelActual))
        print("Turnos restantes: ", turnos)
        print("")

def turnosDisponibles(turnosActuales):
    return turnosActuales > 0

def impresionDelNivelEnJuego():
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

def condicionNivelGanador():
    global tableroDelJugador
    nivelActualTruncado = tableroDelJugador[1:]
    for fila in nivelActualTruncado:
        for caracter in fila:
            if caracter != ".":
                impresionDelNivelEnJuego()
                return False
    return True
