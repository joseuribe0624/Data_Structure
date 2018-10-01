from sys import stdin, setrecursionlimit

setrecursionlimit(10000)

INPUT, I = stdin.buffer.read(), 0
SPACE,CR,CR1,NEG = ord(' '),ord('\n'),ord('\r'),ord('-')


def isDigit():
  return 48 <= INPUT[I] <= 57

def isNeg():
  return INPUT[I] == NEG

def read_blanks():
  global INPUT, I
  while I < len(INPUT) and (INPUT[I] == SPACE or INPUT[I] == CR1 or INPUT[I] == CR):
    I += 1

def read_par():
  global INPUT, I
  ans, I = chr(INPUT[I]), I+1
  return ans

def read_num():
  global INPUT, I
  ans = 0
  while I < len(INPUT) and isDigit():
    ans, I = int(chr(INPUT[I])) + ans*10, I+1
  return ans

def next_token():
  global I
  ans = None
  read_blanks()
  if I != len(INPUT):
    if isNeg():
      I += 1
      ans = -1*read_num()
    elif isDigit():
      ans = read_num()
    else:
      ans = read_par()
  return ans





def solve(i,target):
  x=next_token()
  y=next_token()
  #True if is empty ()
  if x == "(" and y == ")":
    return -1
  else:
    check = solve(i+y,target)
    check1 = solve(i+y,target)
    next_token()
    if check == -1 and check1 == -1:
      if i+y == target:
        return 1
      else:
        return 0
    if check1 == 1 or check == 1:
      return True
    

def main():
  global INPUT,I,tree,target,objective
  #num target
  target = next_token()
  while target != None:
    ans = solve(0,target)
    if ans == True:
      print("yes")
    else:
      print("no")
    target=next_token()
  return 0

main()