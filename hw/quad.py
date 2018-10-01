from sys import stdin,setrecursionlimit

import sys

setrecursionlimit(10000)

#modificar la clase ya que el arbol puede tener 4 hijos
class Tree:
	def __init__(self, num, left=None, left2=None, right=None,  right2=None):
		self.num = num
		self.l = left
		self.l2 = left2
		self.r = right
		self.r2 = right2
		return 
	#convierte x a string
	def __str__ (self):
		str_l = "("+str(self.l)+")" if self.l != None else ''
		str_r = "("+str(self.r)+")" if self.r != None else ''
		str_l2 = "("+str(self.l2)+")" if self.l2 != None else ''
		str_r2 = "("+str(self.r2)+")" if self.r2 != None else ''
		# pre order
		s= '{} {} {} {} {}'.format(self.num, str_l,str_l2,str_r,str_r2) 
		return s.strip() 


def convert2tree(tree):
	global x
	if x < len(tree)-1:
		x+=1		
		if tree[x] == "f":
			return Tree("f")
		elif tree[x] == "e":
			return Tree("e")
		else:
			return Tree("p",convert2tree(tree),convert2tree(tree),convert2tree(tree),convert2tree(tree)) 


#se multiplica por 4
def bfs(t):
	ans=[]
	if t is None:
		return 
	queue = []
	queue.append(t)
	level=[]
	count=0
	pos=0
	ans.append([])
	while queue:
		if count == 1 or count == 4 or count == 8 or count == 32 or count == 128 or count == 512 or count == 2048:
			ans.append([])
			pos+=1
		ans[pos].append(queue[0].num)
		node = queue.pop(0)
		#check if is complete
		if node.l != None:
			queue.append(node.l)
		if node.l2 != None:
			queue.append(node.l2)
			#level.append(queue[0].num)
			#ans.append(level)
		if node.r != None:
			queue.append(node.r)
			
		if node.r2 != None:
			queue.append(node.r2)
		count+=1

	return ans


def solve():
	while i <length3
def main():
	global tree1,tree2,length3,x
	cases = int(stdin.readline())
	while cases != 0:
		tree1 = str(stdin.readline())
		tree2 = str(stdin.readline())
		x=-1
		length1=len(tree1)
		length2=len(tree2)
		#tree3 = tree(None)
		if length1 >= length2:
			length3=length1
		else:
			length3=length2
		#functions to convert
		tree=convert2tree(tree1)
		x=-1
		tree2 = convert2tree(tree2)
		#get the level order
		lvl1 = bfs(tree)
		lvl2 = bfs(tree2)
		print(lvl1)
		print(lvl2)
		#tree2=convert2tree(tree2)
		cases -=1

	return 
main()