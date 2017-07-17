# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        if A == None or A.next == None:
            return A
        
        mem = [None, A, A.next]
        count = 0
        head = A.next
        while mem[-1] != None:
            oldnxt = mem[-1].next
            if count % 2 == 0:
                if mem[-3] != None:
                    mem[-3].next = mem[-1]
                mem[-2].next = oldnxt
                mem[-1].next = mem[-2]
                mem = [mem[-1],mem[-2],oldnxt]
            else:
                mem = [mem[-2],mem[-1],oldnxt]
            count += 1  
            
        return head
