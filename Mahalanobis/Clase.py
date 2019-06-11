from clasificadores import *

class Clase:
	def __init__(self, nombre, coordenadasX, coordenadasY):
		self.nombre = nombre
		self.coordenadasY = coordenadasY
		self.coordenadasX = coordenadasX
		self.xCentroide, self.yCentroide = calcularCentroide(coordenadasX, coordenadasY)