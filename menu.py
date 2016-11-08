import juenoModoAleatorio
import juegoModoPredeterminado
def mostrarMenu():
    print("¡Bienvenido al Juego \"Luces fuera\"!")
    print("Ingrese el modo de Juego:")
    print("1 para Modo Aletarorio")
    print("2 para Modo Predeterminado")
    print("3 para Salir del Juego")
    inputDelUser = input()
    print("")
    if inputDelUser == "1":
        print("Ud ha elegido el Modo Aleatorio!")
        juenoModoAleatorio.aleatorio()
    elif inputDelUser == "2":
        print("Ud ha elegido el Modo Predeterminado!")
        juegoModoPredeterminado.predeterminado()
    elif inputDelUser == "3":
        print("Saliendo...")
        exit()
    else:
        print("Ingrese una opcion valida!")
        print("")
        mostrarMenu()