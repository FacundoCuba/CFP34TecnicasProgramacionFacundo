nivel = [["A", "B", "C", "D", "E"],["0", "0", ".", "0", "0"],["0", ".", "0", ".", "0"],[".", "0", "0", "0", "."],["0", ".", "0", ".", "0"],["0", "0", ".", "0", "0"]]
for i in enumerate(nivel):
    print(i)
columnas = ["A", "B", "C", "D", "E"]
filas = ["1", "2", "3", "4", "5"]
movimiento = list(input().upper())
lucesACambiar = [nivel[(filas.index(movimiento[1])+1)][(columnas.index(movimiento[0]))],
                 nivel[(filas.index(movimiento[1])+1)][(columnas.index(movimiento[0])-1)],
                 nivel[(filas.index(movimiento[1]))][(columnas.index(movimiento[0]))],
                 nivel[(filas.index(movimiento[1])+1)][(columnas.index(movimiento[0])+1)],
                 nivel[(filas.index(movimiento[1])+2)][(columnas.index(movimiento[0]))]]
print(lucesACambiar)
for luz in lucesACambiar:
    if luz == ".":
        lucesACambiar[lucesACambiar.index(luz)] = lucesACambiar[lucesACambiar.index(luz)].replace(".","0")
        print(lucesACambiar)
    elif luz == "0":
        lucesACambiar[lucesACambiar.index(luz)] = lucesACambiar[lucesACambiar.index(luz)].replace("0", ".")
        print(lucesACambiar)
print("")
print(lucesACambiar)
print("")
for i in enumerate(nivel):
    print(i)