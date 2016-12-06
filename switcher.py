import niveles
import juegoModoPredeterminado
import juegoModoAleatorio

def traduccionDeCoordenadas(movimientoRealizado):
    fila = niveles.filas.index(movimientoRealizado[1])
    columna = niveles.columnas.index(movimientoRealizado[0])
    return fila, columna

def buscaVecinos(movimientoRealizado, maximaDimension):
    tuplaDelMovimiento = traduccionDeCoordenadas(movimientoRealizado)
    vecinos = [tuplaDelMovimiento]
    if 0 <= tuplaDelMovimiento[1] - 1 < maximaDimension:
        vecinos.append((tuplaDelMovimiento[0], tuplaDelMovimiento[1] - 1))
    if 0 <= tuplaDelMovimiento[0] - 1 < maximaDimension:
        vecinos.append((tuplaDelMovimiento[0] - 1, tuplaDelMovimiento[1]))
    if 0 <= tuplaDelMovimiento[1] + 1 < maximaDimension:
        vecinos.append((tuplaDelMovimiento[0], tuplaDelMovimiento[1] + 1))
    if 0 <= tuplaDelMovimiento[0] + 1 < maximaDimension:
        vecinos.append((tuplaDelMovimiento[0] + 1, tuplaDelMovimiento[1]))
    return vecinos

def swich(movimientoRealizado):
    if juegoModoAleatorio.tableroDelJugador == None:
        nivelEnJuego = juegoModoPredeterminado.tableroDelJugador
        lucesACambiar = buscaVecinos(movimientoRealizado, len(nivelEnJuego[0]))
    elif juegoModoPredeterminado.tableroDelJugador == None:
        nivelEnJuego = juegoModoAleatorio.tableroDelJugador
        lucesACambiar = buscaVecinos(movimientoRealizado, len(nivelEnJuego[0]))
    for vecino in lucesACambiar:
        if nivelEnJuego[vecino[0]+1][vecino[1]] == "0":
            nivelEnJuego[vecino[0]+1][vecino[1]] = nivelEnJuego[vecino[0]+1][vecino[1]].replace("0", ".")
        elif nivelEnJuego[vecino[0]+1][vecino[1]] == ".":
            nivelEnJuego[vecino[0]+1][vecino[1]] = nivelEnJuego[vecino[0]+1][vecino[1]].replace(".", "0")
    return nivelEnJuego