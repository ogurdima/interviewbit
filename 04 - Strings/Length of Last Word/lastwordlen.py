class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        lastwordlen = 0
        thiswordlen = 0
        for i in range(len(A)):
            if A[i] == ' ':
                if thiswordlen != 0:
                    lastwordlen = thiswordlen
                    thiswordlen = 0
                continue
            thiswordlen += 1
        if thiswordlen > 0:
            return thiswordlen
        return lastwordlen
            
            