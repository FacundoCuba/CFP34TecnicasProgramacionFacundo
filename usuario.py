def nivelUsuario():
    return 1

def puntajeUsuario():
    return 0

nivelActual = nivelUsuario()
puntajeActual = puntajeUsuario()

def pasarDeNivel(nivelActual):
    nivelActual += 1
    return nivelActual