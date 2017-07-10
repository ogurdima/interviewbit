# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param m : integer
    # @param n : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, m, n):
        if (n == m) :
            return A
        m = m - 1
        n = n - 1
        
        beforeM = None
        atM = None
        atN = None
        afterN = None
        prev = None
        
        cur = A
        i = 0
        while cur != None :
            nxt = cur.next
            if i == m :
                #print "m"
                beforeM = prev
                atM = cur
                cur.next = None
            if (i > m and i <= n) :
                #print "rev"
                cur.next = prev
            if i == n :
                #print "n"
                atN = cur
                afterN = nxt
                break
            
            prev = cur
            cur = nxt
            i = i + 1
        
        #print "%s %s %s %s" % (self.safe(beforeM), self.safe(atM), self.safe(atN), self.safe(afterN))
        
        if beforeM != None:
            beforeM.next = atN
        if atM != None:
            atM.next = afterN
        if beforeM != None:
            return A
        return atN
        
        
    def safe(self, A) :
        if A == None:
            return "None"
        return A.val
