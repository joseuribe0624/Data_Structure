def f(tree):
    if type(tree) == int:
        return tree
    elif tree[0] == '+':
        ans = 0
        values = []
        for i in range(1,len(tree)):
            val = f(tree[i])
            ans += val
        return ans
    elif tree[0] == '*':
        ans = 1
        values =[]
        for i in range(1,len(tree)):
            val = f(tree[i])
            ans *= val
        return ans
    elif tree[0] == '-':
        ans = 0
        values =[]
        for i in range(1,len(tree)):
            val = f(tree[i])
            ans -= val
        return ans
    elif tree[0] == '/':
        ans = 1
        values =[]
        for i in range(1,len(tree)):
            val = f(tree[i])
            val /= val
        return ans


def main():
    op = ['*',['+',['*',['+',7,['*',2,4]],1],['*',-1,['+',['+',1,0],2]]],['+',3,0]]
    
    print(f(op))
main()
