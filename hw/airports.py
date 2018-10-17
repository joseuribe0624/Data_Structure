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

"""df = dforest(7)
print(df)
df.union(5,6)
print(df)
print(df.csize(df.find(5)))"""

#with this kruskal i have to modify to give me the count of the money 
def kruskal(graph, lenv):
	global cost
	ans2=list()
	ans=0
	graph.sort(key = lambda x:x[2])
	df, i = dforest(lenv),0
	while i != len(graph):
		u,v,d = graph[i]
		#ciclo parara si la dist mayor aeropuerto
		#if d > cost:
		#	break
		if df.find(u) != df.find(v):
			ans+=d
			ans2.append((u,v,d))
			df.union(u,v)
		i+=1
	#i dont need this assert cause this only ensure me that i have one component
	#but the idea is get the cant of components
	z=df.ccount()
	# ways of getting the minimal cost, choose the one that has the most airports
	#assert df.ccount()==1
	#assert df.csize(df.find(0)) == lenv
	#print("cantidad= ",z)
	return ans,z

def main():
	global cost
	cases = int(stdin.readline())
	count=0
	while cases != 0:
		cost1=0
		lenv, lene, cost = map(int, stdin.readline().split())
		#G = [ list() for _ in range(lenv) ]
		G = list()
		cant=0
		cost1=0
		for i in range(lene):
			u, v, d = map(int, stdin.readline().split())
			#is bidirectional
			if d < cost:
				G.append((u-1,v-1,d))
				G.append((v-1,u-1,d))	
		#cant is the cant of components
		cost1,cant=kruskal(G, lenv)
		#print("fuck=", cant,cost1)
		cost1+= (cant-1)*cost
		cost+=cost1
		count+=1
		out="Case #"
		out+=str(count)
		out+=":"
		s= '{} {} {}'.format(out,cost,cant)
		print(s)
		cases -=1
main()

#two ways are the roads
#entradas n,m,a  	n=number of locations M number of possible roads can be built A cost of build an airport



