from sys import stdin

#Jose David Gutierrez Uribe


def dfs(R, C, M, N, grid):
    stack = [(0,0)]
    i=0
    x=1
    even,odd = 0, 0
    if M == 0 and N == 0:
        return(0,0)        
    while stack:
        vertex = stack.pop()
        
        c1=vertex[0]
        c2=vertex[1]

        if grid[c1][c2] == 1:
            continue
        
        grid[c1][c2] = 1

        options = []
        if M == 0 or N == 0:
            options.append((vertex[i]+M,vertex[x]+N))
            options.append((vertex[i]+N,vertex[x]+M))
            options.append((vertex[i]-M,vertex[x]-N))
            options.append((vertex[i]-N,vertex[x]-M))
        
        elif M == N:
            options.append((vertex[i]+M,vertex[x]+N))
            options.append((vertex[i]-M,vertex[x]+N))
            options.append((vertex[i]+M,vertex[x]-N)) 
            options.append((vertex[i]-M,vertex[x]-N))
           
        else:
            options.append((vertex[i]+M,vertex[x]+N))
            options.append((vertex[i]+N,vertex[x]+M))
            options.append((vertex[i]-M,vertex[x]+N))
            options.append((vertex[i]+N,vertex[x]-M))
            options.append((vertex[i]+M,vertex[x]-N))
            options.append((vertex[i]-N,vertex[x]+M))
            options.append((vertex[i]-M,vertex[x]-N))
            options.append((vertex[i]-N,vertex[x]-M))


        count=0
        for item in options:
            val1=item[i]
            val2=item[x]
            if abs(vertex[i]-item[i])==M and abs(vertex[x]-item[x])==N and item[i] < R and item[x] < C and item[i] >= 0 and item[x] >= 0 and grid[val1][val2] != 2 :    
                stack.append(item)
                count+=1 
                    
            elif abs(vertex[i]-item[i])==N and abs(vertex[x]-item[x])==M and item[i] < R and item[x] < C and item[i] >= 0 and item[x] >= 0 and grid[val1][val2] != 2:  
                stack.append(item)
                count+=1 
                                
            else:
                continue
    
        if count%2 == 0:
            even+=1
        else:
            odd+=1
        
    return (even, odd)

def main():
    v = int(stdin.readline().strip())
    case = 1
    while v:
        valores = [int(x) for x in stdin.readline().strip().split()]
        R = valores[0] 
        C = valores[1]
        M = valores[2] 
        N = valores[3]
        w = int(stdin.readline().strip())
        grid = [[0 for _ in range(C)]for _ in range(R)]
        
        while w:
            water = [int(x) for x in stdin.readline().strip().split()]
            grid[water[0]][water[1]] = 2
            w -= 1

        valor=dfs(R,C,M,N,grid)
        #64 58 4 4
        print("Case {}: {} {}".format(case, valor[0], valor[1]))
        v -=1
        case += 1

#valor=solve(4,4,1,2,[(3,3),(1,1)])
main()
