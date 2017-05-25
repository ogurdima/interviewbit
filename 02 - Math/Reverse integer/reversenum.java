public class Solution {
	public int reverse(int a) {
	    boolean needToNegate = false;
	    if (a < 0)
	    {
	        needToNegate = true;
	        a = -a;
	    }
	    
	    int multiplier = 1;
	    int tmp = a;
	    while (tmp > 0) {
	        tmp /= 10;
	        if (tmp != 0)
	        {
	            multiplier *= 10;
	        }
	    }
	    
	    //System.out.println("multiplier: " + multiplier);

	    int result = 0;
	    tmp = a;
	    while (tmp > 0) {
	        int digit = (tmp % 10);
	        int newRes = result + digit * multiplier;
	        if ((digit * multiplier) / multiplier != digit) {
	            return 0;
	        }
	        //System.out.println("new: " + newRes + " old: " + result);
	        if (newRes < result) {
	            //System.out.println("Overflow: " + newRes + " " + result);
	            return 0;
	        }
	        result = newRes;
	        //System.out.println("multiplier: " + multiplier +" digit " + digit + " res: " + result);
	        tmp /= 10;
	        multiplier /= 10;
	    }
	    
	    if (needToNegate) {
	        return -result;
	    }
	    return result;
	}
}

