# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        head = None
        
        if A == None :
            return B
        if B == None :
            return A
        if A.val < B.val :
            head = A
            A = A.next
        else :
            head = B
            B = B.next
        
        cur = head
        
        while A != None and B != None :
            
            if A.val < B.val :
                cur.next = A
                cur = A
                A = A.next
            else :
                cur.next = B
                cur = B
                B = B.next
            
        while A != None :
            cur.next = A
            cur = A
            A = A.next
            
        while B != None :
            cur.next = B
            cur = B
            B = B.next
            
        
        return head
            
            
            
            
            
            
