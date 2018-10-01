class BinTree:
	def __init__(self, num, left=None, right=None):
		self.num = num
		self.l = left
		self.r = right
		return 
	#convierte x a string
	def __str__ (self):
		str_l = str(self.l) if self.l != None else ''
		str_r = str(self.r) if self.r != None else ''
		#order
		s= '{} ({}) ({})'.format(self.num, str_l, str_r)
		#in order
		#s= '({}) {} ({})'.format(str_l,self.num, str_r)
		return s 


x = BinTree(3)
x.l = BinTree(2,BinTree(10), BinTree(7))
x.r = BinTree(4,BinTree(3), BinTree(9))


print(x)

#lista de adyacencia

#solo dos tipos de arboles los que son numeros o son listas
"""x=[3,[2,10,7],[4,3,9]]

def print_tree(x):
	if type(x) == int:
		if x!=None:
			print(x, end='')
	else:
		print('(', end='')
		print_tree(x[1])
		print(') ', end='')
		print(x[0], end='')
		print('(', end='')
		print_tree(x[2])
		print(') ', end='')
	return 
print_tree(x)

tree=[]
def tree2list(x):
	for i in range(len(x)):
		if type(x) == int:
			tree.append(x)
		else:
			if x == '(':
				tree.append([])
				while x != ')' or type(x) != int:
"""

# para arboles casi completos esta implementacion es la mas rapida pero no puede tener nodos o 
#sub arboles faltantes
"""x=['?',3,2,4,10,7,3,9]
def print_tree(x,r):
	if 2*r < len(x):
		print('(', end='')
		print_tree(x, 2*r)
		print(') ', end='')
	print(x[r], end = '')
	if 2*r+1 < len(x):
		print(' (', end='')
		print_tree(x, 2*r+1)
		print(')', end='')
	return


print_tree(x, r=1); print()"""





