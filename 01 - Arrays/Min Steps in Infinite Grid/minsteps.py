class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):
        def dist(p1,p2):
            (x1,y1),(x2,y2) = p1,p2
            dx,dy = abs(x1-x2),abs(y1-y2)
            return dx + dy - min(dx,dy)
        
        steps = 0
        pts = zip(X,Y)
        for i in range(1,len(pts)):
            steps += dist(pts[i-1],pts[i])
            
        return steps
