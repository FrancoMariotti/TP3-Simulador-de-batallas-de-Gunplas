import random

CANTIDAD_ESQUELETOS=10
	
class Esqueleto:
	"""Representa el esqueleto interno del Gunpla."""
	
	def __init__(self):
		"""Inicializa el Esqueleto"""
		self.velocidad = random.randint(10,50)
		self.energia = random.randint(0,20)
		self.slots =random.randint(1,5)
		self.movilidad = random.randint(100,200)
		
	def set_slots(self,slots):
		"""Asigna los slots al Esqueleto"""
		self.slots = slots
	def get_velocidad(self):
		"""Devuelve la velocidad del esqueleto"""
		return self.velocidad
	def get_energia(self):
		"""Devuelve la energía del esqueleto"""
		return self.energia
	def get_movilidad(self):
		"""Devuelve la movilidad del esqueleto"""
		return self.movilidad
	def get_cantidad_slots(self):
		"""Devuelve la cantidad de slots (ranuras) para 
		armas que tiene el esqueleto"""
		return self.slots


def crear_lista_de_esqueletos():
	"""Crea un lista con Esqueletos y la devuelve."""
	return [Esqueleto() for _ in  range(CANTIDAD_ESQUELETOS)]
