from tkinter import *

# Configuración de la raíz
root = Tk()
root.title('Aplicación Roomba') # Título ventana.
root.resizable(0, 0) # Con este comando desactivamos la redimensión de la ventana.
root.config(bg = 'black') # Color fondo. 

# Añadimos la habitación con la función Canvas que nos da una superficie sobre la que podemos dibujar figuras. Es decir, sobre el canvas que hemos creado 'habitacion' vamos a dibujar el mueble.

habitacion = Canvas(width = 500, height= 630, bg = 'light blue')
habitacion.pack()

root.mainloop() # Bucle de la aplicación

