from sys import stdin

INF = float('inf')

#Jose David gutierrez uribe
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
            return j
    return INF

def main():
	enter = stdin.readline().strip()  
	while enter:
		t = str(stdin.readline().strip())
		n = int(enter)
		while n > 0:
			p = str(stdin.readline().strip())
			word=p.strip("*").split("*")
			flag=True
			partition = 0
			past=0
			count = len(word)
			for i in word:
				if i == "":
					continue
				else:
					if t[partition:] == "":
						if p[-1] == "*" and count==0:
							continue
						else:
							flag=False
							break
					actual=kmp_search(i,t[partition:])
					
					if actual == INF:
						
						flag=False
						break
					else:
						partition+=actual
				count-=1

			if flag:
				print("yes")
			else:
				print("no")
			
			n-=1
		enter = stdin.readline().strip()
	
main()