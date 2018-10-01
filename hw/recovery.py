from sys import stdin,setrecursionlimit
import sys

setrecursionlimit(10000)

#jose david gutierrez
def solve(inOrder,preOrder):
	global ans
	if len(inOrder) == 1:
		ans.append(preOrder[0])
	elif len(inOrder) > 1:
		mid = inOrder.index(preOrder[0])
		solve(inOrder[:mid],preOrder[1:mid+1])
		solve(inOrder[mid+1:],preOrder[mid+1:])
		ans.append(preOrder[0])
	

def main():
	global ans
	trasversal= [str(i) for i in stdin.readline().strip().split() ]
	while len(trasversal) != 0:
		ans=[]
		preOrder = trasversal[0]
		inOrder = trasversal[1]
		solve(inOrder,preOrder)
		for i in ans:
			print(i, end='')
		print()
		trasversal= [str(i) for i in stdin.readline().strip().split() ]
		
	
main()