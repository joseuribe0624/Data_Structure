


def suffix(s):
    n = len(s)
    suffixes = [(s[i:],i) for i in range(n)] #O(n̈́2)
    suffixes.sort()
    suffixarr = [i for w,i in suffixes]
    return suffixarr


def suffix_arr(s): #O(n * log2(n))
    l = list(set(s))
    l.sort()
    n = len(s)
    d = {l[i]:i for i in range(len(l))}
    next_level = [d[s[i]] for i in range(n)]
    #lvl1 = [lvl0[i]*(n+1) + (1+lvl0[i+1] if i+1<n else 0) for i in range(n)]
    N = 2*n
    k = 1
    while N > 0:
        next_level  = [next_level[i]*(n+1) +(1+next_level[i+k] if i+k<n else 0)
                       for i in range(n)]
        
        l = list(set(next_level))
        l.sort()
        d = {l[i]:i for i in range(len(l))}
        next_level = [d[next_level[i]] for i in range(n)]
        N //=2
        k *= 2
        
    return next_level


def suffix_arr_util(s):
    n = len(s)
    last_level = suffix_arr(s)
    SA = [None]*n
    for i in range(n):
        SA[last_level[i]] = i
    return SA,last_level
def main():
    #print(suffix("cocoloco"))
    s = "cocoloco"
    SA,d = suffix_arr_util(s)
    for j in SA:
        print(s[j:])
    

main()
    
    
    

