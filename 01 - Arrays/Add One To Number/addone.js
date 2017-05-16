module.exports = { 
	//param A : array of integers
	//return a array of integers
	plusOne : function(A){
        var B = A.slice();
        var lsb = B.length - 1;
        var msb = 0;
        while (A[msb] == 0 && msb < lsb) {
            msb++;
        }
        if (msb == lsb) {
            if (A[lsb] < 9) {
                return [A[lsb] + 1];
            }
            return [1, 0];
        }
        var carry = true;
        for (var i = lsb; i >= msb; i--) {
            if (carry) {
                B[i]++
            }
            carry = false;
            if (B[i] == 10) {
                B[i] = 0;
                carry = true;
            }
        }
        
        var res = [];
        if (carry) {
            res = [1];
        }
        for (var i = msb; i <= lsb; i++)
        {
            res.push(B[i]);
        }
        return res;
	}
};
