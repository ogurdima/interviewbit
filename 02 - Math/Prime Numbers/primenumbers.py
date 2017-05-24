class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
        allNumbers = [True] * (A + 1)
        
        allNumbers[0] = allNumbers[1] = False
        
        for i in range(2, A + 1) :
            if allNumbers[i] == False :
                continue
            tmp = 2
            while tmp * i <= A :
                allNumbers[tmp * i] = False
                tmp = tmp + 1
        
        res = []
        for i in range(0, A + 1) :
            if allNumbers[i] == True :
                res.append(i)
        
        return res
        
    