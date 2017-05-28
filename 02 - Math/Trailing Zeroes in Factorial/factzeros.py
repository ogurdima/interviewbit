class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        factors = [0,0]
        i = -1
        for n in [2,5]:
            i += 1
            tmp = A
            while tmp > 0:
                tmp = tmp / n
                factors[i] += tmp
                
        return min(factors)
