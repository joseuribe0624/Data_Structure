

class Heap:
	def __init__(self):
		self.t = None
		self.l = None
		self.r = None
		self.nl= 0 
		self.nr = 0
		self.val = val

	def push(self,k):

		if self.val == None:
			self.val = k
		elif self.t.l == None:
			self.t.l = Tree(k)

		elif self.t.r==None:
			self.t.r = Tree(k)
			self.t.nr +=1

		elif self.t.nl < 2*self.t.n+1r:
			self.t.l.push(k)
			self.t.nl += 1
		else 
			self.t.r.push(k)
			self.t.nr += 1

 	def preorder(self):
 		print(self.k)
 		if self
