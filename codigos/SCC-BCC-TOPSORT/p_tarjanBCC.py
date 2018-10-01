import sys
sys.setrecursionlimit(100000)

def dfs(u):
    global visited,low,ids,id_n,bridges,is_art,parents,components
    low[u] = ids[u] = id_n ; visited[u] = True ; children = 0 #inicializar low e ids de acuerdo al id de cada nodo
    id_n += 1
    for v in G[u]:
        if(v == parents[u]): #revisar que no vuelva a su nodo padre
            continue
        if(visited[v] == False):
            children += 1
            parents[v] = u #asignar padre a el nodo recien encontrado v
            dfs(v)
            low[u] = min(low[u],low[v]) #asignar el minimo costo en el back-tracking
            if(ids[u] < low[v]): #significa que no hay un back edge al otro componente
                bridges.append((u,v))
            #preguntar esta partecita
            if((ids[u] <= low[v] and parents[u] != -1 ) or (parents[u] == -1 and children >1) ): #articulation, revisar si es una raiz con mas de 1 hijo en el Gdfs()
                is_art.append(u)
                components[u] += 1
        else:
            low[u] = min(low[u],ids[v])

def main():
    global G,ids,id_n,low,visited,bridges,is_art,parents,components
    id_n = 0
    bcc_cnt = 0
    G = [[1],[2],[0],[7,4],[5],[6,0],[0,2,4],[3,5]]
    n = len(G)
    ids = [0] * n ; low = [0] * n; parents = [-1] * n ; visited = [False] * n

    bridges = []
    is_art = []
    components = [1] * n
    bcc = [-1] * n
    for i in range(n):
        if (visited[i] == False):
            dfs(i)
    print(bridges)
    print(is_art)
    print(components)
    #print(low)


main()
