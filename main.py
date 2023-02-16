from tkinter import *


class Habitacion():
  '''
  Clase que define las dimensiones de nuestra habitación.
  '''
  def __init__(self, largo, ancho):
    self.largo = largo
    self.ancho = ancho

habitacion = Habitacion(630, 500)  #Nuestras medidas sin el borde

# Configuración de la raíz
root = Tk()
root.title('Aplicación Roomba') # Título ventana.
root.resizable(0, 0) # Con este comando desactivamos la redimensión de la ventana.
root.config(bg = 'light blue') # Color fondo. 

root.mainloop() # Bucle de la aplicación

