#kosaraju realizado por mi
import sys
sys.setrecursionlimit(100000)
def dfs1(u):
    #en este dfs agrego a la pila
    global visited,S
    visited[u] = True
    for v in G[u]:
        if(visited[v] == False):
            dfs1(v)
    S.append(u)
    

def dfs2(u):
    global scc,visited
    scc[u] = scc_cnt
    visited[u] = True
    for v in R[u]:
        if(visited[v] == False):
            dfs2(v)
    

def main():
    global G,S,scc_cnt,scc,R,visited
    #G = [[1],[2],[3,4],[0],[5],[6],[4],[6,8],[]]
    G = [ [3],[0,2],[0,4,9],[5],[1],[3,7],[5],[8],[7],[]]
    n = len(G)
    visited = [False] * n
    scc = [-1 for _ in range(n)]
    scc_cnt = 0
    S = []
    #print("gafo", G)
    for i in range(n):
        if(visited[i] == False):
            dfs1(i)
            #print("this",S)

    R = [[] for _ in range(n)]
    for u in range(n):
        for v in G[u]:
            #is the graph transpose
            R[v].append(u)
            
    visited = [False] * n
    #print(S)
    while(len(S) != 0):
        u = S.pop()
        if(visited[u] == False):
            dfs2(u)
            scc_cnt += 1

    print(scc)

main()        
        
    
    
