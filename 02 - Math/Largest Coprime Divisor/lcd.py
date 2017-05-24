class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cpFact(self, A, B):
        def gcd(A, B):
            if B>A:
                A, B = B, A
            while B != 0:
                temp = B
                B = A % B
                A = temp
            return A
        
        tmp = A   
        cmn = gcd(tmp,B)
        while cmn != 1:
            tmp = tmp / cmn
            cmn = gcd(tmp,B)
        return tmp
        
        
        
