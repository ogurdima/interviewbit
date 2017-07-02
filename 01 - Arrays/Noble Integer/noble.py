class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        data = sorted(A)
        for i in range(len(data)):
            r = len(data) - i - 1
            if data[i] == r and (r == 0 or data[i] != data[i+1]):
                return 1
        return -1
