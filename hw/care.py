from sys import stdin
import sys

INF = float("inf")

#jose david gutierrez uribe

#codigo tomado de la clase
def toposort():
	ans = list()
	indeg = [ 0 for _ in range(len(G)) ]
	for u in range(len(G)):
		for v in G[u]:
			indeg[v] += 1
	pending = list()
	for u in range(len(G)):
		if indeg[u]==0:
			pending.append(u)
	while len(pending)!=0:
		u = pending.pop()
		ans.append(u)
		for v in G[u]:
			indeg[v] -= 1
			if indeg[v]==0:
				pending.append(v)
	return ans


def dfs(start):
	global G,visited
	stack = [start]
	last = INF
	while stack:
		vertex = stack.pop()
		if visited[vertex] != 0:
			continue
		#path.append(vertex)

		for neighbor in G[vertex]:
			stack.append(neighbor)
			visited[vertex] = 1
		if not G[vertex]:
			if  last == INF:
				last = vertex
			else:
				if last != vertex:
					return 0
				else:
					pass
	return 1


def solve(n):
	DAG=toposort()
	ans = 0
	if len(DAG) < n:
		return 0
	else:
		for i in range(len(G)):
			if visited[i] == 0:
				ans = dfs(i)
				if ans == 0:
					return 0
		#print(1)
		return 1

def main():
	global G,visited
	cases = [int(i) for i in stdin.readline().strip().split() ]
	#number of nodes
	n = cases[0]
	#number of cases
	m = cases[1]
	while n != 0 or m !=  0:
		i=m
		visited = [0 for _ in range(n)]
		G = [[] for _ in range(n)]
		while i > 0:
			transitions = [int(i) for i in stdin.readline().strip().split()]
			a=transitions[0]
			b=transitions[1]
			G[a].append(b)	
			i-=1

		print(solve(n))

		cases = [int(i) for i in stdin.readline().strip().split() ]
		#railway stations n
		n = cases[0]
		#number of stations to be identifyd as candidate bombing
		m = cases[1]


main()