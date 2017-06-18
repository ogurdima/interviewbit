class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        words = A.split()
        for w in words:
            w = w[::-1]
        return ' '.join(list(reversed(words)))
