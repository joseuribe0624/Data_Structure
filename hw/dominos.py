from sys import stdin
import sys
from collections import deque

#Jose David GUtierrez Uribe
#codigo tomado de la clase

sys.setrecursionlimit(10**6)
def dfs1(u):
	vis[u] = 1
	for v in R[u]:
		if vis[v]== 0:
			dfs1(v)
			vis[v]
	d.appendleft(u)
	return 

def dfs2(u):
	vis[u] = 1
	scc[u] = scc_cnt
	for v in G[u]:
		if vis[v]== 0:
			dfs2(v)
	return 
        
	

def main():
	cases = int(stdin.readline())
	global G, R, vis, d, scc, scc_cnt
	m=[]
	while cases > 0 :
		m = [ int(i) for i in stdin.readline().strip().split() ]
		#print(m[1])
		z = m[1]
		cantNode = m[0]
		G = [[] for _ in range(cantNode)]		
		while z != 0:
			vertex = [int(x) for x in stdin.readline().strip().split()]
			node =  (vertex[0]-1)
			conexion = (vertex[1]-1)
			G[node].append(conexion)
			z-=1

		#algorithm
		n = len(G)
		R= [[] for i in range(n)]
		for u in range(n):
			for v in G[u]:
				R[v].append(u)
		d=deque()
		vis = [0 for i in range(n)]
		for u in range(n):
			if vis[u] == 0:
				dfs1(u)
		scc = [-1 for i in range(n)]
		scc_cnt = 0
		vis = [0 for i in range(n)]
		for u in d:
			if vis[u] == 0:
				dfs2(u)
				scc_cnt += 1
		
		count = 0

		copy =[0 for i in range(n)]
		for i in range(n):
			for j in G[i]:
				if scc[j] != scc[i]:
					copy[scc[j]]+=1

		for i in range(scc_cnt):
			if not copy[i]:
				count+=1

		print(count)
		cases-=1

		


main()