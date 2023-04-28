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
ventana_principal.title("Bandera de Noruega")

 #Tamaño de la ventana
ventana_principal.geometry("600x600")

#Desabilitar boton de maximizar
ventana_principal.resizable(False, False)

#Color de fondo de la ventana
ventana_principal.config(bg="black")

#----------------------------------
#frame rojo
#---------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red", width=500, height=125)
frame_rojo.place(x=0, y=0)

#----------------------------------
#frame rojo
#----------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red", width=500, height=150)
frame_rojo.place(x=0, y=0)

#----------------------------------
#frame blanco
#---------------------------------

frame_blanco= Frame(ventana_principal)
frame_blanco.config(bg="white", width=250, height=600)
frame_blanco.place(x=250, y=0)

#----------------------------------
#frame blanco
#---------------------------------

frame_blanco= Frame(ventana_principal)
frame_blanco.config(bg="white", width=500, height=300)
frame_blanco.place(x=0, y=250)

#----------------------------------
#frame azul
#---------------------------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg="blue", width=150, height=600)
frame_azul.place(x=400, y=0)
#----------------------------------
#frame azul
#---------------------------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg="blue", width=250, height=100)
frame_azul.place(x=0, y=250)

#----------------------------------
#frame rojo
#---------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red" , width=500, height=150)
frame_rojo.place(x=0, y=375)

#----------------------------------
#frame rojo
#----------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red" , width=500, height=250)
frame_rojo.place(x=375, y=0)
#run
#Se ejecuta el metodo mainloop()a través de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (clik en un boton,escribir,etc). Cada acción del usuario se conoce como un evento. El metodo mainloop() es un bluque infinito. 
ventana_principal.mainloop()