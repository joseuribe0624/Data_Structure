from sys import stdin
import sys
from heapq import heappop,heappush

#jose david gutierrez uribe
INF = float('inf')

def dijkstra(heap):
	global ans,G
	#prev = [None for _ in G]
	visited = [False for _ in G]
	#heap = [(0,s)]
	while len(heap)!= 0:
		d,u = heappop(heap)
		if visited[u]==False:
			for v,dv in G[u]:
				if d+dv < ans[v]:
					ans[v] = d+dv
					heappush(heap, (ans[v],v))
					#prev[v] = u
			visited[u] = True 
	return ans

def solve():
	global ans, locationP, G, locationB
	ans = [INF for _ in G]
	#inicio todos los s de los policias
	heap = []
	for i in locationP:
		ans[i]=0
		heappush(heap,(0,i))

	sol=dijkstra(heap)
	#print(sol)
	d=[]
	for i in range(len(locationB)):
		d.append(sol[locationB[i]])
	
	#print(d)
	maximum = max(d)
	order = []
	counter=0
	for i in range(len(d)):
		if d[i] == maximum:
			counter += 1
			order.append(locationB[i])

	order.sort()
	if maximum == INF:
		print(counter, "*")
	else:
		print(counter, maximum)

	flag=0
	for i in range(len(order)-1):
		print(order[i], end=" ")
		flag=i

	if flag+1 < len(order):
		print(order[flag+1])
	elif flag == 0:
		print(order[flag])



def main():
	global locationP, G,locationB
	#N sites on the city
	#M number roads
	#B number banks
	#P number of police station
	var = [int(x) for x in stdin.readline().strip().split()]
	while len(var) != 0:
		N = var[0]
		M = var[1]
		B = var[2]
		P = var[3]
		G = [ list() for _ in range(N)]
		for i in range(M):
			u, v, d = map(int, stdin.readline().split())
			G[u].append((v, d))
			G[v].append((u, d))
		#bank location
		locationB = [int(x) for x in stdin.readline().strip().split()]
		#police station location
		
		if P == 0:
			print(B, "*")
			locationB.sort()
			flag=0
			for i in range(len(locationB)-1):
				print(locationB[i], end=" ")
				flag=i
			if flag+1 < len(locationB):
				print(locationB[flag+1])
			elif flag == 0:
				print(locationB[flag])
		else:
			locationP = [int(x) for x in stdin.readline().strip().split()]
			solve()


		var = [int(x) for x in stdin.readline().strip().split()]

	# 1 29 21
		
main()