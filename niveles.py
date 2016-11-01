import random
import menu

def cargarNivelesPredeterminados():
    niveles = []
    niveles.append([["0", "0", ".", "0", "0"],["0", ".", "0", ".", "0"],[".", "0", "0", "0", "."],["0", ".", "0", ".", "0"],["0", "0", ".", "0", "0"]])
    niveles.append([[".", "0", ".", "0", "."],["0", "0", ".", "0", "0"],[".", "0", ".", "0", "."],["0", ".", "0", ".", "0"],["0", ".", "0", ".", "0"]])
    niveles.append([["0", ".", ".", ".", "0"],["0", "0", ".", "0", "0"],[".", ".", "0", ".", "."],["0", ".", "0", ".", "."],["0", ".", "0", "0", "."]])
    niveles.append([["0", "0", ".", "0", "0"],[".", ".", ".", ".", "."],["0", "0", ".", "0", "0"],[".", ".", ".", ".", "0"],["0", "0", ".", ".", "."]])
    niveles.append([[".", ".", ".", "0", "0"],[".", ".", ".", "0", "0"],[".", ".", ".", ".", "."],["0", "0", ".", ".", "."],["0", "0", ".", ".", "."]])
    return niveles

def getNivelPredeterminado(numeroNivel):
    numeroNivelesValidos = (1, 2, 3, 4, 5)
    if numeroNivel in numeroNivelesValidos:
        print(columnas)
        return nivelesPredeterminados[numeroNivel - 1]
    else:
        print("Nivel no disponible...")
        print("")
        menu.mostrarMenu()

def nivelAleatorio(numeroDeDimension):
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

nivelesPredeterminados = cargarNivelesPredeterminados()
columnas = ("A", "B", "C", "D", "E")
filas = ("1", "2", "3", "4", "5")