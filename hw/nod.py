#Jose David Gutierrez Uribe
from sys import stdin

#CRIBA tomada de la clase
is_prime = [True for i in range(1000001)]

for i in range(2,1000001):
    if is_prime[i]:
        for j in range(i*i,1000001,i):
            is_prime[j] =  False


primes = []
for i in range(2,1000001):
    if is_prime[i]:primes.append(i)


def NOD(n):
    i = 0 
    factor = primes[i] 
    cant = 1
    while factor*factor <= n:
        power = 0
        while(n % factor == 0):
            n /= factor 
            power+=1
        cant *= (power + 1)
        i+=1
        factor = primes[i]
    if n!=1:
        cant*=2 
    return cant


sequence = [1]
i=0
suma = 0
while sequence[i] <= 1000001:
    i+=1
    suma = sequence[i-1] + NOD(sequence[i-1])
    sequence.append(suma)
    

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

def solve(A, B):
    hi=len(sequence)
    indice2=binsearch(sequence,A)
    indice=binsearch(sequence,B)
   

    if sequence[indice2]<A:
        indice2+=1
    if sequence[indice]>B:
        indice-=1
  
    contador=(indice - indice2)+1
   
    
    return contador


def main():
  #make_seq()
  tcnt = int(stdin.readline())
  for tc in range(1, tcnt+1):
    A,B = map(int, stdin.readline().split())
    print('Case {0}: {1}'.format(tc, solve(A, B)))

main()