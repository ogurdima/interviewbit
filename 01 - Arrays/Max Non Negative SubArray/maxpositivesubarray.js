module.exports = { 
	//param A : array of integers
	//return a array of integers
	maxset : function(A){
        var cur = {
            sum: 0,
            left: -1,
            right: 0
        };
        var max = {
            sum: -1,
            left: -1,
            right: 0,
        }
        
        for (var i = 0; i < A.length; i++)
        {
            if (A[i] >= 0)
            {
                if (cur.left == -1) {
                    //console.log("Init");
                    cur.left = i;
                    cur.sum = 0;
                }
                //console.log("Add");
                cur.sum += A[i];
                cur.right = i;
                
            }
            
            if (cur.sum > max.sum || (cur.sum == max.sum && cur.right - cur.left > max.right - max.left) ) {
                //console.log("Swap");
                max = cur;
                cur = {
                    sum: max.sum,
                    left: max.left,
                    right: max.right 
                };
            }
            
            if (A[i] < 0) {
                //console.log("Invalidate");
                cur = {
                    sum: 0,
                    left: -1,
                    right: 0
                };
            }
            
        }
        
        var res = [];
        if (max.left >= 0) {
            for (var i = max.left; i <= max.right; i++)
            {
                res.push(A[i]);
            }
        }
        
        //console.log(max);
        
        return res;
	}
};
