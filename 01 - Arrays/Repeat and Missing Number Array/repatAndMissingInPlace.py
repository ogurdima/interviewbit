class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        S = float(reduce(lambda x,y: x + y, A))
        SS = float(reduce(lambda x,y: x + y, map(lambda x: x**2,A)))
        tS = float(len(A) * (1 + len(A)) / 2)
        tSS = float(reduce(lambda x,y: x + y**2, range(1,len(A)+1)))
        dS = S - tS
        dSS = SS - tSS
        
        m = (dSS - dS**2) / (2 * dS)
        r = dS + m
        return [int(r), int(m)]
