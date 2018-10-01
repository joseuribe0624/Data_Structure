from sys import stdin
#Jose David Gutierrez Uribe

from sys import stdin
#Jose David Gutierrez Uribe


graph = []
visited = []
counts = []

def DFS(node,visited, graph,counts):
    t=0
    visited[node] = 1
    check = graph[node]
    if not visited[check] and graph[node] != -2:
        val = DFS(graph[node],visited, graph,counts)
        check+= 1 + val
    counts[node] = check
    visited[node] = 0
    return counts[node] 
 


def main():
  cases = int(stdin.readline().strip())
  while cases > 0:
    marthians = int(stdin.readline().strip())
    graph = [-2 for _ in range(marthians)]
    visited = [0 for _ in range(marthians)]
    counts = [-2 for _ in range(marthians)]
    x = marthians   
    while marthians > 0:
        pairs = [int(x) for x in stdin.readline().strip().split()]
        c1 = pairs[0]-1
        c2 = pairs[1]-1
        graph[c1] = c2 
        marthians-=1
    y=0
    correct = 0
    while y < x:
        if counts[y] > correct:
            correct = counts[y]
            solution = y
        elif counts[y] == -2:
            DFS(y,visited,graph,counts)
        y+=1 
    cases -= 1

main()

