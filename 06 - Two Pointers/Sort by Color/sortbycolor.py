class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        
        l,r = 0,len(A)-1
        while(l < r):
            if A[l] == 0:
                l += 1
                continue
            while A[r] != 0 and l < r:
                r -= 1
            if l < r:
                A[r] = A[l]
                A[l] = 0
            r -= 1
            l += 1
        
        l,r = 0,len(A)-1
        while(l < r):
            if A[l] != 2:
                l += 1
                continue
            while A[r] != 1 and l < r:
                r -= 1
            if l < r:
                A[r] = A[l]
                A[l] = 1
            r -= 1
            l += 1
            
        return A
                    
