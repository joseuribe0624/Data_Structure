
INF = float('inf')
def floyd_warshall(G):
    n = len(G)
    dp = [[INF for i in range(n)] for j in range(n)]
    path = [[None for i in range(n)] for j in range(n)]
    for u in range(n):
        for v,d in G[u]:
            if d < dp[u][v]:
                dp[u][v] = d
                path[u][v] = u
    for i in range(n):
        dp[i][i] = 0
        path[i][i] = None
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(dp[i][k] + dp[k][j] < dp[i][j]):
                    dp[i][j] = dp[i][k] + dp[k][j]
                    path[i][j] = path[k][j]
                    
                    
                    


def main():
    pass



