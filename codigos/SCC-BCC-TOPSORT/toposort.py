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
    print(indeg)
    while len(pending) != 0:
        u = pending.pop()
        ans.append(u)
        for v in G[u]:
            indeg[v] -= 1
            print(v)
            if indeg[v] == 0:
                pending.append(v)
    return ans

def main():
    G = [[1],[0]]
    print(toposort(G))
    
main()
