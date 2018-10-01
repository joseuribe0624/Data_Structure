from sys import stdin
import sys

#virus
#jose david gutierrez

#tupla
def dfs(start, target):
	stack, path = [start], []
	while stack:
		vertex = stack.pop()
		#if vertex[0] in path:
		#	continue
		path.append(vertex)  
		for neighbor in G[vertex[0]]:
			if vertex[1] <= neighbor[1] and neighbor[1] >= start[1] and neighbor[1] <= time[neighbor[0]]:
				time[neighbor[0]] = neighbor[1]
				stack.append(neighbor)



def main():
	global G,time
	cases = [int(i) for i in stdin.readline().strip().split() ]
	#railway stations n
	n = cases[0]
	#number of stations to be identifyd as candidate bombing
	m = cases[1]
	
	while n != 0 and m !=  0:
		i=m
		G = [[] for _ in range(n)]
		enter = [int(i) for i in stdin.readline().strip().split()]
		src = enter[0]
		target = enter[1]
		t_ini = enter[2]
		t_fin = enter[3]
		while i > 0:
			vertex = [int(i) for i in stdin.readline().strip().split()]
			u=vertex[0]
			v=vertex[1]
			weight = vertex[2]
			G[u].append((v,weight))
			G[v].append((u,weight))
			i-=1

		time = [0 for _ in range(n)]
		if t_ini > t_fin:
			print(0)
		else:
			ans = dfs((src,t_fin),(target,t_ini))
			if t_fin >= time[target]:
				print(1)
			else:
				print(0)

		
		cases = [int(i) for i in stdin.readline().strip().split() ]
		#railway stations n
		n = cases[0]
		#number of stations to be identifyd as candidate bombing
		m = cases[1]

main()