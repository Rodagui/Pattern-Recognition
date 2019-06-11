import numpy
from numpy.linalg import inv

mat = numpy.array([
	[1,2,3],
	[3,2,1],
	[2,1,3]
])

inversa = inv(mat)

print(mat)
print(mat.transpose())
print(inv(mat) @ mat)


mat = numpy.array(mat) #se pone numpy para que la biblioteca reconozca la matriz
mat = mat @ mat.transpose()

mat = 1/n * mat


