import random
import menu

columnas = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
filas = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
numeroNivelesValidos = (1, 2, 3, 4, 5)

def cargarNivelesPredeterminados():
    niveles = []
    niveles.append([["0", "0", ".", "0", "0"],["0", ".", "0", ".", "0"],[".", "0", "0", "0", "."],["0", ".", "0", ".", "0"],["0", "0", ".", "0", "0"]])
    niveles.append([[".", "0", ".", "0", "."],["0", "0", ".", "0", "0"],[".", "0", ".", "0", "."],["0", ".", "0", ".", "0"],["0", ".", "0", ".", "0"]])
    niveles.append([["0", ".", ".", ".", "0"],["0", "0", ".", "0", "0"],[".", ".", "0", ".", "."],["0", ".", "0", ".", "."],["0", ".", "0", "0", "."]])
    niveles.append([["0", "0", ".", "0", "0"],[".", ".", ".", ".", "."],["0", "0", ".", "0", "0"],[".", ".", ".", ".", "0"],["0", "0", ".", ".", "."]])
    niveles.append([[".", ".", ".", "0", "0"],[".", ".", ".", "0", "0"],[".", ".", ".", ".", "."],["0", "0", ".", ".", "."],["0", "0", ".", ".", "."]])
    return niveles

def getNivelMax():
    return len(numeroNivelesValidos)

def getNivelPredeterminado(numeroNivel):
    if numeroNivel in numeroNivelesValidos:
        return cargarNivelesPredeterminados()[numeroNivel - 1]

def nivelAleatorio(numeroDeDimension):
    nivel = []
    for fila in range(numeroDeDimension):
        opciones = ["0", "."]
        fila = []
        for columna in range(numeroDeDimension):
            fila.append(random.choice(opciones))
        nivel.append(fila)
    return nivel

def cargarNivelesAleatorios(numeroDeDimension):
    niveles = []
    for nivel in range(5):
        niveles.append(nivelAleatorio(numeroDeDimension))
    return niveles

def getNivelAleatorio(numeroNivel,numeroDeDimension):
    numeroNivelesValidos = (1, 2, 3, 4, 5)
    if numeroNivel in numeroNivelesValidos:
        return cargarNivelesAleatorios(numeroDeDimension)[numeroNivel - 1]
    else:
        print("Nivel no disponible...")
        print("")
        menu.mostrarMenu()