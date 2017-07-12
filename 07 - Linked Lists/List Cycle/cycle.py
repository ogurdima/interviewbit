# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        if A == None :
            return None
        slow = A
        fast = A.next
        
        while fast != None :
            fast = fast.next
            if slow == fast :
                break
            slow = slow.next
            if fast != None :
                fast = fast.next
        
        if fast == None :
            return None
            
        tmp = slow.next
        loopLen = 1
        while tmp != slow :
            loopLen = loopLen + 1
            tmp = tmp.next
        
        if loopLen == 1 :
            return slow
        
        candidate = A
        test = candidate
        for i in range (loopLen) :
            test = test.next
            
        while candidate != test :
            candidate = candidate.next
            test = test.next
            
        return candidate
