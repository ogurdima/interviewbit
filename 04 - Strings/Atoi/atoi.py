import re
import sys

class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        maxInt = 2147483647
        minInt = -2147483648
        result = 0
        seenMinus = False
        seenPlus = False
        numPattern = re.compile("[0-9]")
        wsPattern = re.compile("\s")
        pos = "start"
        for i in range(0, len(A)):
            nextchar = A[i];
            if wsPattern.match(nextchar) :
                if pos == "start":
                    continue
                break
            pos = "notstart"
            if nextchar == '+':
                if seenMinus or seenPlus:
                    break
                seenPlus = True
                continue
            if nextchar == '-':
                if seenMinus:
                    break
                seenMinus = True
                continue
            if nextchar.isdigit() :
                result = result * 10
                result = result + (ord(nextchar) - ord('0'))
                if result < 0 or result > maxInt:
                    if seenMinus:
                        return minInt
                    return maxInt
                continue
            break
        if seenMinus:
            return -result
        return result
        
            
