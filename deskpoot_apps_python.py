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
ventana_principal.config(bg="black")

#----------------------------------
#frame amarillo
#---------------------------------
frame_amarillo = Frame(ventana_principal)
frame_amarillo.config(bg="yellow", width=500, height=250)
frame_amarillo.place(x=0, y=0)
#----------------------------------
#frame azul
#---------------------------------

frame_azul = Frame(ventana_principal)
frame_azul.config(bg="blue", width=500, height=125)
frame_azul.place(x=0, y=250)

#----------------------------------
#frame rojo
#---------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red" , width=500, height=125)
frame_rojo.place(x=0, y=375)


#run
#Se ejecuta el metodo mainloop()a través de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (clik en un boton,escribir,etc). Cada acción del usuario se conoce como un evento. El metodo mainloop() es un bluque infinito. 
ventana_principal.mainloop()
