from sys import stdin

def kmp_prefix(s):
    n = len(s)
    P = [None]*n
    i,j = 0,-1
    P[0] = -1
    while i < n-1:
        while j> -1 and s[i] != s[j]:
            j = P[j]
        i += 1
        j += 1
        if s[i] == s[j]:
            P[i] = P[j]
        else:
            P[i] = j
    return P

def kmp_search(s1,s2):
    i,j = 0,0
    P = kmp_prefix(s1)
    while j < len(s2):
        while i > -1 and s1[i] != s2[j]:
            i = P[i]
        i += 1
        j += 1
        if i >= len(s1):
            print(i)
            return True

            
    return False


def main():
    #print(kmp_prefix("o"))
    print(kmp_search("hel","heyhelloyou"))
    word='*mneo*aaaa****'
    print(word.strip("*").split("*"))
    word2="heyhelloyou"
    print(word2[5:])

main()
    
    
