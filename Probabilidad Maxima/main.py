import random
from Clase import *
import matplotlib.pyplot as graficador

#________________________________________________________#
def generarPunto(rangoEquis, rangoYes, dispersion):
	x = (random.randint(rangoEquis[0], rangoEquis[1]) * dispersion) 
	y = (random.randint(rangoYes[0], rangoYes[1]) * dispersion)
	return (x, y)
#________________________________________________________#


numClase = int(input('Cuántas clases se leerán? '))

minx = 2**32
maxx = -2**32
miny = 2**32
maxy = -2**32
distanciaMin = 2**32
probabilidadMaxima = -2**31
claseP = -1

informacionClase = []

for j in range(numClase):
	numPuntos = int(input('Cuántos puntos tendrá la clase? '))

	rangoEquis = []
	rangoEquis.append(int(input('Ingrese el inicio de las x: \n')))
	rangoEquis.append(int(input('Ingrese el final de las x: \n')))

	rangoYes = []
	rangoYes.append(int(input('Ingrese el inicio de las y: \n')))
	rangoYes.append(int(input('Ingrese el final de las y: \n')))

	dispersion = int(input('Dispersion: '))

	# Coordenadas x, y son los arreglos en donde se guardan los puntos de la clase actual.
	coordenadasX = []
	coordenadasY = []

	for i in range(numPuntos):
		x, y = generarPunto(rangoEquis, rangoYes, dispersion)

		if(x < minx):
			minx = x

		if(x > maxx):
			maxx = x

		if(y < miny):
			miny = y

		if(y > maxy):
			maxy = y

		coordenadasX.append(x)
		coordenadasY.append(y)

	nuevaClase = Clase('Clase {}'.format(j + 1), coordenadasX, coordenadasY)
	informacionClase.append(nuevaClase)

	graficador.plot(coordenadasX, coordenadasY, 'o', label='Clase {}'.format(j + 1))
											#    ^ para triángulo
	graficador.plot([nuevaClase.xCentroide], [nuevaClase.yCentroide], 's', label='Centroide de Clase {}'.format(j + 1))
	graficador.legend()

graficador.axis([minx - 50, maxx + 50, miny - 50, maxy + 50])

print('Ingrese la coordenada a evaluar')

equis = int(input('x: '))
ye = int(input('y: '))

if (equis < minx):
	minx = equis
if (equis > maxx):
	maxx = equis

if (ye < miny):
	miny = ye
if (ye > maxx):
	maxy = ye

graficador.plot([equis], [ye], '^', label='Punto a evaluar')
graficador.legend()

print('{} {}'.format(equis, ye))

distancias = []
sigma = []
dist = []


print('1. Distancia Euclidiana')
print('2. Distancia Mahalanobis')
print('3. Probabilidad Maxima')

opcion = input('opcion: ')

if (opcion == '1'):
	distancias = calcularDistanciasEuclidianas(equis, ye, informacionClase)
if(opcion == '2'):
	distancias = calcularDistanciasMahalanobis(equis, ye, informacionClase, opcion)
if(opcion == '3'):
	dist, sigma = calcularDistanciasMahalanobis(equis, ye, informacionClase, opcion)
	distancias = calcularMaximaProbabilidad(dist, sigma, informacionClase)

print('\n\n');

if(opcion == '3'):

	for i in range(len(distancias)):
		d = distancias[i]
		print('La probabilidad con la clase %d y el punto es %.6f%%'%(i + 1, d))
		
		if(d > probabilidadMaxima):
			probabilidadMaxima = d
			claseP = i + 1
else:
	for i in range(len(distancias)):
		d = distancias[i]
		print('La distancia con la clase %d y el punto es %.6f'%(i + 1, d))
		if(d < distanciaMin):
			distanciaMin = d
			claseP = i + 1

print('El punto pertenece a la clase {}'.format(claseP))

graficador.show()
