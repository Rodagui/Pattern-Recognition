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
			nivelGris = int(imagen[i, j])
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

cantidadMuestras = int(input('Número de muestras: '))

for i in range(cantidadMuestras):
	x = random.randint(minX, maxX - 1)
	y = random.randint(minY, maxY - 1)

	xPuntos.append(x)
	yPuntos.append(y)
	puntos.append((x, y))

graficador.figure('Muestras')
graficador.title('Conjunto de puntos')
graficador.axis([minX, maxX, minY, maxY])
graficador.plot(xPuntos, yPuntos, 'o')


centros = []
K = int(input('Centroides: '))
print('Centros iniciales: ')

# Primera iteración en la que se igualan a los primeros K puntos aleatorios.
for i in range(K):
	x = random.randint(minX, maxX - 1)
	y = random.randint(minY, maxY - 1)
	centros.append((x, y))
	
	print('{}'.format(centros[i]))
	graficador.plot(centros[i][0], centros[i][1], '^', label='Centro{}'.format(i + 1))

graficador.legend()


print('-------------------------')

clase = 0
badera = 0
iteracionActual = 0

conjunto = []
conjuntoAnterior = []

while badera == 0 and iteracionActual < 100000:
	iteracionActual = iteracionActual + 1
	
	conjunto.clear()

	conjunto = [[] for i in range(K)] # Lista de tamaño k de arreglos vacios.

	for i in range(cantidadMuestras):	
		distanciaMinima = 2 ** 32
		x, y = puntos[i][0], puntos[i][1]
		nivelGrisPunto = imagenEscalaGrises[y][x]


		for j in range(K):
			x, y = int(centros[j][0]), int(centros[j][1])
			nivelGrisCentroide = imagenEscalaGrises[y][x]
			distanciaActual = math.fabs(nivelGrisPunto - nivelGrisCentroide)
			
			if(distanciaActual < distanciaMinima):
				distanciaMinima = distanciaActual
				clase = j

		conjunto[clase].append(i)

	# Calcular los nuevos centros.
	for i in range(K):
			
		totalX = 0
		totalY = 0
		cuantas = len(conjunto[i])
			
		if cuantas != 0:
			for j in range(cuantas):
				p = conjunto[i][j]
				totalX += puntos[p][0]
				totalY += puntos[p][1]

			totalX /= cuantas
			totalY /= cuantas

			centros[i] = (totalX, totalY)
		else:
			x = random.randint(minX, maxX - 1)
			y = random.randint(minY, maxY - 1)
			centros[i] = (x, y)

	if conjuntoAnterior == conjunto:
		badera = 1
	else:
		conjuntoAnterior = conjunto.copy()

graficador.figure('K centro agrupados')
graficador.title('Puntos con sus conjuntos')

print('Centros finales: ')

for i in range(K):

	xConjunto = []
	yConjunto = []

	for indicePunto in conjunto[i]:
		xConjunto.append(puntos[indicePunto][0])
		yConjunto.append(puntos[indicePunto][1])

	graficador.plot(xConjunto, yConjunto, 'o', label='Conjunto {}'.format(i + 1))

	print('{} {}'.format(i + 1, centros[i]))
	graficador.plot(centros[i][0], centros[i][1], '^', label='Z{}'.format(i + 1))
	

fondoImagen = graficador.imread(nombreImagen)
graficador.imshow(fondoImagen[::-1])

graficador.axis([minX, maxX, minY, maxY])
graficador.legend()
graficador.show()