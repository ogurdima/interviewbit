class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        def comp(s1,s2):
            return cmp(s1+s2, s2+s1)
        strings = sorted(map(str,A), comp)[::-1]
        #print " ".join(strings)
        res = "".join(strings)
        if int(res) == 0:
            return 0
        return res
