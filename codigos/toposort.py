def toposort(G):
	ans = list()
	indeg = [ 0 for _ in len(G)]
	for u in range(len(G)):
		for v in G[u]:
			indeg[v] += 1
	pending = list()
	for u in range(len(G)):
		if indeg[u]==0:
			pending.append(u)
			
	while len(pending) ! = 0:
		u=pending.pop()
		ans.append(u)
		for v in G[u]:
			indeg[v] -= 1
			if indeg[v] == 0:
				pending.append(v)
	return ans

algoritmo que determine si hay mas de un orden topologico?
si la coleccion pending llega a tener mas de un elemento
