# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        if A==None or A.next == None:
            return A
        
        nodeCount = 1  
        tmp = A
        while tmp.next != None:
            tmp = tmp.next
            nodeCount += 1
        
        B = B % nodeCount
        if B == 0:
            return A
        
        count = 0
        hd,prev = A,None
        newHdIdx = nodeCount - B
        
        
        while count < newHdIdx:
            prev = hd
            hd = hd.next
            count += 1
        
        if prev != None:
            prev.next = None
            
        tmp = hd
        while tmp.next != None:
            tmp = tmp.next
        tmp.next = A
        
        return hd
        
        
