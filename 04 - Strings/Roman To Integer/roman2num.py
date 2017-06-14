class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        num = 0
        last = len(A) - 1
        needToSkip = False
        
        for i in range(0, len(A)):
            if (needToSkip):
                needToSkip = False
                continue
            cur = self.translateChar(A[i])
            if i == last:
                return num + cur
            
            needToSkip = True
            nxt = self.translateChar(A[i+1])
            
            if (nxt == 10 or nxt == 5) and cur == 1:
                num = num + nxt - cur
                continue
            if (nxt == 50 or nxt == 100) and cur == 10:
                num = num + nxt - cur
                continue
            if (nxt == 500 or nxt == 1000) and cur == 100:
                num = num + nxt - cur
                continue
            needToSkip = False
            num = num + cur
         
        return num
    
    def translateChar(self, nextchar):
        cur = 0
        if nextchar == 'I':
            cur = 1
        if nextchar == 'V':
            cur = 5
        if nextchar == 'X':
            cur = 10
        if nextchar == 'L':
            cur = 50
        if nextchar == 'C':
            cur = 100
        if nextchar == 'D':
            cur = 500
        if nextchar == 'M':
            cur = 1000
        return cur
        
        