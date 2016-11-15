import niveles
import juegoModoPredeterminado

def traduccionDeCoordenadas(movimientoRealizado):
    fila = niveles.filas.index(movimientoRealizado[1])
    columna = niveles.columnas.index(movimientoRealizado[0])
    return fila, columna

def buscaVecinos(movimientoRealizado):
    tuplaDelMovimiento = traduccionDeCoordenadas(movimientoRealizado)
    vecinos = [tuplaDelMovimiento]
    if 0 <= tuplaDelMovimiento[1] - 1 < 5:
        vecinos.append((tuplaDelMovimiento[0], tuplaDelMovimiento[1] - 1))
    if 0 <= tuplaDelMovimiento[0] - 1 < 5:
        vecinos.append((tuplaDelMovimiento[0] - 1, tuplaDelMovimiento[1]))
    if 0 <= tuplaDelMovimiento[1] + 1 < 5:
        vecinos.append((tuplaDelMovimiento[0], tuplaDelMovimiento[1] + 1))
    if 0 <= tuplaDelMovimiento[0] + 1 < 5:
        vecinos.append((tuplaDelMovimiento[0] + 1, tuplaDelMovimiento[1]))
    return vecinos

#TODO mecanismo de swich para las luces
 '''''''''
def swich(movimientoRealizado):
    nivelActual = juegoModoPredeterminado.nivelActual
    lucesACambiar = buscaVecinos(movimientoRealizado)
    for tupla in lucesACambiar:
        if nivelActual[tupla[0]][tupla[1]] == "0":
            nivelActual[tupla[0]][tupla[1]].replace(".")
        elif nivelActual[tupla[0]][tupla[1]] == ".":
            nivelActual[tupla[0]][tupla[1]].replace("0")
'''''''''''