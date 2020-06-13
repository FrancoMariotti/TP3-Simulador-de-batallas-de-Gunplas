import time

from gunpla import *
from esqueleto import *
from partes import *
from arma import *
from piloto import *
from cola import *
from equipos import *
	
NOMBRE="GUMPLA"
FACTOR_ENERGIA_MAXIMA=0.05
PAUSA_PRINT=2

def ordenar_jugadores(jugadores):
	"""Recibe una lista de jugadores,devuelve una nueva lista con los 
		jugadores ordenados por su velocidad."""
	return sorted(jugadores,key=lambda jugador: jugador.get_gunpla().get_velocidad())

	
def armar_gunpla(partes,armas,jugador=None):
	"""Recibe una lista de partes, una de armas y un jugador. Arma el 
		gunpla asociado al jugador con las partes y armas recibidas. """
	gunpla = None
	if(jugador):
		gunpla = jugador.get_gunpla()	
	if(not gunpla):
		raise ValueError("Gunpla no asignado")
		
	while(partes):
		try:
			gunpla.equipar_parte(partes.pop())
		except ValueError as error:
			print(error.args)
	while(armas):
		try:
			gunpla.equipar_arma(armas.pop())
		except ValueError as error:
			print(error.args)
	

def hay_partes(partes):
	"""Recibe un diccionario con partes. Devuelve True si quedan partes 
	en el diccionario o False en caso contrario."""
	for pila_parte in partes.values():
		if(not pila_parte.esta_vacia()):
			return True
	return False

def eleccion_de_partes(lista_partes,jugadores):
	"""Recibe una diccionario de partes ({tipo_parte:parte}) y una lista 
	de jugadores.Devuelve un diccionario con las partes reservadas 
	por cada jugador."""
	
	lista_partes_reservadas_por_jugador={jugador.get_nombre():[] for jugador in jugadores}
	while(hay_partes(lista_partes)):
		for jugador in jugadores:
			parte = jugador.elegir_parte(lista_partes)
			if(not lista_partes[parte].esta_vacia()):
				lista_partes_reservadas_por_jugador[jugador.get_nombre()].append(lista_partes[parte].desapilar())
		
	return lista_partes_reservadas_por_jugador

def inicializar_turnos(jugadores):
	"""Recibe un lista de jugadores y devuelve una cola con los 
		jugadores."""
	turnos = Cola()
	for jugador in jugadores:
		turnos.encolar(jugador)
	return turnos
	
def buscar_oponentes(equipos,jugador):
	"""Recibe una lista de equipos y un jugadores. Devuelve una lista 
	con los oponentes del jugador."""
	oponentes=[]
	for equipo in equipos:
		if equipo != jugador.get_equipo():
			oponentes+=equipo.get_integrantes()
		
	return oponentes

def determinar_ganador(equipos):
	"""Recibe una lista de equipos y devuelve el equipo que contien 
		gunplas activos de la lista de equipos recibida."""
	for equipo in equipos:
		if(equipo.tiene_integrantes_con_vida()):
			return equipo


def ciclo_de_juego(equipos,turnos):
	
	while(cantidad_equipos_con_gunplas_activos(equipos)>=2):

		jugador = turnos.desencolar()
		
		gunpla_jugador =jugador.get_gunpla()
		
		#se saltea el turno si el gunpla del jugador no esta activo.
		if(gunpla_jugador.get_energia_restante()<=0):
			continue
		
		gunpla_jugador.recargar_armas()	
			
		oponentes = buscar_oponentes(equipos,jugador)
		
		oponente = jugador.elegir_oponente(oponentes)
		
		arma=jugador.elegir_arma(oponente)
		
		#si el jugador no tiene armas disponibles para atacar, pierde el turno.
		if(not arma):
			print("{} no tiene armas disponibles y pierde su turno...".format(jugador.get_nombre()))
			time.sleep(PAUSA_PRINT)
			turnos.encolar(jugador)
			continue
		
		print("{} ataca a {}".format(jugador.get_gunpla().get_nombre(),oponente.get_gunpla().get_nombre()))
		danio = gunpla_jugador.atacar(oponente.get_gunpla(),arma)
		print("Danio:{:.2f}".format(danio))
		time.sleep(PAUSA_PRINT)
		
		if(danio == 0):
			turnos.encolar(oponente)
		elif(gunpla_jugador.get_energia_restante()<0 and 
			abs(gunpla_jugador.get_energia_restante()) > gunpla.get_energia() * FACTOR_ENERGIA_MAXIMA):
			turnos.encolar(jugador)
		
		turnos.encolar(jugador)
	
	print("Equipo GANADOR:\n",determinar_ganador(equipos))
		

def main():
	
	cantidad_equipos = int(input("Ingrese cantidad de Equipos:"))
	
	jugadores = crear_pilotos(JUGADORES_POR_EQUIPO*cantidad_equipos)
	equipos = armar_equipos(cantidad_equipos,jugadores)	
	
	partes_disponibles = generar_lista_partes() 
	armas_disponibles = generar_lista_armas()
	
	random.shuffle(jugadores)
	
	partes_por_jugador = eleccion_de_partes(partes_disponibles,jugadores)
	armas_por_jugador = eleccion_de_partes(armas_disponibles,jugadores)
	
	lista_esqueletos= crear_lista_de_esqueletos()

	for i,jugador in enumerate(jugadores):
		partes_seleccionadas = jugador.elegir_combinacion(partes_por_jugador[jugador.get_nombre()])
		armas_seleccionadas = jugador.elegir_combinacion(armas_por_jugador[jugador.get_nombre()])
		esqueleto = jugador.elegir_esqueleto(lista_esqueletos)
		jugador.set_gunpla(Gunpla(NOMBRE+str(i),lista_esqueletos[esqueleto]))
		armar_gunpla(partes_seleccionadas,armas_seleccionadas,jugador)
	
	jugadores = ordenar_jugadores(jugadores)
	turnos = inicializar_turnos(jugadores)
	ciclo_de_juego(equipos,turnos)
	
	
		
main()
		
		

	
		
		
	

	
			
