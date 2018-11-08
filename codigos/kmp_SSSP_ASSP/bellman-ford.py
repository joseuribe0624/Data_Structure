
INF = float('inf')
def bellman_ford(G,s):
    n = len(G)
    d = [INF]*n; d[s] = 0
    cycle = False
    for i in range(n-1):
        for u in range(n):
            for v,t in G[u]:
                if d[u] + t < d[v]:
                    #print(u)
                    d[v] = d[u] + t
        

    for u in range(n):
        for v,t in G[u]:
            if d[u] + t < d[v]:
                cycle = True
                
            
    
    return d,cycle


def main():
    G = [[(1,-1),(2,4)],[(2,3),(3,2),(4,2)],[],[(2,5),(1,1)],[(3,-3)]]
    ans = bellman_ford(G,3)
    print(ans)

main()
