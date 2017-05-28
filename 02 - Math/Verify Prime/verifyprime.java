public class Solution {
	public int isPrime(int a) {
	    if (a < 2) {
	        return 0;
	    }
	    int stop = Math.max(2,(int)Math.ceil(Math.sqrt(a)));
	    for (int i = 2; i <= stop; i++) {
	        if (a % i == 0) {
	            return 0;
	        }
	    }
	    return 1;
	}
}
