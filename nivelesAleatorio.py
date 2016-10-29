import random
def nivelaleatorio(numeroDeDimension):
    columnas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    columnas = columnas[:(numeroDeDimension)]
    nivel = [columnas]
    for filas in range(numeroDeDimension):
            opciones = ["0", "."]
            fila = []
            for columnas in range(numeroDeDimension):
                fila.append(random.choice(opciones))
            nivel.append(fila)
    return nivel






