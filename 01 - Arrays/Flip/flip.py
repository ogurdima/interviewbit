class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        mStart = -1
        mEnd = -1
        mCount = -1
        
        cStart = 0
        cCount = 0
        
        for i in range(len(A)):
            if cCount < 0:
                cCount = 0
                cStart = i
            if A[i] == '0':
                cCount += 1
                if cCount > mCount:
                    mStart = cStart
                    mEnd = i
                    mCount = cCount
            if A[i] == '1':
                cCount -= 1
        
        if mCount == -1:
            return []
        return [mStart+1, mEnd+1]
