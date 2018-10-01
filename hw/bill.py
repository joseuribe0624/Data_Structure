from sys import stdin

def cost(n):
	if n <= 100:
		return n*2
	elif n <= 10000:
		return 200+(n-100)*3
	elif n <= 1000000:
		return 29900 + (n-10000)*5
	else:
		return 4979900 + (n-1000000)*7


def solve(tsum, diff):
	i=0
	c=tsum
	total=0
	while i <= c:
		m = (i + c)>>1
		cobro = cost(m)
		if cobro == tsum:
			total = m
			break
		elif cobro < tsum:
			i = m+1
		else:
			c = m-1
	i=0
	c = total
	while i <= c:
		m = (i+c)>>1
		you = cost(m)
		neighbour = cost(total-m)
		if (neighbour-you) == diff:
			return you
		elif (neighbour - you) < diff:
			c = m-1
		elif you > neighbour:
			c=m-1
		else:
			i = m+1;


def main():
  tsum,diff = map(int,stdin.readline().split())
  while tsum+diff!=0:
    print(solve(tsum, diff))
    tsum,diff = map(int,stdin.readline().split())

main()
