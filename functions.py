
def inicio(inputDelUser):
    print("Bienvenido al Juego \"Luces fuera\"")
    print("Ingrese el modo de Juego (Aletarorio/Predeterminado/Salir): ")
    inputDelUser = input()
    if inputDelUser == "Aleatorio":
        print("modoAleatorio")
    elif inputDelUser == "Predeterminado":
        print("modoPredeterminado")
    elif inputDelUser == "Salir":
        exit(0)
    else:
        print("Ingrese una opcion valida")
        print("")
        inicio(inputDelUser)

''''
#Tablero
columnas = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
filas = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
dimensiones = int(input("Ingrese el numero de dimensiones para jugar (de 5 a 10): "))
print(" ", columnas[:dimensiones])
for i in range(dimensiones):
    print(filas[i])

#ModoPredeterminado
#Nivel 1
fila11 = ("0", "0", ".", "0", "0")
fila12 = ("0", ".", "0", ".", "0")
fila13 = (".", "0", "0", "0", ".")
fila14 = ("0", ".", "0", ".", "0")
fila15 = ("0", "0", ".", "0", "0")
#Nivel2
fila21 = (".", "0", ".", "0", ".")
fila22 = ("0", "0", ".", "0", "0")
fila23 = (".", "0", ".", "0", ".")
fila24 = ("0", ".", "0", ".", "0")
fila25 = ("0", ".", "0", ".", "0")
#Nivel3
fila31 = ("0", ".", ".", ".", "0")
fila32 = ("0", "0", ".", "0", "0")
fila33 = (".", ".", "0", ".", ".")
fila34 = ("0", ".", "0", ".", ".")
fila35 = ("0", ".", "0", "0", ".")
#Nivel4
fila41 = ("0", "0", ".", "0", "0")
fila42 = (".", ".", ".", ".", ".")
fila43 = ("0", "0", ".", "0", "0")
fila44 = (".", ".", ".", ".", "0")
fila45 = ("0", "0", ".", ".", ".")
#Nivel5
fila51 = (".", ".", ".", "0", "0")
fila52 = (".", ".", ".", "0", "0")
fila53 = (".", ".", ".", ".", ".")
fila54 = ("0", "0", ".", ".", ".")
fila55 = ("0", "0", ".", ".", ".")
''''