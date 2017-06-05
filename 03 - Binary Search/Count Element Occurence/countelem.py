class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        def searchLeft(arr, elem):
            left = 0
            right = len(arr)-1
            resIdx = -1
     
            while(left <= right):
                mid = (left + right) / 2
                #print str((arr[left],arr[mid],arr[right]))
                if elem <= arr[mid]:
                    if elem == arr[mid] : resIdx = mid
                    right = mid - 1
                    continue
                left = mid + 1
                    
            return resIdx
            
        def searchRight(arr, elem):
            left = 0
            right = len(arr)-1
            resIdx = -1
     
            while(left <= right):
                mid = (left + right) / 2
                if elem >= arr[mid]:
                    if elem == arr[mid]: resIdx = mid
                    left = mid + 1
                    continue
                right = mid - 1
                    
            return resIdx
            
        lidx = searchLeft(A,B)
        ridx = searchRight(A,B)
        
        #print str((lidx,ridx))
        
        if lidx == -1 or ridx == -1: 
            return 0
        
        return ridx-lidx+1

