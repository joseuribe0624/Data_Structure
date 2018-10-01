from sys import stdin, setrecursionlimit

setrecursionlimit(10000)

#jose david gutierrez uribe
def toposort(G):
    ans = list()
    indeg = [0 for _ in range(len(G))]
    pending = list()
    for u in range(len(G)):
        for v in G[u]:
            indeg[v] += 1
    for u in range(len(G)):
        if indeg[u] == 0:
            pending.append(u)
    while len(pending) != 0:
        u = pending.pop()
        ans.append(u)
        for v in G[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                pending.append(v)
    return ans

def topologicalSort(ans,visited):
	global indeg,ans2
	mark=False
	for i in range(n):
		if indeg[i] == 0 and visited[i] == False:	
			for v in G[i]:
				indeg[v] -= 1
			ans.append(i)
			visited[i] = True
			topologicalSort(ans,visited)
			visited[i] = False
			val=ans.pop()
			for v in G[i]:
				indeg[v] += 1
			mark=True
	if mark != True:
		if len(ans) != 0:
			for i in range(len(ans)):
				if i < len(ans)-1:
					print(mapa2[ans[i]],end=' ')
				else:
					print(mapa2[ans[i]])
		else:
			complete=True
			print("NO")
		
			return complete
		


def main():
	global G,n,indeg,mapa,mapa2, ans2
	cases = int(stdin.readline())
	while cases != 0:
		blank = stdin.readline()
		variables = stdin.readline().split()
		c = sorted(variables, key=lambda c: (c.upper(), c.isupper()))
		graph = stdin.readline().split()
		#C IS ORDER
		mapa={}
		mapa2={}
		n=len(c)
		x=0
		for i in c:
			mapa[i] = x
			mapa2[x] = i
			x+=1
		G=[[] for _ in range(len(c))]
		for i in range(len(graph)):
			conection = graph[i]
			pos = mapa[conection[0]]
			to = mapa[conection[2]]
			G[pos].append(to)

		visited=[False for _ in range(n)]
		ans=[]
		indeg = [0 for _ in range(n)]
		for u in range(len(G)):
			for v in G[u]:
				indeg[v] += 1

		respuesta=[]
		respuesta=toposort(G)
		if len(respuesta) < len(c):
			print("NO")
		else:
			complete = False
			complete=topologicalSort(ans,visited)
		
		if cases != 1:
			print()	
		cases-=1

main()