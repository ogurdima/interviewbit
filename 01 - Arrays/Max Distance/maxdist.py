class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        lm = [0] * len(A)
        rm = [0] * len(A)
        
        cmin = A[0]
        cmax = A[-1]
        for i in range(0,len(A)):
            cmin = min(cmin,A[i])
            lm[i] = cmin
        
        for i in reversed(range(0,len(A))):
            cmax = max(cmax,A[i])
            rm[i] = cmax
            
        i,j = 0,0
        
        cmax = -1
        
        while i < len(A) and j < len(A):
            if A[i] <= A[j]:
                cmax = max(cmax, j-i)
            if lm[i] > rm[j]:
                i += 1
            else:
                j += 1
                
        return cmax
            
        
    def maximumGapBF(self, A):
        cmax = -1
        for i in range(0, len(A)):
            s = i + cmax
            if cmax == -1:
                s += 1
            for j in range(s, len(A)):
                if A[j] >= A[i]:
                    cmax = max(cmax, j-i)
        
        return cmax
            
