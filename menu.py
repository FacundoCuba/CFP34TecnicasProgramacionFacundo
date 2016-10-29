import modoAleatorio
import modoPredeterminado
def menu():
    print("¡Bienvenido al Juego \"Luces fuera\"!")
    print("Ingrese el modo de Juego:")
    print("1 para Modo Aletarorio")
    print("2 para Modo Predeterminado")
    print("3 para Salir del Juego")
    inputDelUser = input()
    print("")
    if inputDelUser == "1":
        print("Ud ha elegido el Modo Aleatorio!")
        modoAleatorio.aleatorio()
    elif inputDelUser == "2":
        print("Ud ha elegido el Modo Predeterminado!")
        modoPredeterminado.predeterminado()
    elif inputDelUser == "3":
        print("Saliendo...")
        exit()
    else:
        print("Ingrese una opcion valida!")
        print("")
        menu()


''''
#Tablero
columnas = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
filas = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
dimensiones = int(input("Ingrese el numero de dimensiones para jugar (de 5 a 10): "))
print(" ", columnas[:dimensiones])
for i in range(dimensiones):
    print(filas[i])


'''''