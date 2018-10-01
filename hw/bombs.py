from sys import stdin
import sys

INF = float("inf")

sys.setrecursionlimit(10**6)
#jose David Gutierrez Uribe

def dfs(u,v,idn):
	#v = child
	#u = parent
	#ids = discovery time
	#pigeonsValue this is for save the quantity of components that conform the graph when an articulation point
	#is disconnected
	global G,low,ids,parent,visited,isArt
	#ids = disc time
	visited[u] = True
	ids[u] = low[u] = idn +1
	child = 0 
	count=0
	for v in G[u]:
		if visited[v]==0:
			child += 1
			#parent array
			parent[v] = u
			dfs(v, u,idn+1)
			low[u] =  min(low[u], low[v])
			if parent[u]==-1 and child > 1:
				isArt[u] = True
				pigeonsValue[u]+=1
			if parent[u] != -1 and low[v] >= ids[u]:
				count+=1
				#print("this is node=",u)
				pigeonsValue[u] = count
				#print(count)
				isArt[u] = True
		elif parent[u] != v:
			low[u] = min(low[u],ids[v])



def solve(longi):
	global  G, outEdgeCount, low, ids, visited, isArt,parent, pigeonsValue
	idN = 0
	n = longi
	#outEdgeCount = 0
	pigeonsValue = [0 for _ in range(n)]
	low = [INF for _ in range(n)]
	ids = [0 for _ in range(n)]
	visited = [0 for _ in range(n)]
	parent = [-1 for _ in range(n)]
	isArt = [False for _ in range(n)]
	#for i in range(n):
		#print("this is i=",i)
	#if visited[i] == 0:
	#outEdgeCount = 0
	dfs(0, -1,idN)
	#isArt[i] = (outEdgeCount > 1)
	
	
	return isArt


def main():
	global G
	cases = [int(i) for i in stdin.readline().strip().split() ]
	#railway stations n
	longi = cases[0]
	#number of stations to be identifyd as candidate bombing
	m = cases[1]
	while m > 0 and longi > 0:
		G=[[] for _ in range(longi)]
		x=0
		y=0
		while x != -1 and y != -1:
			railway = [int(i) for i in stdin.readline().strip().split()]
			x=railway[0]
			y=railway[1]
			if x != -1 and y != -1:
				#graph construction
				G[x].append(y)
				G[y].append(x)

		articulations = []
		articulations=solve(longi)
		candidates = 0
		ans = []
		complete = m

		#for i in range(longi):
		#	ans.append(())
		#for i in range(longi):
		#	print(i, articulations[i])

		for xy in range(longi):
			if(articulations[xy] == True):
				pigeons=pigeonsValue[xy] + 1
				ans.append((xy, pigeons))
				complete-=1
		
		ans = sorted(ans, key=lambda item: -item[1])
		if complete <= 0:
			for v in range(m):
				print(ans[v][0], ans[v][1])

		else:
			p = 0 
			while p < longi and complete != 0:
				if articulations[p] == False:
					ans.append((p,1))
					complete-=1
				p+=1
			for t in range(len(ans)):
				print(ans[t][0], ans[t][1])
			
		print()
		cases = [int(i) for i in stdin.readline().strip().split() ]
		#railway stations n
		#creo que tiene que ser longi no n= caseS[0]
		longi = cases[0]

		#number of stations to be identifyd as candidate bombing
		m = cases[1]


main()