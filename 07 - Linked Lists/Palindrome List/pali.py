# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        
        L = 0
        tmp = A
        while tmp != None:
            L += 1
            tmp = tmp.next
        mid = L / 2
        
        prevnext = A.next
        tmp = A
        prev = None
        for count in range(0,mid):
            prevnext = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = prevnext
            
        if L % 2 == 1:
            tmp = tmp.next
        
        v1 = tmp
        v2 = prev
        
        while v1 != None:
            if v2 == None:
                return 0
            if v1.val != v2.val:
                return 0
            v1 = v1.next
            v2 = v2.next
        
        if v2 == None:
            return 1
        return 0
        
        