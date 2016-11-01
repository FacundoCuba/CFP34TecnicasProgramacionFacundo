import usuario
import menu

def cargarConfiguracionesIniciales():
    usuario.nivelUsuario()
    usuario.puntajeUsuario()
    puntajePorNivel = {1:0, 2:0, 3:0, 4:0, 5:0}

def iniciarJuego():
    menu.mostrarMenu()

#Funciones primitivas son las que manipulan los datos....