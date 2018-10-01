from sys import stdin

#Jose David Gutierrez Uribe

deltar = [-1,0,0,1]
deltac = [0,-1,1,0]


#tomado de la clase problema war 
def dfs(row,col):
    global visited, board, n
    val = 1
    stack = [ (row,col) ] ; visited[row][col] = 1
    equidivision = board[row][col]
    while len(stack) != 0:
        r,c = stack.pop()
        for i in range (len(deltar)):
            dr,dc = r+deltar[i],c+deltac[i]
            if (0 <= dr < n and 0 <= dc < n and board[dr][dc] == equidivision and visited[dr][dc] == 0):
                stack.append((dr,dc)) ; visited[dr][dc] = 1
                val += 1
        visited[r][c] = 2
    return val


def solve():
    row= 0
    fail=1
    while fail and row < n:
        col = 0
        while col < n and fail != 0:
            if visited[row][col] == 0:
                c=dfs(row,col)
            if c != n:
                fail = 0 
                return fail
            col += 1
        row += 1
    return fail



def main():
    global board, n, visited
    n = int(stdin.readline())
    while n != 0:
        board = [[n for _ in range(n)] for _ in range(n)]
        visited = [[0 for _ in range(n)] for _ in range(n)]
        i=1
        while i < n:
            values = [ int(i) for i in stdin.readline().strip().split() ]
            tmp=list()
            tmp1=list()
            for y in range(1, len(values), 2):
                tmp.append(values[y]-1)
            for y in range(0,len(values),2):
                tmp1.append(values[y] - 1)
            for(x,y) in zip(tmp1,tmp):
                board[x][y] = i
            i+=1
        ans = solve()
        if ans == 0:
            print("wrong")
        else:
            print("good")

        n=int(stdin.readline())

main()
