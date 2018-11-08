from sys import stdin
import sys

INF = float('inf')

#jose david gutierrez uribe

def floydWarshall(G):
	length=len(G)
	dist=[[INF for _ in range(inter)] for _ in range(inter)]

	for u,v in G:
		dist[u][v] = 1
	for u,v in G: 
		dist[v][v] = 0 

	for k in range(inter):
		for i in range(inter): 
			for j in range(inter):
				if dist[i][k] + dist[k][j] < dist[i][j]: 
					dist[i][j] = dist[i][k] + dist[k][j] 
	return dist
	

def main():
	global inter
	inter= int(stdin.readline().strip())
	while inter != 0:
		old = list()
		for i in range(inter):
			conect = [int(x) for x in stdin.readline().strip().split()]
			for x in range(1,len(conect)):
				old.append((conect[0]-1,conect[x]-1))
		new = list()
		for i in range(inter):
			conect = [int(x) for x in stdin.readline().strip().split()]
			for x in range(1,len(conect)):
				new.append((conect[0]-1,conect[x]-1))

		A, B = map(int, stdin.readline().strip().split())
		dis1=floydWarshall(old)
		dis3=floydWarshall(new)
		response = False
		for i in range(inter):
			for x in range(inter):
				valNew = dis3[i][x]
				valOld = (A*dis1[i][x]) + B 
				if valNew > valOld:
					response = True
		if response:
			print("No")
		else:
			print("Yes")
		inter = int(stdin.readline().strip())

main()