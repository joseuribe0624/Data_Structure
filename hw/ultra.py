#Jose David Gutierrez Uribe

#merge sort: https://www.geeksforgeeks.org/merge-sort/
#https://www.pythoncentral.io/merge-sort-implementation-guide/

from sys import stdin


MAX   = 50010
num   = [ None for i in range(MAX) ]

# Merge sort obtenido de la clase del miercoles de la primera semana
def solve(lo, hi):
  # Conquistar
  if hi - lo <= 1:
    return 0

  # Dividir
  mid = (lo + hi) // 2
  count = solve(lo, mid)
  count += solve(mid, hi)

  # Combinar
  aux = []
  i = lo
  j = mid
  while i < mid and j < hi:
    if num[i] <= num[j]:
      aux.append(num[i])
      i += 1
    else:
      aux.append(num[j])
      j += 1
      count += mid - i

  while i < mid:
    aux.append(num[i])
    i += 1

  while j < hi:
    aux.append(num[j])
    j += 1

  num[lo:hi] = aux
  return count

def main():
  global num
  inp = stdin
  n = int(stdin.readline().strip())
  while n>0:
    for i in range(n):
      num[i] = int(stdin.readline())
    print(solve(0, n))
    n = int(stdin.readline().strip())

main()
