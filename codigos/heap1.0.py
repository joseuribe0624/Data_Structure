import random

def bin_search(Q,x):
	N=len(Q)
	low,hi=0,N
	while(low+1 != hi):
		mid=low+((hi-low)>>1)
		if(x<Q[mid]):
			low=mid
		else:
			hi=mid


def push(0,x):
	j=bin_search(0,x)
	Q[:]=Q[:j]+[x]+Q[j:]



def get_min(Q):
	return Q[-1]

def pop_min(Q):
	return Q.pop()


Q=[]
random.seed(20181003)
for i in range(20):
	push(Q,random.randrange(-20,20))
	print(Q)
	assert(sorted(Q)== Q[::-1])



