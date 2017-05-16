class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        n = len(A) - 1
        h = int(math.floor(math.sqrt(n)))
        rangecount = [0] * (h+1)
        numcount = {}
        
        print str((n,h))
        #return -1
        
        for i in range(len(A)):
            ri = A[i] / h
            #print ri
            rangecount[ri] += 1
        
        print map(str,rangecount)
        
        for ri in range(len(rangecount)):
            if rangecount[ri] > h:
                for i in range(len(A)):
                    rj = A[i] / h
                    if rj == ri:
                        if A[i] in numcount:
                            return A[i]
                        numcount[A[i]] = 1
                        
        return -1
