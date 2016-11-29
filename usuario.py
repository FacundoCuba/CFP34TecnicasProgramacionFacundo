def nivelUsuario():
    return 1

def seguimientoDePuntaje(opcion, cantidadDeTurnos):
    if opcion == "R" and cantidadDeTurnos > 0:
        puntajePorNivel[nivelActual] += -50
        return puntajePorNivel
    elif opcion == None and cantidadDeTurnos == 0:
        puntajePorNivel[nivelActual] += -300
        return puntajePorNivel
    elif opcion == None and cantidadDeTurnos > 0:
        puntajePorNivel[nivelActual] += 500
        return puntajePorNivel

def puntajeDelNivel(nivel):
    print("Ha ganado " + str(puntajePorNivel[nivel]) + " puntos en el nivel " + str(nivel) + "!!!")

def puntajeTotal():
    total = sum(puntajePorNivel.values())
    print("Ha ganado " + str(total) + " en total!!!")

nivelActual = nivelUsuario()
puntajePorNivel = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

def pasarDeNivel(nivelActual):
    nivelActual += 1
    return nivelActual