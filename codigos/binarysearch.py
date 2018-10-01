#busqueda binaria
def binsearch(A, x):
	"""A is order ascending and contains numbers x is a number this functions
	checks if x is an element of A"""

	N = len(A)
	#asser N>=1
	low,hi = 0,N
	while low+1 != hi:
		mid = low+((hi-low)>>1)
		if x<A[mid]:hi=mid
		else: low = mid



	return A[low]==x