from sys import stdin,setrecursionlimit
import sys

setrecursionlimit(10000)

def solve(low, hi, ans):
	global tree
	if low < hi:
		mid = low+1
		while mid != hi and tree[mid] < tree[low]:
			mid+=1
	
		solve(low+1,mid,ans)
		solve(mid,hi,ans)
		ans.append(tree[low])
	return ans


def main():
	global tree
	#pre-order <root,left,right>
	#post-order <left,rigth,root>
	tree = []
	node = int(stdin.readline())
	#pre order tree
	tree.append(node)
	while node:
		try:
			node = int(stdin.readline())
			tree.append(node)
		except ValueError:
			break
	low=0
	#print(tree)
	hi=len(tree)
	ans=[]
	postOrder=solve(low,hi,ans)

	for i in range(len(postOrder)):
		print(postOrder[i])
	
	return 0

main()