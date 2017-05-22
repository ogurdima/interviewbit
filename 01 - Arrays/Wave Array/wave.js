module.exports = { 
	//param A : array of integers
	//return a array of integers
	wave : function(A){
	    var res = A.slice();
        res.sort(function(a, b){return a-b});
        //console.log(res);
        for (var i = 1; i < res.length; i += 2) {
            var tmp = res[i];
            res[i] = res[i-1];
            res[i-1] = tmp;
        }
        
        return res;
        
	}
};
