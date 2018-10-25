#Given a graph in which all nodes can be
#reached from any starting point, your job is to
#nd the average shortest path length between ar-
#bitrary pairs of nodes.
from sys import stdin
import sys

INF = float('inf')

def floydWarshall():
	global G
	v=len(G)
	dist=[[INF for _ in range(100)] for _ in range(100)]
	for u,v in G:
		print(u,v)
		dist[u][v] = 1
		dist[u][u] = dist[v][v] = 0 

	for k in range(1,v):
		for i in range(v): 
			for j in range(v):
				if dist[i][k] + dist[k][j] < dist[i][j]: 
					dist[i][j] = dist[i][k] + dist[k][j] 
	#print(dist)

def main():
	global G
	line = [int(x) for x in stdin.readline().strip().split()]
	#line = stdin.readline().strip()
	while line[0] != 0 and line[1] != 0:	
		#G=[list() for _ in range(100)]
		G=list()
		i=0
		while i < (len(line)-2):
			#print(line[i],line[i+1])
			G.append((line[i],line[i+1]))
			i+=2
		
		floydWarshall()
		print(G)
		line = [int(x) for x in stdin.readline().strip().split()]
main()