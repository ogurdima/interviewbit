class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        B = A[:]
        C = A[:]
        for i in range(len(A)):
            B[i] += i
            C[i] -= i
        
        return max(max(B) - min(B), max(C) - min(C))
        
        
