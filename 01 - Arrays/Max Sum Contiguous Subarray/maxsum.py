class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        mSum = -1000000000
        mStart = 0

        cSum = 0
        cStart = 0
        for i in range(len(A)):
            if cSum == 0:
                cStart = i
            cSum += A[i]
            if cSum >= mSum:
                mSum = cSum
                mStart = cStart
            if cSum < 0:
                cSum = 0
        
        return mSum
        
        