from collections import deque
from sys import stdin

#Jose David Gutierrez Uribe

INF = float('inf')

def numero(digitos):
  valor=digitos[0]*1000+digitos[1]*100+digitos[2]*10+digitos[3]
  return valor


nexts = []
i = 0
while i < 10000:
    values = []
    y = []
    y.append(i // 1000)
    y.append((i % 1000) // 100)
    y.append((i % 100) // 10)
    y.append(i % 10)
    z=0
    while z < 4:
      copy = y[:]
      copy[z] = (y[z]+1)%10
      values.append(numero(copy))
      copy1 = y[:]
      copy1[z] = (y[z]-1)%10
      values.append(numero(copy1))
      z+=1
    nexts.append(values)
    i+=1


def bfs(visited,start, goal):
    queue = deque()
    x = [INF for _ in range(10000)]
    queue.append(start)
    x[start] = 0   
    #missing = len(queue)
    while  len(queue) != 0 and x[goal] == INF:
        vertex = queue.popleft()
        if visited[vertex] == 2:
          continue
        for item in nexts[vertex]:
          if visited[item] == 0:
              queue.append(item)
              x[item] = x[vertex] + 1
              visited[item]= 1

        visited[vertex] = 2
            
    if x[goal] == INF :
        return -1
    else:
        return x[goal]
   


def main():
  cases = int(stdin.readline().strip())
  while cases > 0:
    stdin.readline()
    initial = [int(x) for x in stdin.readline().strip().split()]
    target = [int(x) for x in stdin.readline().strip().split()]
    cantForbbidens = int(stdin.readline().strip())
    visited = [0 for _ in range(10000)]
    
    while cantForbbidens > 0:
      forbiddens = [int(x) for x in stdin.readline().strip().split()]
      visited[numero(forbiddens)] = 2
      cantForbbidens -= 1

    #change to numbers
    ini = numero(initial)
    targ = numero(target)
    print(bfs(visited,ini,targ))
    cases -= 1


main()