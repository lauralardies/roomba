from tkinter import *

class Aplicacion():
  def __init__(self):

    # Configuración de la raíz.
    self.root = Tk()
    self.root.title('Aplicación Roomba') # Título ventana.
    self.root.resizable(0, 0) # Con este comando desactivamos la redimensión de la ventana.
    self.root.config(bg = 'black') # Color fondo. 
  
    # Añadimos la habitación con la función Canvas que nos da una superficie sobre la que podemos dibujar figuras. Es decir, sobre el canvas que hemos creado 'habitacion' vamos a dibujar el mueble.
    self.habitacion = Canvas(width = 500, height= 630, bg = 'lightyellow1')
    self.habitacion.pack()
    
    # Con la siguiente función pintamos el mueble sobre nuestro canvas 'habitación'.
    self.mueble = self.habitacion.create_rectangle(101, 150, 191, 410, fill = 'navajowhite3')

    # Calculamos el área que tiene que limpiar el roomba. Para ello, dividimos la habitación en 4 rectángulos y calculamos su área.
    self.area_total = self.area(500, 150) + self.area(101, 480) + self.area(309, 480) + self.area(220, 90)
    
    # Calculamos el tiempo estimado que tarda el roomba en limpiar la habitación con obstáculos. 
    self.a = 0.929 # Suponemos que el roomba limpia 92,9 m^2 cada 100 min aproximadamente. Por eso, limpia 0,929 m^2/min.
    self.tiempo = self.area_total/self.a # Obtenemos el tiempo en minutos.
    
    # Añadimos un botón que nos abra una ventana con el tiempo que tarda el roomba en limpiar nuestra habitación.
    self.boton1 = Button(self.root, text = 'Ver tiempo de recorrido', command = self.segunda_ventana(self.tiempo))
    self.boton1.pack(side=RIGHT)

    # Añadimos un botón para cerrar la aplicación.
    self.boton2 = Button(self.root, text = 'Salir', command = self.root.destroy)
    self.boton2.pack(side=LEFT)
    
    self.root.mainloop() # Bucle de la aplicación.

  def area(self, base, altura):
    '''
    Función que devuelve el área de un rectángulo. Los datos introducidos van en cm y el resultado obtenido lo pasamos a m^2.
    '''
    return (base * altura)/10000

  def segunda_ventana(self, tiempo):
    '''
    Función que crea una segunda ventana.
    '''
    ventana_secundaria = Toplevel()
    ventana_secundaria.title('Estimación')
    etiqueta = Label(ventana_secundaria, text = 'Se estima que Roomba tarda en limpar la habitación en ' + str(tiempo) + ' minutos.')
    etiqueta.pack()
    boton = Button(ventana_secundaria, text = "Salir", command = ventana_secundaria.destroy)
    boton.pack()

aplicacion = Aplicacion()