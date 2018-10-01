#Jose David Gutierrez Uribe
from sys import stdin
    

#tomado de la clase
def binsearch(A,x):
    N = len(A)
    assert N >= 1
    low,hi = 0,N
    
    while(low+1 != hi):
        mid = low+((hi-low)>>1)
        if(x < A[mid]):
            hi = mid
        else:
            low = mid
    return low

def solve(chimps, heights):
    value=binsearch(chimps,heights)
    if chimps[value]==heights:
        if value-1 < 0:
            if value+1 >= len(chimps):
                return ('X', 'X')
            else:
                return ('X', chimps[value+1])

        elif value+1 >= len(chimps):
            return (chimps[value-1], 'X')
        else:
            return (chimps[value-1], chimps[value+1])

    elif chimps[value] != heights:
        if chimps[value] > heights:

            return ('X', chimps[value])
        else:
            if value-1 < -1:
                if value+1 >= len(chimps):
                    return ('X', 'X')
                else:
                    return ('X', chimps[value])

            elif value+1 >= len(chimps):
                return (chimps[value], 'X')
            
            else:
                return (chimps[value], chimps[value+1])



#stdin.readline()
        #chimps = [int(x) for x in stdin.readline().strip().split()]

def main():
    chimpsHeights = int(stdin.readline().strip())
    limit=chimpsHeights
    chimp = [int(x) for x in stdin.readline().strip().split()]
    chimps=[]
    chimps.append(chimp[0])
    z=0
    i=1
    while i < limit:
        if chimps[z] != chimp[i]:
            chimps.append(chimp[i])
            z+=1
        i+=1
    heightsLuchu = int(stdin.readline().strip())
    heights = [int(x) for x in stdin.readline().strip().split()]
    #heightsLuchu -=1
    
    for i  in heights:
        tupla = solve(chimps, i)
        print(tupla[0],tupla[1])


main()