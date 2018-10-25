import random


#hago un dfs desde 0 hasta n nodo osea los nodos de arriba
def dfs_iterative(graph, start):
    stack, path = [start], []

    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)

    return path

def shot():
	pass

def main():
	global G
	n=2
	#no hay limite de taladradas
	nodes = [0 for _ in range(n)]
	G=[[0 for _ in range(n)] for _ in range(n)]

	while nodes[i] != 0:

	row=random.randint(0,n-1)	
	col=random.randint(0,n-1)
	

	
	print(G)

main()