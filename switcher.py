import niveles
import juegoModoPredeterminado

def traduccionDeCoordenadas(movimientoRealizado):
    fila = niveles.filas.index(movimientoRealizado[1])
    columna = niveles.columnas.index(movimientoRealizado[0])
    return (fila, columna)

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