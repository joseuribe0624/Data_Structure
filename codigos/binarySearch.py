def search(a,lo, hi, x):
	if hi - lo == 0:
		return -1
	elif  hi-lo == 1:
		if a[lo] == x: return lo
		else: return -1

	mid = (lo+hi)//2

	if x < a[mid]:
		return search(a, lo, mid, x)
	elif a[mid] < x:
		return search(a, mid, hi, x)
	else:
		i = search(a, lo, mid, x)
		if i == -1: return mid
		else: return i

def lower(serie,target,hi,index=0,):
	
	start = 0
	end = hi
	while start <= end:
		mid = start + (end - start)//2
		if serie[mid] <= target and serie[mid] < serie[index]:
			return mid
		else:
			if target >= serie[mid]:
				index=mid
			if serie[mid] <= target:
				start = mid +1
			else:
				end = mid -1
	return index

def binarySearch(sequence,lo, hi, x):
	if hi - lo == 0:
		return -1
	elif  hi-lo == 1:
		print(sequence[lo] + "<="+ target +"y"+ sequence[lo]+"<"+ senquence[mid])
		if sequence[lo] <= target and sequence[lo] < senquence[mid]: return lo
		else: return -1

	mid = (lo+hi)//2

	if x < sequence[mid]:
		return search(sequence,lo, mid, x)
	elif sequence[mid] < x:
		return search(sequence,mid, hi, x)
	else:
		i = search(sequence,lo, mid, x)
		if i == -1: return mid
		else: return i

def binsearch(A,x):
    N = len(A)
    assert N >= 1
    low,hi = 0,N
    
    while(low+1 != hi):
        mid = low+((hi-low)>>1)
        if(x < a[mid]):
            hi = mid
        else:
            low = mid
    return A[low]

b = [2,4,6]
print("binary 1")
print(binsearch(b,5))


print(a)
print(search(a, 0, len(a), 4))
print("sigue")
print(lower(a,3,len(a)))
print("termina")

print("sigue2")
print(binarySearch(a,0,len(a),6))
print("termina")


input()

def sub_mid(a, lo, mid, hi):
	best_left = acum = 0
	for i in range(mid-1, lo-1, -1):
		acum+= a[i]
		best_left = max(best_left, acum)

	best_right = acum = 0
	for i in range(mid, hi):
		acum+= a[i]
		best_right = max(best_right, acum)
	return best_left + best_right

def sub_arr_sum(a,lo, hi):
	if lo==hi:
		return 0
	elif lo+1==hi:
		return max(0, a[lo])

	mid = (lo+hi)>>1
	ans_left = sub_arr_sum(a, lo, mid)
	ans_right = sub_arr_sum(a, mid, hi)
	ans_mid =  sub_mid(a, lo, mid, hi)

	return max(ans_left, ans_right, ans_mid)