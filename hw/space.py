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

#right, left, down, up
moves = [(0,1),(0,-1),(1,0),(-1,0)]
#union for initia board
def union(i,j):
	global r,c, joint, board, pastBoard, matriz
	pos=equation(i,j)
	#print(board[j])
	#matriz[pos]=True
	#check if is conected to the alien
	if i-1==-1 and board[j] == ".":
		#print("entro alien")	
		joint.union(pos,0)
	#check if is conected to the ship
	if i+1 == r and board[j] == ".":	
		#print("entro ship")	
		joint.union(pos, r*c+1)
	#check right
	#here, is verifying that the post next to the actual there is a dot
	#print("epa",moves[0][1],"pos search= ",(j+moves[0][1]),board[j+moves[0][1]])
	if j+1 < c and board[j+moves[0][1]] == "." and board[j] == ".":	
		#print("entro right")	
		posRight = equation(i,j+1)
		joint.union(posRight,pos)
	#check left
	if j-1 > c and board[j+moves[0][1]]=="." and board[j] == ".":	
		#print("entro left")	
		posLeft = equation(i,j-1)
		joint.union(posLeft,pos)

	#check up for this i create a board that stores the values of the col above
	if i-1 >= 0 and pastBoard[j] == "." and board[j] == ".":
		#print("entro up2")	
		posUp = equation(i-1,j)
		joint.union(pos,posUp)
#union after a shot
#area is a pos of the new point
def afterShot(i,j):
	global r,c, joint, board, pastBoard, matriz
	pos=equation(i,j)
	matriz[pos]=True
	#check if is conected to the alien
	if i-1==-1:
		joint.union(pos,0)
	#check if is conected to the ship
	if i+1 == r:
		joint.union(pos, r*c+1)
	#check right
	if j+1 < c:
		posRight = equation(i,j+1)
		if matriz[posRight] == True:
			joint.union(posRight,pos)
		else:
			pass
	#check left
	if j-1 > c:
		posLeft = equation(i,j-1)
		if matriz[posRight] == True:
			joint.union(posLeft,pos)
		else:
			pass
	#up
	if i-1 >= 0:
		posUp = equation(i-1,j)
		if matriz[posUp] == True:
			joint.union(pos,posUp)
		else:
			pass
	#check down
	if i+1 < r:
		posDown = equation(i+1,j)
		if matriz[posDown] == True:
			joint.union(pos,posDown)
		else:
			pass

def equation(i,j):
	global board,up,down, pastBoard, joint,c
	return c*i+j+1

def update(i,j):
	global up,down,board,r,c,matriz
	dif = i-r
	#print("hey",i)
	#alien
	if i < dif:
		if board[j] == "#":

			#en la col j va a ver un shield en la row i
			up[j]=i
	#space ship
	elif dif < i:
		if board[j] == "#":
			down[j]=i
	#elif i<=:

def update2(i,j):
	global up,down,board,r,c,matriz
	dif = i-r
	#print("hey",i)
	#alien
	pos = equation(i,j)
	matriz[pos] == True
	for p in range(len(matriz)):
		if i < dif:
			if matriz[j] == False:
				#en la col j va a ver un shield en la row i
				up[j]=i
		#space ship
		elif dif < i:
			if matriz[pos] == False:
				down[j]=i


def main():
	global board,up,down, pastBoard, joint,c,matriz,r
	line = stdin.readline().strip()
	while len(line):
		#r= row c=col s=shots
		r, c, s = map(int, line.split())
		#r, c, s = map(int, stdin.readline().split())
		joint = dforest(r*c+2)
		#this is an array that contain the next shield for up and down and is representing the cols
		# and i need update where is the next shield to brake 
		up=[0 for _ in range(c)]
		down = [0 for _ in range(c)]
		pastBoard = []
		matriz = [False for _ in range(r*c+2)]
		for i in range(r):
			board = stdin.readline().strip()
			for j in range(c):
				union(i,j)
				update(i,j)
			pastBoard = board

		k=0
		if joint.find(0) == joint.find(r*c+1):
			print(0)
		else:
			#the cant of shots
			#i=row
			#j=col
			for i in range(s):
				a=int(stdin.readline().strip())	
				shot=abs(a)-1
				if a < 0:
					#print(len(down))
					#en la col shot-1 cual es el proximo? y=
					y=down[shot]
					#print(y)
					position = equation(y,shot)
					if matriz[position] == True:
						pass
					else:
						update(y,shot)
						afterShot(y,shot)
						
				else:
					y=up[shot-1]
					position = equation(y,shot)
					if matriz[position] == True:
						pass
					else:
						update(y,shot)
						afterShot(y,shot)
						
				if joint.find(0) == joint.find(r*c+1):
					if shot < 0:
						print(shot)
					else:
						print(a)
				#print(joint)
				k+=1


			if joint.find(0) != joint.find(r*c+1):
				print('X')
		for _ in range(s-k):
			stdin.readline()

		line = stdin.readline().strip()
main()