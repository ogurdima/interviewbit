import re
import string

class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        aNumPattern = re.compile("[A-Z]|[a-z]|[0-9]");
        right = len(A) - 1;
        left = 0;
        while (left < right):
            while not aNumPattern.match(A[left]) and left < right:
                left+=1;
            while not aNumPattern.match(A[right]) and left < right:
                right-=1;
            #print "i:" + `left` + "|" + `right` + "\n"
            if left > right :
                return 1
            #print `A[left]` + "|" + `A[right]` + "\n"
            if A[left].upper() != A[right].upper() :
                return 0
            left+=1
            right-=1
        return 1
            
           
