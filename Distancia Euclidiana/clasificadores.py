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
def calcularDistanciasEuclidianas(equis, ye, centroides):
	distancias = []
	
	for i in range(len(centroides)):
		d = calcularDistancia(equis, ye, centroides[i][0], centroides[i][1])
		distancias.append(d)

	return distancias