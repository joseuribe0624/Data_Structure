def dfs_tarjan(u):
    low[u] = depth[u]
    for v in G[u]:
        if depth[v] == -1: #(u,v) es parte del arbol
            depth[v] = depth[u] + 1
            s.append((u,v))
            papa[v] = u
            dfs_tarjan(v)
            low[u] = min(low[u],low[v])
            if(low[v] >= depth[u]):
                comps[u] += 1
                #hacer pop hasta encontrar la pareja de arriba
        elif v == papa[u]: #(u,v) es el retorno hacia el padre
            pass
        else:
            #(u,v) es un back-edge
            low[u] = min(low[u],depth[v])
            
            


def main():
    global low,depth,papa,comps,s
    n = len(G)
    s = []
    comps = [0 for i in range(n)]
    low = [-1 for i in range(n)]
    depth = [-1 for i in range(n)]
    papa = [-1 for i in range(n)]
    for u in range(n):
        if depth[u] == -1:
            depth[u] = 0
            dfs_tarjan(u)
    print(depth)
    print(low)
    
    return



G = [ [1,3,5,6,9],[0,2,4],[1,4],[0,5],[1,2],[0,3,7,8],[0,9],[5],[5],[0,6]]
main()
