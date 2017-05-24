public class Solution {
	public int gcd(int a, int b) {
	    int min = (a < b) ? a : b;
	    int max = (a < b) ? b : a;
	    
	    if (max == min) {
	        return min;
	    }
	    
	    if (min == 0) {
	        return max;
	    }
	    
	    if (min == 1) {
	        return 1;
	    }
	    
	    return gcd(max - min, min);
	}
}
