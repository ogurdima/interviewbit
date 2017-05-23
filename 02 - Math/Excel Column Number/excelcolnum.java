public class Solution {
	public int titleToNumber(String a) {
	    if (a.equals("") ){
	        return 0;
	    }
	    char[] title = a.toCharArray();
	    int result = 0;
	    int multiplier = 1;
	    for (int i = 0; i < title.length; i++) {
	        result *= 26;
	        int curValue = (int)title[i] - (int)'A' + 1;
	        result += curValue;
	    }
	    return result;
	}
}
