class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        res = [[1 for j in range(i+1)] for i in range(A)]
        for i in range(1,A):
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res