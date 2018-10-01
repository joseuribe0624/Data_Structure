from sys import stdin, setrecursionlimit
import operator
setrecursionlimit(10000)

#jose david gutierrez uribe

#tomado d ela clase
class Tree:
    def __init__(self, num, left=None, right=None):
        self.num = num
        self.l = left
        self.r = right
        return 
    def __str__ (self):
        str_l = "("+str(self.l)+")" if self.l != None else ''
        str_r = "("+str(self.r)+")" if self.r != None else ''
        # pre order
        s= '{} {} {} '.format(self.num, str_l,str_r) 
        return s.strip() 


def convert2tree(tree):
    global t, complete
    i=0
    stack = []
    stack.append(t)
    arbol = t
    while i < len(tree):
        #copio el arbol vacio
        if tree[i] == "(":
          arbol.l = Tree(None)
          stack.append(arbol)
          arbol = arbol.l        
        elif tree[i] == "*" or tree[i] == "/" or tree[i] == "-" or tree[i]=="+":
          arbol.num = tree[i]
          arbol.r = Tree(None)
          stack.append(arbol)
          arbol = arbol.r  
        elif tree[i] not in ["*","/","-","+", "(", ")"]:
          arbol.num = float(tree[i])
          arbol = stack.pop()
        elif tree[i] == ")":
          arbol = stack.pop()
        i+=1
 
#tomado de la clase    
def solve(t):
  if type(t.num) == float:
    return t.num
  elif t.num == '+':
    ans = 0
    val = solve(t.r)
    val2 = solve(t.l)
    ans = val
    ans += val2
    return ans
  elif t.num == '*':
    ans = 1
    val = solve(t.r)
    val2 = solve(t.l)
    ans *= val
    ans *= val2
    return ans
  elif t.num == '-':
    ans = 0
    val = solve(t.l)
    ans = val
    val2 = solve(t.r)
    ans -= val2
    return ans
  elif t.num == '/':
    ans = 1
    values =[]
    val = solve(t.l)
    ans = val
    val2 = solve(t.r)
    ans /= val2
    return ans

def main():
  global INPUT,I,tree,target,t
  #num target
  cases = int(stdin.readline())
  while cases != 0:
    t=Tree(None)
    tree = stdin.readline().split()
    convert2tree(tree)
    result = 0
    result = solve(t)
    check="%.2f"%result
    print(check)
    
    cases-=1

  return 0

main()

