class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        valmap = [
            (1000, 'M'), 
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I'),
        ]

        out = ""
        num = A
        for i in valmap:
            while num >= i[0]:
                out += i[1]
                num -= i[0]
        return out
        
        
        
        
        