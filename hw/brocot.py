from sys import stdin

#Jose David Gutierrez Uribe
def solve(target):
    
    stop=False
    i=1
    ruta=""
    a=target[0]
    b=target[1]

    numerIzq = 0
    denomIzq = 1
    numerActual=1
    denomActual=1
    numerDer = 1
    denomDer = 0
    
    if(a==numerActual and b==denomActual):
        return "I"

    while(stop != True): 
        
        if (numerActual * b < denomActual * a):
            ruta+="R"
            numerIzq = numerActual
            denomIzq = denomActual
            numerActual = numerIzq + numerDer
            denomActual = denomIzq + denomDer 
            if numerActual == a and denomActual == b:
              stop=True
              return ruta 
        else:
          ruta+="L"
          numerDer = numerActual
          denomDer = denomActual
          numerActual = numerIzq + numerDer
          denomActual = denomIzq + denomDer 
          if numerActual == a and denomActual == b:
            stop=True
            return ruta 
          

def main():
  target = [int(x) for x in stdin.readline().strip().split()]
  while target[0]!=1 or target[1]!=1:
    print(solve(target))
    target = [int(x) for x in stdin.readline().strip().split()]

main()
