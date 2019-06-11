import numpy
from numpy.linalg import inv


#________________________________________________________#
def calcularCentroide(coordenadasX, coordenadasY):
	xC = 0
	yC = 0

	for k in range(len(coordenadasX)):
		xC += coordenadasX[k]
		yC += coordenadasY[k]

	xC /= len(coordenadasX)
	yC /= len(coordenadasY)

	return (xC, yC)

#________________________________________________________#

def calcularDistancia(x0, y0, x1, y1):
	d = ((x0 - x1)**2 + (y0 - y1)**2)**(1/2)
	return d


#________________________________________________________#
def calcularDistanciasEuclidianas(equis, ye, informacionClases):
	distancias = []
	
	for i in range(len(informacionClases)):
		d = calcularDistancia(equis, ye, informacionClases[i].xCentroide, informacionClases[i].yCentroide)
		distancias.append(d)

	return distancias
#________________________________________________________#
def calcularDistanciasMahalanobis(equis, ye, informacionClases):
	distancias = []


	for i in range(len(informacionClases)):
		
		coordX = informacionClases[i].coordenadasX
		coordY = informacionClases[i].coordenadasY
		
		n = len(coordY)

		xo = informacionClases[i].xCentroide
		yo = informacionClases[i].yCentroide
		
		mat = []
		fila = []
		

		for j in range(len(coordX)):
			fila.append((coordX[j] - xo))

		mat.append(fila)
		fila = []

		for j in range(len(coordY)):
			fila.append(coordY[j] - yo)

		mat.append(fila)

		mat = numpy.array(mat) #se pone numpy para que la biblioteca reconozca la matriz
		
		transpMat = mat.transpose()
		
		sigma = mat @ transpMat
		
		sigma = 1.0 / n * sigma

		inversa = inv(sigma)

		aux = [equis - xo , ye - yo]
		aux = numpy.array(aux)
		transpAux = aux.transpose()

		dist = aux @ inversa @ transpAux

		distancias.append(dist)

	return distancias