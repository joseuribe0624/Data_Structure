#dijkstra
from heapq import heappop,heappush

INF = float('inf')

#se puede mejorar usando colas de prioridad en esta se usa decrease
"""para llave u actualiza el valor u"""

#complexity O(v+elogv)
def dijksra(G,s):
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
					pre[v] = u
			visited[u] = True 
	return ans

def main():
    lenv, lene = map(int, stdin.readline().split())
    G = [ list() for _ in range(lenv) ]
    for _ in range(lene):
        u, v, d = map(int, stdin.readline().split())
        G[u].append((v, d))
        G[v].append((u, d))
    print(dijkstra(G, 0))

