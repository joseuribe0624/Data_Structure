class binTree:
    def __init__(self,num,left = None,right = None):
        self.num = num
        self.l = left
        self.r = right
        return
    def __str__(self):
        str_l = str(self.l) if self.l != None else ''
        str_r = str(self.r) if self.r != None else ''
        #s = '{} ({}) ({})'.format(self.num, str_l, str_r) #pre-order
        s = '({}) {} ({})'.format(str_l, self.num , str_r) #in-order
        return s


#-----------------------------------Preorders------------------------------------------------------
def preorder_class(tree): #para la clase arbol
    if(tree.l == None and tree.r == None):
        print(tree.num)
        return
    print(tree.num)
    preorder_class(tree.l)
    preorder_class(tree.r)


def preorder_li(tree):
    if(type(tree) != list):
        if(tree != None):
            print(tree)
    else:
        print(tree[0])
        preorder_li(tree[1])
        preorder_li(tree[2])
        
def preorder_li2(tree,r):
    print(tree[r])
    if 2*r < len(tree):
        preorder_li2(tree,2*r)
    if 2*r+1 < len(tree):
        preorder_li2(tree,2*r+1)
#-----------------------------------Preorders------------------------------------------------------

#-----------------------------------inorders-------------------------------------------------------

def inorder_class(tree):
    if(tree.r == None and tree.l == None):
        print(tree.num)
    else:
        inorder_class(tree.l)
        print(tree.num)
        inorder_class(tree.r)

def inorder_li(tree):
    if(type(tree) != list):
        if(tree != None):
            print(tree)
    else:
        inorder_li(tree[1])
        print(tree[0])
        inorder_li(tree[2])

def inorder_li2(tree,r):
    if(2*r < len(tree)):
        inorder_li2(tree,2*r)
    print(tree[r])
    if(2*r+1 < len(tree)):
        inorder_li2(tree,2*r+1)

#-----------------------------------inorders-------------------------------------------------------

#-----------------------------------postorders-------------------------------------------------------

def postorder_class(tree):
    if(tree.r == None and tree.l == None):
        print(tree.num)
    else:
        postorder_class(tree.l)
        postorder_class(tree.r)
        print(tree.num)

def postorder_li(tree):
    if(type(tree) != list):
        if tree != None:
            print(tree)
    else:
        postorder_li(tree[1])
        postorder_li(tree[2])
        print(tree[0])


def postorder_li2(tree,r):
    if 2*r < len(tree):
        postorder_li2(tree,2*r)
    if 2*r+1 < len(tree):
        postorder_li2(tree,2*r+1)
    print(tree[r])


#-----------------------------------postorders-------------------------------------------------------
def main():
    #-----------------------------------Preorders------------------------------------------------------
    print("preorders:",end = '\n\n')
    x = binTree(3,None,None)
    x.l= binTree(2,binTree(10),binTree(7))
    x.r = binTree(4,binTree(3),binTree(9))
    preorder_class(x)
    print("")

    tree = [3,[2,10,7],[4,3,9]]
    preorder_li(tree)
    print("")

    tree2 = ['?',3,2,4,10,7,3,9]
    preorder_li2(tree2,1)
    print("")
    #-----------------------------------Preorders------------------------------------------------------

    #-----------------------------------inorders-------------------------------------------------------
    print("inorders",end = '\n\n')
    inorder_class(x)
    print("")
    inorder_li(tree)
    print("")
    inorder_li2(tree2,1)
    print("")

    #-----------------------------------postorders-------------------------------------------------------
    print("postorder:",end = '\n\n')
    postorder_class(x)
    print("")
    postorder_li(tree)
    print("")
    postorder_li2(tree2,1)
    
    

    
    

main()
