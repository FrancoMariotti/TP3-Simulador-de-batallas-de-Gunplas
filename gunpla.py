
import random
from arma import Arma , MAXIMA_PRECISION
from esqueleto import Esqueleto

PROBABILIDAD_INICIO=0
PROBABILIDAD_FINAL=1
FACTOR_DANIO=1.5
PROBABILIDAD_MELEE=0.40
PROBABILIDAD_RANGO=0.25


class Gunpla():
	"""Representa un Gunpla"""
	
	def __init__(self,nombre,esqueleto):
		"""Inicializa un gunpla con su esqueleto. Lanza TypeError si el 
		esqueleto recibido no es una intancia de la Clase Esqueleto"""
		self.nombre=nombre
		if(not esqueleto or not isinstance(esqueleto, Esqueleto)):
			raise TypeError("El parametro recibido no es del tipo esperado")
		self.esqueleto = esqueleto
		self.equipo = None
		self.armas=[]
		self.armas_descargadas=[]
		self.partes={}
		self.peso=0
		self.velocidad = esqueleto.get_velocidad()
		self.armadura=0
		self.escudo=0
		self.energia = esqueleto.get_energia()
		self.energia_restante=esqueleto.get_energia()
		
	def get_nombre(self):
		return self.nombre
		
	def get_peso(self):
		"""Devuelve el peso total del Gunpla. Un Gunpla pesa 
		lo que pesa la sumatoria de sus partes y armas"""
		return self.peso
	
	def get_equipo(self):
		return self.equipo
		
	def get_armadura(self):
		"""Devuelve la armadura total del Gunpla. Un Gunpla tiene 
		tanta armadura como la sumatoria de la armadura de sus partes 
		y armas"""
		return self.armadura
		
	def get_escudo(self):
		"""Devuelve el escudo total del Gunpla. Un Gunpla tiene tanto 
		escudo como la sumatoria del escudo de sus partes y armas"""
		return self.escudo
	
	def get_velocidad(self):
		"""Devuelve la velocidad total del Gunpla. Un Gunpla tiene 
		tanta velocidad como la sumatoria de las velocidades de sus 
		partes y esqueleto"""
		return self.velocidad
		
	def get_energia(self):
		"""Devuelve la energía total del Gunpla. Un Gunpla tiene tanta 
		energía como la sumatoria de la energía de sus partes, armas y
		 esqueleto"""
		return self.energia
	
	def get_energia_restante(self):
		"""Devuelve la energía que le resta al Gunpla"""
		return self.energia_restante
	
	def get_movilidad(self):
		"""Devuelve la movilidad de un Gunpla. Se calcula según la 
		fórmula descripta en la seccion de fórmulas"""
		movilidad = ((self.esqueleto.get_movilidad() - self.peso)/2 + self.velocidad * 3) / self.esqueleto.get_movilidad()
		if(movilidad >1):
			return 1
		elif(movilidad<0):
			return 0
		return movilidad
	
	def set_equipo(self,equipo):
		"""Asigna el equipo del gunpla con el recibido."""
		self.equipo = equipo	
	
	def get_armamento(self):
		"""Devuelve una lista con todas las armas adosadas al Gunpla 
		(Se incluyen las armas disponibles en las partes)"""		
		armamento_gunpla = [arma for arma in self.armas]
		for parte_gunpla in self.partes.values():
			armamento_gunpla += parte_gunpla.get_armamento()
		return armamento_gunpla
	
	def esta_vivo(self):
		"""Devuelve True si el gunlpa contiene energia restante mayor a cero,
		 o False en caso contrario"""
		return self.energia_restante > 0
	
	def __buscar_armas_combinables(self,arma_elegida):
		"""Recibe el arma elegida para atacar y devuelve una lista con 
		las armas con las que podria combinarse el arma recibida."""
		
		armas_combinables=[]
		for arma in self.armas:
			if(arma_elegida == arma):
				continue
			if(arma.esta_lista() and arma.get_tipo()==arma_elegida.get_tipo() 
			and arma.get_tipo_de_municion() == arma_elegida.get_tipo_de_municion() and arma.get_clase() == arma_elegida.get_clase()):
				armas_combinables.append(arma)
		return armas_combinables
		
	def __calcular_danio(self,arma_elegida,armas_combinables=[]):
		"""Recibe el arma_elegida para atacar, calcula el danio total que se le realiza, sumando 
		los danios en caso de poder realizar alguna combinacion con otra arma combinable.
		Devuelve el danio total calculado."""
		
		danio_reducido=0
		
		probabilidad = arma_elegida.get_precision()/MAXIMA_PRECISION
		
		if(random.uniform(PROBABILIDAD_INICIO,PROBABILIDAD_FINAL)<=probabilidad):
			danio_reducido+=arma_elegida.get_danio()
			probabilidad = (arma_elegida.get_precision()*25)/(MAXIMA_PRECISION*25)
			if(random.uniform(PROBABILIDAD_INICIO,PROBABILIDAD_FINAL)<=probabilidad):
				danio_reducido*=FACTOR_DANIO
			if(armas_combinables):
				arma_combinable = armas_combinables.pop()
				tipo = arma_combinable.get_tipo()
				probabilidad = 0
				if(tipo == Arma.MELEE):
					probabilidad = PROBABILIDAD_MELEE
				else:
					probabilidad = PROBABILIDAD_RANGO
                        
				if(random.uniform(PROBABILIDAD_INICIO,PROBABILIDAD_FINAL) <= probabilidad):
					arma_combinable.utilizar()
					self.armas_descargadas.append(arma_combinable)
					return danio_reducido + self.__calcular_danio(arma_combinable,armas_combinables,danio_reducido)
				
		return danio_reducido
	
	
	def equipar_parte(self,parte):
		"""Recibe una parte y se la equipa al gunpla.Lanza ValueError 
		si el gunpla ya contiene el tipo de parte que se quiere equipar."""
				
		if(self.partes.get(parte.get_tipo_parte(),None)):
			raise ValueError("El gunpla ya contiene esta parte adherida.")
			
		self.peso+= parte.get_peso()
		self.armadura+=parte.get_armadura()
		self.escudo+=parte.get_escudo()
		self.velocidad+=parte.get_velocidad()
		self.energia+=parte.get_energia()
		self.partes[parte.get_tipo_parte()] = parte
		
		
	def equipar_arma(self,arma):
		"""Recibe un arma y se la agrega a las armas del gunpla. Lanza ValueError 
		si se alcanzo el numero maximo de armas que pueden equiparse al gunpla."""
		
		if(self.esqueleto.get_cantidad_slots()==0):
			raise ValueError("Cantidad maxima armas por Gunpla alcanzada.")
			
		self.armas.append(arma)
		self.armadura+=arma.get_armadura()
		self.peso += arma.get_peso()
		self.escudo+=arma.get_escudo()
		self.energia+=arma.get_energia()
		self.esqueleto.set_slots(self.esqueleto.get_cantidad_slots()-1)
		
	def __defender(self,danio,arma):
		"""Recibe el danio recibio en el ataque y lo reduce dependiendo de la armadura 
		o escudo que tenga el gunpla. Devuelve el danio reducido."""
		if(arma.get_tipo_de_municion()==Arma.MUNICION_FISICA):
			return danio - self.armadura
		elif(arma.get_tipo_de_municion()==Arma.MUNICION_LASER):
			return danio - danio * (self.escudo/100)
		return danio
		
				
	def atacar(self,gunpla_oponente,arma_elegida):
		"""Recibe un gunpla rival y el arma elegida. Ataca al gunpla enemigo 
		y devuelve el danio causado al gunpla rival."""
		armas_combinables = self.__buscar_armas_combinables(arma_elegida)
		danio_causado=0 
		for i in range(arma_elegida.get_hits()):
			arma_elegida.utilizar()
			danio = self.__calcular_danio(arma_elegida,armas_combinables)
			danio_causado += gunpla_oponente.recibir_ataque(danio,arma_elegida)
		self.armas_descargadas.append(arma_elegida)
		
		return danio_causado
			
	def recibir_ataque(self,danio_recibido,arma):
		"""Recibe el danio_recibido del ataque y el arma con la que el gunpla fue atacado, 
		reduce el danio dependiendo de el escudos y armadura equipados. Devuelve el danio causado"""
		danio = self.__defender(danio_recibido,arma)
		self.energia_restante-=danio
		return danio
		
	def recargar_armas(self):
		"""Recarga las armas que se encunetran descargadas"""
		for arma in self.armas_descargadas:
			arma.recargar()
			if(arma.esta_lista()):
				self.armas_descargadas.remove(arma)
		
		
		
		


		
