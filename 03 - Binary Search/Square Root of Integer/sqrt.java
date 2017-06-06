public class Solution {
	public int sqrt(int a) {
	    if (a == 1) {
	        return 1;
	    }
	    if (a == 0) {
	        return 0;
	    }
	    long left = 1;
	    long right = a;
	    long mid = 0;
	    while (left < right) {
	        long sum = (left + right);
	        //System.out.println("sum:" + sum); 
	        mid = sum / 2;
	        //System.out.print("l:" + left + " m:" + mid + " r:" + right + " ") ;
	        if (mid == left || mid == right) {
	            //System.out.println("here1");
	            return (int)mid;
	        }
	        long squared = mid * mid;
	        long nextSquared = (mid + 1) * (mid + 1);
	        if (squared == a || (squared < a && nextSquared > a)) {
	            //System.out.println("here2");
	            return (int)mid;
	        }
	        if (squared < a) {
	            left = mid;
	            continue;
	        }
	        right = mid;
	        continue;
	    }
	    //System.out.println("here3");
	    //System.out.println("left: " + left + " mid: " + mid + " right: " + right);
	    return (int)mid;
	    
	}
}
