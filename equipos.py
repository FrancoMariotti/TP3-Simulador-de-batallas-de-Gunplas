JUGADORES_POR_EQUIPO=3

class Equipo:
	"""Representa un equipo de jugadores"""
	
	def __init__(self,nombre):
		"""Inicializa un equipo vacio"""
		self.nombre=nombre
		self.integrantes=[]
	
	def get_nombre(self):
		"""Devuelve el nombre del equipo"""
		return self.nombre
	
	def get_integrantes(self):
		"""Devuelve una lista con los integrantes del equipo"""
		return self.integrantes
		
	def agregar_integrantes(self,jugadores):
		"""Recibe una lista de jugadores y los agrega al equipo."""
		self.integrantes+=jugadores
	
	def tiene_integrantes_con_vida(self):
		"""Deuvelve True si quedan jugadores en el equipo con gunplas
		 activos o False en caso contrario."""
		for integrante in self.integrantes:
			if(integrante.get_gunpla().esta_vivo()):
				return True
		return False
		
	def __str__(self):
		"""Devuelve una cadena(Representacion del objeto Equipo)."""
		nombres=[]
		for integrante in self.integrantes:
			nombres.append(integrante.get_nombre())
		return self.nombre + ": " +",".join(nombres)

def armar_equipos(cantidad_equipos,jugadores):
	"""Recibe la cantidad de equipos que se quiere crear y una lista de jugadores.
		Devuelve una lista con Equipos."""
	equipos =  [Equipo("Equipo"+str(i)) for i in range(1,cantidad_equipos+1)]
	contador=0
	for equipo in equipos:
		integrantes=jugadores[contador:contador+JUGADORES_POR_EQUIPO]
		for integrante in integrantes:
			integrante.set_equipo(equipo)
		equipo.agregar_integrantes(integrantes)
		contador+=JUGADORES_POR_EQUIPO
	return equipos



def cantidad_equipos_con_gunplas_activos(equipos):
	"""Recibe una lista de equipos. Devuelve la cantidad de equipos que 
	contiene jugadores con gunplas activos."""
	contador=0
	for equipo in equipos:
		if(equipo.tiene_integrantes_con_vida()):
			contador+=1
	return contador	

	
