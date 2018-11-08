from sys import stdin
#code taken from the class
#jose david gutierrez uribe
class segtree(object):
    def __init__(self, A):
        """Create a segment tree of the given indexed list A"""
        assert len(A) != 0
        self.__size = len(A)
        self.__tree = [None for _ in range(len(A) << 2)]
        self.__init_aux(A, 0, 0, len(A))

    def __init_aux(self, A, i, low, hi):
        assert 0 <= low < hi <= len(self)
        if low + 1 == hi:
            self.__tree[i] = A[low]
        else:
            mid = low + ((hi - low) >> 1)
            self.__tree[i] = self.__init_aux(A, self.__left(i), low, mid)
            self.__tree[i] *= self.__init_aux(A, self.__right(i), mid, hi)
        return self.__tree[i]

    def __len__(self): return self.__size

    def __str__(self): return str(self.__tree)

    def __left(self, i): return 1 + (i << 1)

    def __right(self, i): return (1 + i) << 1

    def update(self, j, x):
        """Update the j-th element of the collection with value x"""
        self.__update_aux(0, 0, len(self), j, x)

    def __update_aux(self, i, low, hi, j, x):
        """Recursively find the corresponding index below the subtree rooted
        at i in the underlying structure for the j-th element of the collection
        between the range [low..hi)"""
        assert 0 <= low < hi <= len(self) and low <= j < hi
        # base case: modify the given position and return the new value
        if low + 1 == hi:
            assert low == j
            self.__tree[i] = x
        # inductive case: choose either left or right, and solve recursively
        else:
            mid, il, ir = low + ((hi - low) >> 1), self.__left(i), self.__right(i)
            if j < mid:
                l, r = self.__update_aux(il, low, mid, j, x), self.__tree[ir]
            else:
                l, r = self.__tree[il], self.__update_aux(ir, mid, hi, j, x)
            self.__tree[i] = l * r
        return self.__tree[i]

    def query(self, low, hi):
        """Query the value for the segment [low..hi) in the collection"""
        assert 0 <= low < hi <= len(self)
        return self.__query_aux(0, 0, len(self), low, hi)

    def __query_aux(self, i, ilow, ihi, low, hi):
        assert 0 <= ilow < ihi <= len(self) << 2 and 0 <= low < hi <= len(self)
        ans = None
        # in this case, the intersection is empty: conquer
        if ihi <= low or hi <= ilow:
            ans = 1
        # [ilow..ihi) is a subset of [low..hi) : conquer
        elif low <= ilow and ihi <= hi:
            ans = self.__tree[i]
        # [ilow..ihi) is just one point ->[this case is subsumed by the previous one]<-
        elif ilow + 1 == ihi:
            ans = self.__tree[i]
        # [ilow..hi) and [low..hi) have some elements in common (and some
        # not in common): divide and conquer
        else:
            imid, il, ir = ilow + ((ihi - ilow) >> 1), self.__left(i), self.__right(i)
            ans = self.__query_aux(il, ilow, imid, low, hi) * self.__query_aux(ir, imid, ihi, low, hi)
        return ans

def main():
    enter = stdin.readline().split()
    while enter:
        N,K = map(int, enter)
        initials = list(map(int, stdin.readline().split()))
        result = segtree(initials)
        for i in range(K):
            values = stdin.readline().split()
            helps = list(map(int, values[1:]))
            commands = [values[0]]
            commands += helps
            if commands[0] == 'P':
                ans = result.query(commands[1] - 1, commands[2])
                if ans < 0:
                    ans = '-'
                elif ans > 0:
                    ans = '+'        
                else:
                    ans = 0
                print(ans, end='')
            else:
                result.update(commands[1] - 1, commands[2])        
        print()
        enter = stdin.readline().split()

main()