# --------------------------------
# Deskpoot_apps_python
#---------------------------------

# Se inporta la librreria de tkinter con todas sus funciones
from tkinter import *

#-------------------------------
# Funsiones de la app
#--------------------------------

#--------------------------------
# ventana principal de la app
#--------------------------------

# Se declara una ventana llamada ventana principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

#Titulo de la ventana
ventana_principal.title("Bandera de Colombia")

 #Tamaño de la ventana
ventana_principal.geometry("500x500")

#Desabilitar boton de maximizar
ventana_principal.resizable(False, False)

#Color de fondo de la ventana
ventana_principal.config(bg="red")

#----------------------------------
#frame blanco1
#---------------------------------
frame_blanco1 = Frame(ventana_principal)
frame_blanco1.config(bg="white", width=100, height=300)
frame_blanco1.place(x=200, y=100)

#----------------------------------
#frame blanco
#---------------------------------
frame_blanco2 = Frame(ventana_principal)
frame_blanco2.config(bg="white", width=300, height=100)
frame_blanco2.place(x=100, y=200)

#run
#Se ejecuta el metodo mainloop()a través de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (clik en un boton,escribir,etc). Cada acción del usuario se conoce como un evento. El metodo mainloop() es un bluque infinito. 
ventana_principal.mainloop()