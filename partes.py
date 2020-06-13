import random
from pila import Pila
from arma import agregar_armas_parte

CANTIDAD_PARTES=20

TIPOS_PARTE=("BACKPACK","BODY","HEAD","LEFT_ARM","RIGHT_ARM","LEGS")


class Parte:
	"""Representa una parte de un Gunpla."""

	def __init__(self,tipo):
		"""Inicializa una Parte random."""
		self.armas=[]
		self.slots =random.randint(1,5)
		self.tipo = tipo
		self.peso=random.randint(1,20)
		self.armadura=random.randint(0,10)
		self.escudo=random.randint(0,10)
		self.velocidad=random.randint(-2,10)
		self.energia=random.randint(2,20)
	
	def get_slots(self):
		"""Devuelve la cantidad de slots de la parte"""
		return self.slots	
	
	def get_armamento(self):
		"""Devuelve una lista con las armas adosadas a la parte"""
		return self.armas
	
	def get_tipo_parte(self):
		"""Devuelve una cadena que representa el tipo de parte"""
		return self.tipo
	
	def get_peso(self):
		"""Devuelve el peso total de la parte. Una parte pesa lo que 
		pesa la sumatoria de sus armas más el peso base de la parte"""
		return self.peso
	
	def get_armadura(self):
		"""Devuelve la armadura total de la parte. Una parte tiene 
		tanta armadura como la sumatoria de la armadura de sus armas 
		más la armadura base de la parte"""

		return self.armadura
	
	def get_escudo(self):
		"""Devuelve el escudo total de la parte. Una parte tiene tanto 
		escudo como la sumatoria del escudo de sus armas más el escudo
		 base de la parte"""
		return self.escudo
		
	def get_velocidad(self):
		"""Devuelve la velocidad de la parte"""
		return self.velocidad
	
	def get_energia(self):
		"""Devuelve la energía total de la parte. La parte tiene tanta 
		energía como la sumatoria de la energía de sus armas más la
		 energía base de la parte"""
		return self.energia
		
	def equipar_arma(self,arma):
		"""Equipa un arma a la parte. Lanza un ValueError si no hay mas 
		slots para seguir equipando armas."""
		if(self.slots==0):
			raise ValueError("Cantidad maxima armas por Parte alcanzada.")
		self.armas.append(arma)
		self.peso+= arma.get_peso()
		self.armadura+=arma.get_armadura()
		self.escudo+=arma.get_escudo()
		self.energia+= arma.get_energia()
		self.slots-=1
		

def generar_lista_partes():
	""""No recibe nada. Devuelve una lista de partes random"""
	partes={}
	for tipo_parte in TIPOS_PARTE:
		pila_tipo_parte = Pila()
		for _ in range(CANTIDAD_PARTES):
			parte = Parte(tipo_parte)
			agregar_armas_parte(parte)
			pila_tipo_parte.apilar(parte)
		partes[tipo_parte]= pila_tipo_parte
	return partes
	
	

	
