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


nombreImagen = 'italia.png'

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
media = []
clase = 0
conjunto = [[]]
ctrl = 1

umbral = int(input("Umbral: "))

numMuestras = int(input('Número de muestras: '))

for i in range(numMuestras):
	x = random.randint(minX, maxX - 1)
	y = random.randint(minY, maxY - 1)
	#x= int(input())
	#y= int(input())

	xPuntos.append(x)
	yPuntos.append(y)
	puntos.append((x, y))

	if(i == 0):
		media.append((x, y))
		conjunto[0].append(i)

graficador.figure('Muestras')
graficador.title('Conjunto de puntos')
graficador.axis([minX, maxX, minY, maxY])
fondoImagen = graficador.imread(nombreImagen)
graficador.imshow(fondoImagen[::-1])
graficador.plot(xPuntos, yPuntos, 'o')


print('-------------------------')


for i in range(1, numMuestras):	
	distanciaMinima = 2 ** 32
	x, y = puntos[i][0], puntos[i][1]
	nivelGrisPunto = imagenEscalaGrises[y][x]
	
	for j in range(len(media)):
		#d = math.sqrt((puntos[i][0] - media[j][0])**2 + (puntos[i][1] - media[j][1])**2)
		x, y = int(media[j][0]), int(media[j][1])
		grisMedia = imagenEscalaGrises[y][x]
		d = math.fabs(nivelGrisPunto - grisMedia)
			
		if(d < distanciaMinima):
			distanciaMinima = d
			clase = j

	if(distanciaMinima >= umbral):
		
		conjunto.append([])
		conjunto[ctrl].append(i)
		media.append((puntos[i][0], puntos[i][1]))
		ctrl += 1

	else:
		# Calcular la nueva media.		
		conjunto[clase].append(i)
		

for i in range(len(conjunto)):
	print(conjunto[i])

graficador.figure('K centro agrupados')
graficador.title('Puntos con sus conjuntos')

print('media finales: ')

for i in range(len(media)):
	x = []
	y = []
	for j in range(len(conjunto[i])):
		indice = conjunto[i][j]
		punto = puntos[indice]
		x.append(punto[0])
		y.append(punto[1])
	
	graficador.plot(x, y, '^', label='media{}'.format(i + 1))
	

fondoImagen = graficador.imread(nombreImagen)
graficador.imshow(fondoImagen[::-1])

graficador.axis([minX, maxX, minY, maxY])
graficador.legend()
graficador.show()