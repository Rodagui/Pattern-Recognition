from Clase import *
from scipy.cluster import hierarchy
import matplotlib.pyplot as graficador
from PIL import Image
#pip install Pillow

def printTabla(tabla):
	for i in range(len(tabla)):
		for j in range(len(tabla[i])):
			print("%3.3f, "%tabla[i][j], end='')
		print('')

minx = 2**32
maxx = -2**32
miny = 2**32
maxy = -2**32
distanciaMin = 2**32
claseP = -1
informacionClase = []

numClase = 20


grupos = []


for j in range(numClase):
	rangoEquis = []
	rangoEquis.append(-1000)
	rangoEquis.append(1000)

	rangoYes = []
	rangoYes.append(-1000)
	rangoYes.append(1000)


	x, y = generarPunto(rangoEquis, rangoYes, 1)

	if(x < minx):
		minx = x

	if(x > maxx):
		maxx = x

	if(y < miny):
		miny = y

	if(y > maxy):
		maxy = y

	grupos.append([x, y])

	graficador.plot([x], [y], 'o', label='Clase {}'.format(j + 1))
											#    ^ para triángulo
	graficador.legend()

graficador.axis([minx - 50, maxx + 50, miny - 50, maxy + 50])

#grupos = [[0, 0], [0, 4], [1, 0], [3, 0], [1, 3]]

for j in range(len(grupos)):
	x = grupos[j][0]
	y = grupos[j][1]

	if(x < minx):
		minx = x

	if(x > maxx):
		maxx = x

	if(y < miny):
		miny = y

	if(y > maxy):
		maxy = y
	graficador.plot([x], [y], 'o', label='Clase {}'.format(j + 1))
											#    ^ para triángulo
	graficador.legend()

graficador.axis([minx - 5, maxx + 5, miny - 5, maxy + 5])

ytdist = numpy.array(grupos)
Z = hierarchy.linkage(ytdist, 'single')
graficador.figure()
dn = hierarchy.dendrogram(Z)


tablaDist = []

for i in range(len(grupos)):
	distancia = []
	for j in range(len(grupos)):
		if i == j:
			distancia.append(0)
		else:
			distancia.append(calcularDistancia(grupos[i][0], grupos[i][1], grupos[j][0], grupos[j][1]))

	tablaDist.append(distancia)


eliminados = []

for i in range(3 * len(grupos)):
	eliminados.append(False)

activos = len(grupos)

while activos > 1:
	minGrupos = [-1, -1]
	minDistancia = float(2.0**64.0)

	for i in range(len(tablaDist)):
		if not eliminados[i]:	
			for j in range(len(tablaDist)):
				if i != j and not eliminados[j]:
					if tablaDist[i][j] < minDistancia:
						minDistancia = tablaDist[i][j]
						minGrupos = [i, j]

	activos = activos - 1
	print("El grupo %3d se unio con el grupo %3d con una distancia de %3.5f"%(minGrupos[0] + 1, minGrupos[1] + 1, minDistancia))
	eliminados[minGrupos[0]] = True
	eliminados[minGrupos[1]] = True

	for i in range(len(tablaDist)):
		tablaDist[i].append(min(tablaDist[i][minGrupos[0]], tablaDist[i][minGrupos[1]]))


	nuevaFila = []
	for i in range(len(tablaDist)):
		if i == minGrupos[0] or i == minGrupos[1]:
			nuevaFila.append(0.0)
		else:
			nuevaFila.append(min(tablaDist[minGrupos[0]][i], tablaDist[minGrupos[1]][i]))

	nuevaFila.append(0.0)

	tablaDist.append(nuevaFila)

graficador.show()