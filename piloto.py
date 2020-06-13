

import random

from arma import Arma

JUGADOR="JUGADOR"


class Piloto:
	
	""" Representa una inteligencia artificial para controlar un Gunpla."""
	def __init__(self):
		"""Crea un piloto y no recibe ningun parámetro"""
		self.nombre=""
		self.equipo=None
		self.gunpla=None
	
	def set_equipo(self,equipo):
		"""Asgina un equipo al piloto"""
		self.equipo = equipo

	def set_nombre(self,nombre):
		"""Asgina un nombre al piloto"""
		self.nombre = nombre
	
	def get_equipo(self):
		"""Devuelve el equipo del piloto"""
		return self.equipo
		
	def get_nombre(self):
		"""Devuelve el nombre del piloto"""
		return self.nombre
	
	def get_gunpla(self):
		"""Devuelve el Gunpla asociado al piloto"""
		return self.gunpla
		
	def set_gunpla(self,gunpla):
		"""Asigna un Gunpla a un piloto"""
		self.gunpla = gunpla
			
	def elegir_esqueleto(self,lista_esqueletos):
		"""Dada una lista con esqueletos, devuelve el índice del
		 esqueleto a utilizar"""

		if(len(lista_esqueletos)==0):
			raise ValueError("La lista de esqueletos vacia.")
			
		return random.choice(range(len(lista_esqueletos)))
		
	def elegir_parte(self,partes_disponibles):
		"""Dado un diccionario: {tipo_parte:parte}, devuelve el tipo de 
		parte que quiere elegir. Este metodo se utiliza para ir eligiendo 
		de a una las partes que se van a reservar para cada piloto, de 
		entre las cuales va a poder elegir para armar su modelo"""
		return random.choice(list(partes_disponibles))
	
	def elegir_combinacion(self,partes_reservadas):
		"""Dada una lista con partes previamente reservadas, devuelve 
		una lista con las partes a utilizar para construir el Gunpla. 
		Este metodo se utiliza para elegir las partes que se van a utilizar 
		en el modelo de entre las que se reservaron previamente para cada 
		piloto."""
		combinacion=dict()
		for parte in partes_reservadas:
			if(parte.get_tipo_parte() not in combinacion):
				combinacion[parte.get_tipo_parte()] = parte
		return list(combinacion.values())
		
	def elegir_oponente(self,oponentes):
		"""Devuelve el índice del Gunpla al cual se decide atacar de la 
		lista de oponentes pasada"""
		return random.choice(oponentes)
	
	def elegir_arma(self,oponente):
		"""Devuelve el arma con la cual se decide atacar al oponente"""
		gunpla = oponente.get_gunpla()
		arma_hadron=None
		
		armamento_gunpla = self.gunpla.get_armamento()
		
		armas_hadron = [arma for arma in armamento_gunpla if arma.esta_lista() and arma.get_tipo_de_municion()==Arma.MUNICION_HADRON]  
		armas_fisica = [arma for arma in armamento_gunpla if arma.esta_lista() and arma.get_tipo_de_municion()==Arma.MUNICION_FISICA]
		armas_laser = [arma for arma in armamento_gunpla if arma.esta_lista() and arma.get_tipo_de_municion()==Arma.MUNICION_LASER]  
		
		if(armas_hadron):
			for arma in armas_hadron:
				if(armas_hadron):
					armas_hadron = arma
				elif(arma.get_danio()>armas_hadron.get_danio()):
					armas_hadron = arma
		if(not arma_hadron):
			
			arma_laser = None
			arma_fisica =None
			
			if(armas_laser):
				for arma in armas_laser:
					if(not arma_laser):
						arma_laser = arma
					elif(arma.get_danio()>arma_laser.get_danio()):
						arma_laser = arma
			
			
					
			if(arma_fisica):
				for arma in armas_fisica:
					if(not arma_fisica):
						arma_fisica = arma
					elif(arma.get_danio()>arma_fisica.get_danio()):
						arma_fisica = arma
			
			if(arma_laser and gunpla.get_armadura()>gunpla.get_escudo()):
				return arma_laser			
			else:
				return arma_fisica
				
		return arma_hadron
		
def crear_pilotos(cantidad_pilotos):
	"""Recibe la cantidad de pilotos que se quiere crear y devuelve una 
		lista con los Pilotos creados."""
	pilotos=[]
	for i in range(1,cantidad_pilotos+1):
		piloto = Piloto()
		piloto.set_nombre(JUGADOR+str(i))
		pilotos.append(piloto)
	return pilotos
