# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        lenA = 0
        tmp = A
        while tmp != None :
            tmp = tmp.next
            lenA = lenA + 1
        
        lenB = 0
        tmp = B
        while tmp != None :
            tmp = tmp.next
            lenB = lenB + 1
        
        if lenA > min(lenA, lenB) :
            A = self.wind(A, lenA - min(lenA, lenB))
        
        if lenB > min(lenA, lenB) :
            B = self.wind(B, lenB - min(lenA, lenB))
            
        tmpA = A
        tmpB = B
        while tmpA != None :
            
            if tmpA == tmpB :
                return tmpA
            
            tmpA = tmpA.next
            tmpB = tmpB.next
        
        return None
        
    def wind(self, A, n) :
        i = 0
        while i < n :
            i = i + 1
            A = A.next
        return A
        
    
