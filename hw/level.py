from sys import stdin

#JOSE DAVID GUTIERREZ URIBE
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


#listo
def convert2tree(tree):
    global t, complete
    i=0
    while complete and i < len(tree)-1:
        ins = tree[i].split(",")
        arbol = t
        x=0
        num = ins[0][1:]
        edge = ins[1][:len(ins[1])-1]
        while x < len(edge):
            if edge[x] == "L":
                if arbol.l == None:
                    arbol.l = Tree(None)
                arbol = arbol.l
            else:
                if arbol.r == None:
                    arbol.r = Tree(None)
                arbol = arbol.r
            x+=1
        if arbol.num == None:
            arbol.num = num 
        else:
            complete = False  
        i+=1
    
#make level order or bfs

def levelOrder():
    global complete,t
    if t is None:
        return 
    queue = []
    queue.append(t)
    while queue and complete:
        ans.append(queue[0].num)
        node = queue.pop(0)
        #check if is complete
        if node.l != None or node.r != None:
            if node.num == None:
                complete = False
                continue
        if node.l != None:
            queue.append(node.l)
        if node.r != None:
            queue.append(node.r)


def main():
    global t,complete,ans
  #tree = [str(i) for i in stdin.readline().strip().split()
    tree = [str(i) for i in stdin.readline().strip().split()]
    while len(tree) != 0:
        complete = True
        ans=[]
        t=Tree(None)
        convert2tree(tree)
        levelOrder()

        if complete == False:
            print("not complete")
        else:
            i=0 
            while i < len(ans)-1:
                print(ans[i], end=" ")
                i+=1
            print(ans[i])
            
        tree = [str(i) for i in stdin.readline().strip().split()]
main()
