import random
from clasificadores import *
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
claseP = -1

centroides = []

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

	xCentroide, yCentroide = calcularCentroide(coordenadasX, coordenadasY)
	centroides.append((xCentroide, yCentroide))

	graficador.plot(coordenadasX, coordenadasY, 'o', label='Clase {}'.format(j + 1))
											#    ^ para triángulo
	graficador.plot([xCentroide], [yCentroide], 's', label='Centroide de Clase {}'.format(j + 1))
	graficador.legend()

graficador.axis([minx - 50, maxx + 50, miny - 50, maxy + 50])

print('Ingrese la coordenada a evaluar')

equis = int(input('x: '))
ye = int(input('y: '))

graficador.plot([equis], [ye], '^', label='Punto a evaluar')
graficador.legend()

print('{} {}'.format(equis, ye))

distaciasEuclidianas = calcularDistanciasEuclidianas(equis, ye, centroides)

for i in range(len(distaciasEuclidianas)):
	d = distaciasEuclidianas[i]
	print('La distancia con la clase {} y el punto es {}'.format(i + 1, d))
	if(d < distanciaMin):
		distanciaMin = d
		claseP = i + 1

print('El punto pertenece a la clase {}'.format(claseP))

graficador.show()