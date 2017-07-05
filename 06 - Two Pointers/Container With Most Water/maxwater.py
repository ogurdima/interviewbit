class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        bestArea = (len(A) - 1) * min(A)
        
        left = 0
        right = len(A) - 1
        
        while (left < right) :
            #print "%d %d" % (left, right)
            curArea = (right - left) * min(A[left], A[right])
            bestArea = max(bestArea, curArea)
            
            
            if (A[right] > A[left]) :
                left = left + 1
                continue
            
            right = right - 1
            
        return bestArea
        
