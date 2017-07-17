# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        def llen(hd):
            count = 0
            while hd != None:
                hd,count  = hd.next,count+1
            return count
            
        L = llen(A)
        B = max(B,1)
        B = min(B,L)
        victimIdx = L - B
        
        res = A
        if victimIdx == 0:
            res = A.next
        
        i,prev,cur = 0,None,A
        while i < victimIdx:
            i,prev,cur = i+1,cur,cur.next
        if prev != None:
            prev.next = cur.next
        cur.next = None
        
        return res
        
