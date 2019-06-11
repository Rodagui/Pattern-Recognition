import numpy
import random
import matplotlib.pyplot as graficador

print('AND')
print('Wk = 1    r = 1')

r = 1

fsal = ([])
cambio = 1
matUno = numpy.array([[0,0,1]])
matDos = numpy.array([[0,1,1]])
matTres = numpy.array([[1,0,1]])
matCuatro = numpy.array([[1,1,1]])

w = numpy.array([ [1], [1], [1] ])

while(cambio != 0):
	
	cambio = 0
	
	fsal =  matUno.dot(w)
	if(fsal[0][0] >= 0):
		w = w - (r *matUno.transpose())
		#print('--------')
		#print(w)
		cambio = 1

	fsal =  matDos.dot(w)
	if(fsal[0][0] >= 0):
		w = w - (r *matDos.transpose())
		cambio = 1

	fsal =  matTres.dot(w)
	if(fsal[0][0] >= 0):
		w = w - (r * matTres.transpose())
		cambio = 1

	fsal =  matCuatro.dot(w)
	if(fsal[0][0] <= 0):
		w = w + (r*matCuatro.transpose())
		cambio = 1

cte1 = w[0][0]
cte2 = w[1][0]
cte3 = w[2][0]

print(w)
x = numpy.arange(-6, 6)
y = ((-cte1*x) -cte3) / cte2

graficador.plot(0, 0, 'o', label ='Punto 1 (0,0)')
graficador.plot(0, 1, 'o', label ='Punto 2 (0,1)')
graficador.plot(1, 0, 'o', label ='Punto 3 (1, 0)')
graficador.plot(1, 1, 'o', label ='Punto 4 (1,1)')

graficador.plot(x, y, label='({})x + ({})y +({})'.format(cte1, cte2, cte3))
graficador.axis([-5,5, -5, 5])
graficador.legend()
graficador.show()
