
#fathers 
pa=[0,0,1,2,3,4,5,2,0,8,8,7,7,11]
n = len(pa)
depth = [None]*n

def compute_depth(i):
	#ya esta calculado
	if depth[i] != None:
		return
	elif i==pa[i]:
		depth[i]=0
	else:
		depth[i] = compute_depth([pa[i]])+1
	return depth[i]


for i in range(n):
	compute_depth(i)


k=5
gpa = [[None]*n for i in range(k)]

for i in range(n):
	gpa[0][i] = pa[i]

for k in range(1,k):
	for i in range(n):
		j=gpa[k-1][i]
		gpa[k][i] = gpa[k-1][j]


def kth_pa(k,i):
	for j in range(k-1,-1,-1):
		if (k>>j)%2==1:
			i=gpa[j][i]
	return i

def lowestCommonAncestor(i,j):
	if depth[i] > depth[j]:
		i=j

	j=kth_parent(depth[j]-depth[i],j)
	if i==j: return i
	for k in range(K-1,-1,-1):
		if gpa[k][i] != gpa[k][j]:
			i = gpa[k][i]
			j = gpa[k][j]
	
	return pa[i]

print(kth_pa(0,6))
