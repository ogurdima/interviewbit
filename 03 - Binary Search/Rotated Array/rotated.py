class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        
        def findPivot(arr, left, right):
            if left >= right:
                return right
            if arr[left] <= arr[right]:
                return left
            if right - left == 1:
                return right
                
            mid = (left + right) / 2
            #print "%d %d %d" % (arr[left],arr[mid],arr[right])
            if arr[left] > arr[mid]:
                return findPivot(arr, left, mid)
            return findPivot(arr, mid, right)
        
        pivotIdx = findPivot(A, 0, len(A)-1)
        return A[pivotIdx]
    
