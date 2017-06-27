class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        
        bestToTarget = 999999;
        closestSum = 999999
        
        for i in range(0, len(A)) :
            target = B - A[i]
            twoSum = self.twoSumClosestD(A, target, i)
            if abs(twoSum + A[i] - B) < bestToTarget :
                closestSum = twoSum + A[i]
                bestToTarget = abs(twoSum + A[i] - B)
        
        return closestSum
        
        
    def twoSumClosestD(self, A, target, startIdx) :
        bestToTarget = 999999
        closestSum = 999999
        left = startIdx + 1
        right = len(A) - 1
        
        while (left < right) :
            if abs(A[left] + A[right] - target) < bestToTarget :
                bestToTarget = abs(A[left] + A[right] - target)
                closestSum = A[left] + A[right]
            if A[left] + A[right] == target :
                break;
            if A[left] + A[right] > target :
                right = right - 1
                continue
            left = left + 1
            
        return closestSum
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    