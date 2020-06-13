import random
from pila import Pila

CANTIDAD_DE_ARMAS=30
MAXIMA_PRECISION=100
MINIMA_PRECISION=0

CLASES_ARMA = ("GN Beam Rifle","GN Buster Rifle", "GN Cannon","GN Pistol","GN Sword","GN Lance")

class Arma:
	"""Representa un Arma"""
	
	MELEE="MELEE"
	RANGO="RANGO"
	MUNICION_FISICA="FISICA"
	MUNICION_LASER="LASER"
	MUNICION_HADRON="HADRON"
	
	def __init__(self,clase,tipo,tipo_de_municion):
		"""Inicializa un arma random."""
		self.peso = random.randint(1,20)
		self.armadura = random.randint(-13,13)
		self.escudo = random.randint(-13,13)
		self.energia = random.randint(-10,25)
		self.tipo=tipo
		self.tipo_de_municion = tipo_de_municion
		self.clase = clase
		self.danio = random.randint(10,40)
		self.hits = random.randint(1,3)
		self.precision = random.randint(MINIMA_PRECISION,MAXIMA_PRECISION)
		self.tiempo_de_recarga = random.randint(1,4)
		self.disponible = True
		self.cantidad_de_recargas_faltantes=0
	
	def get_clase(self):
		"""Devuelve la clase del arma"""
		return self.clase
	
	def get_precision(self):
		"""Devuelve la precision del arma"""
		return self.precision

	def get_peso(self):
		"""Devuelve el peso del arma"""
		return self.peso
		
	def get_armadura(self):
		"""Devuelve la armadura del arma"""
		return self.armadura
	
	def get_escudo(self):
		"""Devuelve el escudo del arma"""
		return self.escudo
		
	def get_energia(self):
		"""Devuelve la energía del arma"""
		return self.energia
		
	def get_tipo(self):
		"""Devuelve el tipo del arma"""
		return self.tipo
		
	def get_tipo_de_municion(self):
		"""Devuelve el tipo de munición del arma"""
		return self.tipo_de_municion
	
	def get_danio(self):
		"""Devuelve el daño de un ataque del arma"""
		return self.danio
		
	def get_hits(self):
		"""Devuelve la cantidad de veces que puede atacar un arma 
		en un turno"""
		return self.hits
		
	def get_tipo_parte(self):
		"""Devuelve el tipo de parte de un arma"""
		return "Arma"
		
	def utilizar(self):
		"""Utiliza el arma asignando el tiempo de recarga.Luego el arma 
		no podra volver a ser utilizada hasta que se recargue y vuelva 
		a estar disponible."""
		self.disponible= False
		self.cantidad_de_recargas_faltantes= self.tiempo_de_recarga
		
	def esta_lista(self):
		"""Devuelve la disponibilidad del arma"""
		return self.disponible
		
	def recargar(self):
		"""Disminuye el tiempo de recarga, al llegar a cero el arma 
		vuelve a estar disponible"""
		if(self.disponible):
            return
        self.cantidad_de_recargas_faltantes-=1
        if(self.cantidad_de_recargas_faltantes<=0):
            self.disponible=True

def agregar_armas_parte(parte):
	"""Recibe un parte y la quipa con armas."""
	tipos_arma=(Arma.MELEE,Arma.RANGO)	
	tipos_municion=(Arma.MUNICION_FISICA,Arma.MUNICION_HADRON,Arma.MUNICION_LASER)
	for _ in range(parte.get_slots()):
		arma = Arma(random.choice(CLASES_ARMA),random.choice(tipos_arma),random.choice(tipos_municion))
		parte.equipar_arma(arma)
	
		
def generar_lista_armas():
	"""Devuelve una lista de armas random."""
	armas={}
	
	tipos_arma=(Arma.MELEE,Arma.RANGO)
	tipos_municion=(Arma.MUNICION_FISICA,Arma.MUNICION_HADRON,Arma.MUNICION_LASER)
	for tipo_arma in tipos_arma:
		pila_tipo_arma=Pila()
		for _ in range(CANTIDAD_DE_ARMAS):
			pila_tipo_arma.apilar(Arma(random.choice(CLASES_ARMA),tipo_arma,random.choice(tipos_municion)))
		armas[tipo_arma]=pila_tipo_arma
	return armas
	
