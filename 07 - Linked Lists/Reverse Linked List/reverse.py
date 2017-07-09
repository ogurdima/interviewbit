# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        prev = None
        cur = A
        
        while cur != None :
            oldnext = cur.next
            cur.next = prev
            prev = cur
            cur = oldnext
        
        return prev