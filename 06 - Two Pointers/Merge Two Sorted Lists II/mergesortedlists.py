class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return A modified after the merge
    def merge(self, A, B):
        ib = 0
        ia = 0
        
        res = []
        
        while (ia < len(A) and ib < len(B)) :
            if (A[ia] <= B[ib]) :
                res.append(A[ia])
                ia = ia + 1
                continue
            res.append(B[ib])
            ib = ib + 1
        
        while (ia < len(A)) :
            res.append(A[ia])
            ia = ia + 1
        
        while (ib < len(B)) :
            res.append(B[ib])
            ib = ib + 1
            
        
        A = res
        return A
            
