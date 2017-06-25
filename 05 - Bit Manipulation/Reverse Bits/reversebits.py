class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        res = 0
        for i in range(32):
            res += (A % 2)
            if i != 31:
                res *= 2
                A /= 2
        return res