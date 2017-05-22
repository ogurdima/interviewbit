class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        histo = [0] * len(A)
        for i in range(len(A)):
            histo[A[i]-1] += 1
        
        missing,repeating = 0,0
        for i in range(len(A)):
            if histo[i] == 0:
                missing = i + 1
            if histo[i] == 2:
                repeating = i + 1
                
        return [repeating, missing]