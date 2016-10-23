
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