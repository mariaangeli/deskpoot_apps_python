# --------------------------------
# Deskpoot_apps_python
#---------------------------------

# Se inporta la librreria de tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

#-------------------------------
# Funsiones de la app
#--------------------------------

# Sumar 
def sumar():
    pass
# Borrar
def borrar():
    pass 
#Salir 
def salir():
    messagebox.showinfo("Suma Enteros 1.0","la app se va a cerrar")
    ventana_principal.destroy()

#--------------------------------
# ventana principal de la app
#--------------------------------

# Se declara una ventana llamada ventana principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

#Titulo de la ventana
ventana_principal.title("Suma Enteros")

 #Tamaño de la ventana
ventana_principal.geometry("500x500")

#Desabilitar boton de maximizar
ventana_principal.resizable(False, False)

#Color de fondo de la ventana
ventana_principal.config(bg="purple")

#----------------------------------
#variables globales
#---------------------------------
x = StringVar()
y = StringVar()

#----------------------------------
#frame entrada
#---------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=180)
frame_entrada.place(x=10, y=10)

#Logo de la app
logo = PhotoImage (file="ing/escudo_colegio.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=70,y=40)

#titulo de la app
titulo = Label(frame_entrada, text="Suma Enteros 1.0")
titulo.config(bg="white", fg="purple", font=("Arial", 16))
titulo.place(x=240,y=10)

#Etiqueta para valor de x
lb_x = Label(frame_entrada, text = "x = ")
lb_x.config(bg="white", fg="purple", font=("Helvetica", 18))
lb_x.place(x=240,y=60)

#caja de texto para valor de x
entry_x = Entry(frame_entrada,textvariable=X)
entry_x.config(bg="white", fg="blue", font=("Tines New Roman", 18), width=6)
entry_x.focus_set()
entry_x.place(x=290,y=60)

#Etiqueta para valor de y
lb_y = Label(frame_entrada, text = "y = ")
lb_y.config(bg="white", fg="purple", font=("Helvetica", 18))
lb_y.place(x=240,y=120)

#caja de texto para valor de y
entry_y = Entry(frame_entrada,textvariable=X)
entry_y.config(bg="white", fg="blue", font=("Tines New Roman", 18), width=6)
entry_y.focus_set()
entry_y.place(x=290,y=120)


#----------------------------------
#frame operaciones
#---------------------------------

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=100)
frame_operaciones.place(x=10, y=200)

#boton para sumar
bt_sumar = Button(frame_operaciones,text="Sumar",command=sumar)
bt_sumar.place(x=45,y=35, width=100, height=30)

#boton para borrar
bt_borrar = Button(frame_operaciones, text="Borrar",command=borrar)
bt_borrar.place(x=190,y=35, width=100, height=30)

#boton para salir
bt_salir = Button(frame_operaciones,text="Salir",command=salir)
bt_salir.place(x=335,y=35,width=100, height=30 )

#----------------------------------
#frame resultados
#---------------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white" , width=480, height=180)
frame_resultados.place(x=10, y=310)

#area de textos para los resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="black", fg="green yellow", font=("Courier", 20))
t_resultados.place(x=10,y=10,width=460, height=160)

#run
#Se ejecuta el metodo mainloop()a través de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (clik en un boton,escribir,etc). Cada acción del usuario se conoce como un evento. El metodo mainloop() es un bluque infinito. 
ventana_principal.mainloop()