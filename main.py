from tkinter import *

# Configuración de la raíz
root = Tk()
root.title('Aplicación Roomba') # Título ventana.
root.resizable(0, 0) # Con este comando desactivamos la redimensión de la ventana.
root.config(bg = 'black') # Color fondo. 

# Añadimos la habitación con la función Canvas que nos da una superficie sobre la que podemos dibujar figuras. Es decir, sobre el canvas que hemos creado 'habitacion' vamos a dibujar el mueble.
habitacion = Canvas(width = 500, height= 630, bg = 'lightyellow1')
habitacion.pack()

# Con la siguiente función pintamos el mueble sobre nuestro canvas 'habitación'.
mueble = habitacion.create_rectangle(101, 150, 191, 410, fill = 'navajowhite3')

root.mainloop() # Bucle de la aplicación.

# Una vez creada la ventana, el siguiente paso es calcular el área que tiene que limpiar el roomba. Para ello, dividimos la habitación en 4 rectángulos y calculamos su área.

def area(base, altura):
  '''
  Función que devuelve el área de un rectángulo. Los datos introducidos van en cm y el resultado obtenido lo pasamos a m^2.
  '''
  return (base * altura)/10000

area_total = area(500, 150) + area(101, 480) + area(309, 480) + area(220, 90)

# Por último, calculamos el tiempo que tarda el roomba en limpiar la habitación con el mueble.

a = 0,929 # Suponemos que el roomba limpia 92,9 m^2 cada 100 min aproximadamente. Por eso, limpia 0,929 m^2/min.

tiempo = area_total/a # Obtenemos el tiempo en minutos.

#Añadimos una etiqueta con el tiempo tarda el roomba en limpiar nuestra habitación