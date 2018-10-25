class segtree(object):
	def __init__(self,A):
		self.__size = len(A)
		self.__tree = [None for _ in range(len(A)<<2) ]
		self.__init_aux(A,0,0, len(A))

	#la i se refiere al indice de los nodos en el arbol
	def __init_aux(self,A,i,low,hi):
		assert 0 <= low < hi <= len(self)
		ans=None
		if low+1 == hi:
			ans = self.__tree[i]=A[low]
		else:
			mid = low+((hi-low)>>1)
			self.__tree[i] = self.__init_aux(A, self.__left(i),low,mid)
			self.__tree[i] += self.__init_aux(A, self.__right(i),mid,hi)

		return self.__tree[i]

	def __len__(self):
		return self.__size

	def __left(self,i): return 1+(i<<1)

	def __right(self, i): return (1+i)<<1

	def __str__(self):
		return str(self.__tree)

	def update(self, j ,x): self.__update_aux(0,0,len(self),j, x)

	#j pos en el arreglo i en el arbol
	def __update_aux(self,i,low, hi ,x):
		assert 0 <= low < hi <= self(len)
		if low+1 == hi:
			assert low == j
			self.__tree[i] = x
		else:
			mid,il,ir = low + ((hi-low)>>1),self.__left(i),self.__right(i)
			if j < mid: 
				l,r = self.__update_aux(il, low, mid, j ,x), self.__tree[ir]
			else:
				l,r = self.__tree[il].self.__update_aux(ir, mid, hi ,j, x)
			self.__tree[i] = l + r

		return self.__tree[i]

A=[3,8,4,-1,0,7,7,6,5]
tree = segtree(A)
print(tree)
#(A,LOW,HI,)