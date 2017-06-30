class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        last = 0
        for i in range(1, len(A)) :
            cur = A[i]
            prev = A[last]
            if (cur != prev) :
                last = last + 1
                A[last] = cur
        
        return last + 1
            
            
