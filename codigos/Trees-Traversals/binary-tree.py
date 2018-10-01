
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



def print_tree(tree):#el de listas de listas
    if type(tree) != list:
        if(tree != None):
            print(tree, end = '')
    else:
        print('(', end = '')
        print_tree(tree[1])
        print(') ', end = '')
        print(tree[0],end = '')
        print(' (',end = '')
        print_tree(tree[2])
        print(')',end = '')
    return 

def in_order(tree,r):

    if 2*r < len(tree):
        print('(',end = '')
        in_order(x,2*r)
        print(')',end = '')
    print(x[r], end = '')

    if 2*r+1 < len(tree):
        print('(',end = '')
        in_order(tree,2*r+1)
        print(')',end = '')
    
    

def main():
    #como listas de listas
    tree = [3,[2,10,7],[4,None,9]]
    #con clases
    x = binTree(3,None,None)
    x.l= binTree(2,binTree(10),binTree(7))
    x.r = binTree(4,binTree(3),binTree(9))

    #con un solo arreglo
    x = ['?',3,2,4,10,7,3,9]

    print_tree(tree)
    print("\n")
    """
    x = binTree()
    x.num = 3
    x.l = binTree()
    x.l.num = 2
    
    x.l.l = binTree()
    x.l.l.num = 10

    x.l.r = binTree()
    x.l.r.num = 7

    x.r = binTree()
    x.r.num = 4

    x.r.l = binTree()
    x.r.l = 3

    x.r.r = binTree()
    x.r.r.num = 9
    """

    print(x)
    
    
    
main()
