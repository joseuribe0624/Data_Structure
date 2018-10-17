from sys import stdin
import sys
from heapq import heappop,heappush

#jose david gutierrez uribe
INF = float('inf')

#codigo obtenido de la clase

class dforest(object):
	"""implements an union-find with path compression and ranking"""
	def __init__(self,size=10):
		self.__parent =[i for i in range(size)]
		self.__rank = [1 for _ in range(size)]
		#tamaño de componente y solo tienen sentido cuando esta asociado a una raiz
		self.__csize = [1 for _ in range(size)]
		self.__ccount = self.__size = size

	def __str__(self):
		"""return the string representation of the forest"""
		return str(self.__parent)

	def __len__(self):
		#return the number of elements in the forest
		return self.__size

	def csize(self, x):
		#return the number of elements in the component of x
		return self.__csize[self.find(x)]


	def ccount(self):
		#return the number of components of x
		return self.__ccount

	def find(self,x):
		#return the representative of the component of x
		if self.__parent[x] != x:
			self.__parent[x] = self.find(self.__parent[x])
		return self.__parent[x]

	def union(self, x, y):
		#computes the union of the components of x and y if they are different
		fx,fy = self.find(x),self.find(y)
		if fx != fy:
			rx,ry = self.__rank[fx],self.__rank[fy]
			#miro cual de los dos set es mayor para saber cual pongo debajo de cual
			if rx > ry:
				self.__parent[fy] = fx
				self.__csize[fx] += self.__csize[fy]
			else:
				self.__parent[fx] = fy
				self.__csize[fy] += self.__csize[fx]
				if rx==ry:
					self.__rank[fy] += 1
			self.__ccount -= 1


def solve():
	global no,x,y,forest
	if forest.find(x) == forest.find(y):
		no +=1
	else:
		forest.union(x,y)

def main():
	global x,y,no, forest
	enter = stdin.readline().split()
	while len(enter) != 0:
		no = 0
		forest = dforest(100001)
		while len(enter) > 1:
			x,y = map(int,enter)
			solve()
			enter = stdin.readline().split()
		stdin.readline()
		enter = stdin.readline().split()
		print(no)
	
main()