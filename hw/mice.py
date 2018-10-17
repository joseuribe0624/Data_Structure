from sys import stdin
import sys
from heapq import heappop,heappush

#jose david gutierrez uribe
INF = float('inf')

#codigo obtenido de la clase
def dijkstra(G,s):
	global timer 
	ans = [INF for _ in G]; ans[s]=0
	prev = [None for _ in G]
	visited = [False for _ in G]
	#parejas distancia vertice cuando es monton, cuando es lista es vertice dist
	heap = [(0,s)]
	while len(heap)!= 0:
		d,u = heappop(heap)
		if visited[u]==False:
			for v,dv in G[u]:
				if d+dv<ans[v]:
					ans[v] = d+dv
					#decrease(v,ans[v])
					heappush(heap, (ans[v],v))
					prev[v] = u
			visited[u] = True 
			
	return ans

def main():
	cases = int(stdin.readline())
	while cases != 0:
		stdin.readline()
		cellNumber = int(stdin.readline()) + 1
		gate = int(stdin.readline())
		timer = int(stdin.readline())
		n = int(stdin.readline())
		G = [ list() for _ in range(cellNumber)]
		for i in range(n):
			u, v, d = map(int,stdin.readline().split())
			G[u].append((v, d))
			#G[v-1].append((u-1, d))
		#transpose
		R = [ list() for _ in range(cellNumber)]
		for u in range(cellNumber):
			for v,d in G[u]:
				R[v].append((u,d))
			#is the graph transpose
		ans=dijkstra(R, gate)

		count = 0
		#print("this is ans",ans)
		for i in ans[1:]:
			if i <= timer:
				count+=1
		print(count)
		if cases != 1:
			print()
		cases -= 1

main()

# 1 entrada N = number of cells
#2 number of exit cell E
#3 timer
# 4 M the number of conections
#one way
