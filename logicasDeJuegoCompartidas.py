import menu
import usuario
import niveles
import switcher

def impresionDelTablero(tablero):
    letras = tablero[0]
    panelDeJuego = tablero[1:]
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

def condicionNivelGanado(tablero, impresion):
    nivelActualTruncado = tablero[1:]
    for fila in nivelActualTruncado:
        for caracter in fila:
            if caracter != ".":
                impresion
                return False
    return True

def impresionInicial(turnos):
    if usuario.nivelActual < niveles.getNivelMax():
        print("NIVEL: " + str(usuario.nivelActual))
        print("Turnos restantes: ", turnos)
        print("")

def pasajeDeNivel(nivelGanado, impresion, tipoDeJuego):
    nivelYaGanado = nivelGanado()
    if nivelYaGanado and usuario.nivelActual <= 5:
        usuario.seguimientoDePuntaje(None, 1)
        impresion()
        print("")
        usuario.puntajeDelNivel(usuario.nivelActual)
        usuario.nivelActual = usuario.pasarDeNivel(usuario.nivelActual)
        print("")
        tipoDeJuego()
    elif nivelYaGanado and usuario.nivelActual > 5:
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

def turnosDisponibles(turnosActuales):
    return turnosActuales > 0

def logicaDeMovimiento(condicionNivelGanador, turnos, tablero, tipoDeJuego):
    impresionInicial(turnos)
    while not condicionNivelGanador() and turnosDisponibles(turnos) and usuario.nivelActual <= 5:
        print("")
        print("Ingrese su movimiento (de A1 a E5), Reinicie el nivel (R) o Regrese al menu principal (M):")
        movimiento = input().upper()
        if movimiento[0] in niveles.columnas and movimiento[1] in niveles.filas:
            tablero = switcher.swich(movimiento)
            turnos -= 1
        elif movimiento == "R":
            usuario.seguimientoDePuntaje(movimiento, turnos)
            tipoDeJuego()
        elif movimiento == "M":
            menu.mostrarMenu()
        else:
            print("Ingrese un movimiento valido!")
        print("")
        print("NIVEL: " + str(usuario.nivelActual))
        print("Turnos restantes: ", turnos)