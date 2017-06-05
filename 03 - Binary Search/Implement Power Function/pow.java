public class Solution {
	public int pow(int x, int n, int d) {
	    long res = 1;
	    if (x == 0) {
	        return 0;
	    }
	    if (n == 0) {
	        return 1;
	    }
	    long tmpX = x % d;
	    while (n > 1) {
	        if (n % 2 == 0) {
	            tmpX = (tmpX * tmpX) % d;
	            n = n / 2;
	            continue;
	        }
	        res = (tmpX * res) % d;
	        tmpX = (tmpX * tmpX) % d;
	        n = (n-1) / 2;
	    }
	    long tmpRes = (tmpX * res) % d;
	   // System.out.println("tmpRes: " + tmpRes);
	   // System.out.println("res: " + res);
	   // System.out.println("tmpX: " + tmpX);
	    while (tmpRes < 0) {
	        tmpRes += d;
	    }
	    return (int)tmpRes;
	}
}
