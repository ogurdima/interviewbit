class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        A.sort()
        N = len(A)
        res = []
        for i in range(N) :
            target = -A[i]
            left = i + 1
            right = N - 1
            while left < right :
                if A[left] + A[right] == target :
                    item = [A[i], A[left], A[right]]
                    if item not in res:
                        res.append([A[i], A[left], A[right]])
                if A[left] + A[right] < target :
                    left = left + 1
                else :
                    right = right -1
        return res
        

