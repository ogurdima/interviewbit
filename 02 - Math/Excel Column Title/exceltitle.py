class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        num = A
        res = ""
        while num > 0:
            resid = num % 26
            num = num / 26
            if resid == 0:
                num -= 1
                resid = 26
            res = chr(ord('A') + resid - 1) + res
        return res
            
