public class Solution {
	public int uniquePaths(int a, int b) {
	    if (a == 0 || b == 0) {
	        return 0;
	    }
	    if (a == 1 || b == 1) {
	        return 1;
	    }
	    int totalSteps = a + b - 2;
	    
	    int min = ((a < b) ? a : b) - 1;
	    int max = (a + b - min) - 2;
	    
	    long nom = 1;
	    for (int i = max + 1; i <= totalSteps; i++) {
	        nom *= i;
	    }
	    
	    long denom = fact(min);
	   
	   // System.out.println("totalSteps = " + totalSteps);
	   // System.out.println("min = " + min + " max = " + max);
	   // System.out.println("n/d = " + nom + " / " + denom);

	    return (int)(nom / denom);
	}
	
	private long fact(int a) {
	    long res = 1;
	    for (int i = 1; i <= a; i++) {
	        res *= i;
	    }
	    return res;
	}
}
