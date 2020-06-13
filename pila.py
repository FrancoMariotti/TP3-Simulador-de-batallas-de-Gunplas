class Pila:
	"""Tipo de dato abstracto Pila."""
	def __init__(self):
		"""Inicializa una pila vacía."""
		self.elementos=[]
	def apilar(self,elemento):
		"""Apila el elemento recibido"""
		self.elementos.append(elemento)

	def desapilar(self):
		"""Devuelve el elemento tope y lo elimina de la pila.
			Si la pila está vacía levanta una excepción."""
		if(self.esta_vacia()):
			#Gaston: ValueError
			raise IndexError("La pila está vacía")
		return self.elementos.pop()

	def esta_vacia(self):
		"""Devuelve True si la lista está vacía, False si no."""
		return len(self.elementos) == 0

	#Gaston: No te olvides de ver tope
