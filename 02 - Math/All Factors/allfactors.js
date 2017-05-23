module.exports = { 
	//param A : integer
	//return a array of integers
	allFactors : function(A){
        var res = [];
        var other = [];
        var stop = Math.sqrt(A);
        for (var i = 0; i <= stop; i++) {
            if (A % i == 0) {
                res.push(i);
                if (i * i != A) {
                    other.push(A / i);
                }
            }
        }
        return res.concat(other.reverse());
	}
};
