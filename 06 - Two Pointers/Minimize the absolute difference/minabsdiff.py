class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        la = 0
        lb = 0
        lc = 0
        
        ra = len(A) - 1
        rb = len(B) - 1
        rc = len(C) - 1
        
        best = 999999

        while la <= ra or lb <= rb or lc <= rc :
            #print "%d %d %d" % (la,lb,lc)
            lv = self.val(A[la],B[lb],C[lc])
            if lv < best:
                #print "Updating best to %d" % lv
                best = lv

            if min(A[la],B[lb],C[lc]) == A[la] :
                if (la == ra) :
                    break
                la = la + 1
                continue
            if min(A[la],B[lb],C[lc]) == B[lb] :
                if (lb == rb) :
                    break
                lb = lb + 1
                continue
            if min(A[la],B[lb],C[lc]) == C[lc] :
                if (lc == rc) :
                    break
                lc = lc + 1
                continue
            
        #print "Best is %d" % best
        return best
            
    
    def val(self, x, y, z) :
        return abs(max(x,y,z) - min(x,y,z))
            
        
   
