import cv2
import math
import numpy
import random
import multiprocessing as mp
from scipy.misc import imread
import matplotlib.pyplot as graficador

def obtenerImagenEscalaGrises(imagenRGB):
	# Convertimos la imagen en escala de grises.
	imagen = cv2.cvtColor(imagenRGB, cv2.COLOR_BGR2GRAY)
	
	alto, ancho = imagen.shape

	imagenEscalaGrises = []

	for i in range(alto):
		fila = []
		
		for j in range(ancho):
			r, g, b = imagenRGB[i, j]
			r, g, b = int(r), int(g), int(b)
			#nivelGris = int(imagen[i, j])
			nivelGris = int((r + g + b) // 3)
			fila.append(nivelGris)

		imagenEscalaGrises.append(fila)

	return imagenEscalaGrises


nombreImagen = 'japon.png'

# Lectura de imagen.
imagen = cv2.imread(nombreImagen)

alto, ancho, canales = imagen.shape
imagenEscalaGrises = obtenerImagenEscalaGrises(imagen)


minX = 0
minY = 0
maxY = alto
maxX = ancho
puntos = []
xPuntos = []
yPuntos = []
xCentros = []
yCentros = []
cambio = []
clase = 0

centros = int(input('Número de centros: '))
numMuestras = int(input('Número de muestras: '))

#factor de Aprendizaje propuesto:
factor = int(input('Factor de Aprendizaje: '))
factor = 0.1

print("Centros iniciales: ")

for i in range(centros):
	x = random.randint(minX, maxX - 1)
	y = random.randint(minY, maxY - 1)
	xCentros.append(x)
	yCentros.append(y)
	cambio.append(0)

	print("Z{}: {},{}".format(i+1, x, y))

for i in range(numMuestras):
	x = random.randint(minX, maxX - 1)
	y = random.randint(minY, maxY - 1)
	#x= int(input())
	#y= int(input())

	xPuntos.append(x)
	yPuntos.append(y)
	puntos.append((x, y))


graficador.figure('Muestras')
graficador.title('Conjunto de puntos')
graficador.axis([minX, maxX, minY, maxY])
fondoImagen = graficador.imread(nombreImagen)
graficador.imshow(fondoImagen[::-1])
graficador.plot(xPuntos, yPuntos, 'o')

for i in range(centros):
	graficador.plot(xCentros[i], yCentros[i], '^')


print('-------------------------')

band = 0


for i in range(1, numMuestras):	
	cont = 0
	x, y = puntos[i][0], puntos[i][1]
	nivelGrisPunto = imagenEscalaGrises[y][x]
	
	distanciaMinima = 2 ** 32
	for j in range(centros):
		#d = math.sqrt((puntos[i][0] - media[j][0])**2 + (puntos[i][1] - media[j][1])**2)
		x, y = int(xCentros[j]), int(yCentros[j])
		grisMedia = imagenEscalaGrises[y][x]
		d = math.fabs(nivelGrisPunto - grisMedia)
			
		if(d < distanciaMinima):
			distanciaMinima = d
			clase = j

	
	#---calculamos el nuevo centro ---#

	auxX = xCentros[clase]
	auxY = yCentros[clase]

	xCentros[clase] = xCentros[clase] + factor*(puntos[i][0] - xCentros[clase])
	yCentros[clase] = yCentros[clase] + factor*(puntos[i][0] - yCentros[clase])

	if(abs(xCentros[clase] - auxX) < 0.5 and abs(yCentros[clase] - auxY) < 0.5):
		cambio[clase] = 1

	for j in range(centros):
		if(cambio[j] == 1):
			cont += 1

	if(cont == centros):
		break;	

fondoImagen = graficador.imread(nombreImagen)
graficador.imshow(fondoImagen[::-1])

graficador.axis([minX, maxX, minY, maxY])
graficador.legend()
graficador.show()