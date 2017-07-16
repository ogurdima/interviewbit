# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        tmp = A
        
        smallHead = None
        smallTmp = None
        
        largeHead = None
        largeTmp = None
        
        prev = None
        
        while tmp != None:
            nxt = tmp.next
            tmp.next = None
            if tmp.val < B :
                if smallHead == None :
                    smallHead = tmp
                    smallTmp = smallHead
                else :
                    smallTmp.next = tmp
                    smallTmp = tmp
            else :
                if largeHead == None:
                    largeHead = tmp
                    largeTmp = largeHead
                else :
                    largeTmp.next = tmp
                    largeTmp = tmp
            tmp = nxt
        
        #print "Small: %d" % self.count(smallHead)
        #print "Large: %d" % self.count(largeHead)
        
        
        if smallTmp == None :
            return A
        smallTmp.next = largeHead
        return smallHead
    
    def cutNext(self, prev, cur):
        #print "Cut %d from %s" % (cur.val, prev)
        n = cur.next
        if prev != None :
            prev.next = n
        cur.next = None
        return n
        
    def count(self, A):
        temp = 0
        while A != None :
            temp = temp + 1
            A = A.next
        return temp
