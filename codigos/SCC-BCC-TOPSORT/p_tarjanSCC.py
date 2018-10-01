#algoritmo para SCC tarjan hecho por mi
import sys
sys.setrecursionlimit(100000)

def dfs(u):
    global scc_cnt,stack,onstack,ids,low,id_n
    stack.append(u) ; onstack[u] = True
    ids[u] = low[u] = id_n ; id_n += 1

    for v in G[u]:
        if(ids[v] == -1):
            dfs(v)
        if(onstack[v]):
            low[u] = min(low[u],low[v])
    if(ids[u] == low[u]):
        node = -1
        while(node != u):
            node = stack.pop()
            onstack[node] = False
            low[node] = ids[u]
            #arreglo scc
        scc_cnt += 1


def main():
    global ids,low,scc_cnt,id_n,onstack,stack,G
    G = [ [3],[0,2],[0,4,9],[5],[1],[3,7],[5],[8],[7],[]]
    n = len(G)
    ids = [-1] * n
    low = [0] * n
    scc_cnt = 0
    id_n = 0
    onstack = [False]*n
    stack = []

    for i in range(n):
        if(ids[i] == -1):
            dfs(i)
    print(low)

    
main()
   

