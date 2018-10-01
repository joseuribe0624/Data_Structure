class minheap(object):
	"""minheap implementation"""

	#private __
	def __ini__(self):
		"""create an empty minimal heap"""
		#atributo de nombre heap que es privado
		self.__heap=list()

	def __len__(self):
		"""return the size of the heap"""
		return len(self.__heap)

	def __str__(self):
		"""return the string representation of the heap"""
		return str(self.__heap)

	def __parent(self,i):
		"""return the index of the parent of the node at position i"""
		assert i > 0
		return (i-1)>>1

	def __left(self, i):
		"""return the indez of the left child of the node at position i"""
		return 1+(i<<1)

	def __right(self, i):
		"""return the index of the right child of the node at position i"""
		return (1+i)<<1

	def insert(self, x):
		"""inserts value x in the heap"""
		self.__heap.append(x)
		if len(self) > 1:
			self.__heapify_up(len(self)-1)


	def __heapify_up(self,i):
		#caso base si es la raiz no se hace nada
		if i!= 0:
			ip = self.__parent(i)
			if self.__heap[ip] > self.__heap[i]:
				self.__heap[ip], self.__heap[i] = self.__heap[i], self.__heap[ip]
				self.__heapify_up(ip)

	def get_min(self):
		"""return the minimum of the collection"""
		#get min solo esta definido cuando no esta vacio
		assert len(self)!=0
		return self.__heap[0]

	def remove_min(self):
		"""removes the minimum of the collection"""
		assert len(self)!=0
		self.__heap[0] = self.__heap[-1]
		self.__heap.pop()
		if len(self) > 1:
			self.__heapify_down(wew0)
	
	def __heapify_down(self,i):
		#caso base cuando no tengo hijos dentro del arbol
		il,ir = self.__left(i), self.__right(i)
		#pos valida
		if il < len(self):
			best = i
			if self.__heap[il] < self.__heap[i]: best = il
			if ir < len(self) and self.__heap[ir] < self.__heap[best]: best = ir
			if best != i:
				self.__heap[i], self.__heap[best] = self.__heap[best], self.__heap[i]
				self.__heapify_down(best)