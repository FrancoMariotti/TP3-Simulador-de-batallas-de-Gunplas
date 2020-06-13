class _Nodo():
	"""Representa un nodo de Lista Enlazada"""

	def __init__(self,dato=None,prox=None):
		self.dato=dato
		self.prox=prox

	def __str__(self):
		return self.dato

class Cola():

	def __init__(self):
		""" Crea una cola vacía. """
		# En el primer momento, tanto el primero como el último son None
		self.primero = None
		self.ultimo = None

	def encolar(self, x):
		""" Agrega el elemento x como último de la cola. """
		nuevo = _Nodo(x)
		# Si ya hay un último, agrega el nuevo y cambia la referencia.
		if self.ultimo:
			self.ultimo.prox = nuevo
			self.ultimo = nuevo
		# Si la cola estaba vacía, el primero es también el último.
		else:
			self.primero = nuevo
			self.ultimo = nuevo

	def desencolar(self):
		""" Elimina el primer elemento de la cola y devuelve su
        valor. Si la cola está vacía, levanta ValueError. """
		# Si hay un nodo para desencolar

		#Gaston: Again (o antes, este lo lei ultimo), con la condicion invertida
		#		 te ahorras el else y queda mas prolijo
		if self.primero:
			valor = self.primero.dato
			self.primero = self.primero.prox
			# Si después de avanzar no quedó nada, también hay que
			# eliminar la referencia del último.
			if not self.primero:
				self.ultimo = None
			return valor
		else:
			raise ValueError("La cola está vacía")

	def esta_vacia(self):
		"""Devuelve True si la cola esta vacia. False en caso contrario."""
		return (self.primero == None and self.ultimo == None)

	#Gaston: No te olvides de ver primero
