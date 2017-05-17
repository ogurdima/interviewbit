public class Solution {
	// DO NOT MODIFY THE LIST
	public int repeatedNumber(final List<Integer> a) {
	    if (a.size() < 4) {
	        return stupidRepeatedNumber(a);
	    }
	    
	    int x = 0;
	    int xCount = 0;
	    int y = 0;
	    int yCount = 0;
	    
	    //System.out.println("Start: " + xCount + ", " + yCount + ", " + limit);
	    
	    for (int nextIdx = 0; nextIdx < a.size(); nextIdx++)
	    {
	        int next = a.get(nextIdx);
	        if (xCount != 0 && next == x) {
	            xCount++;
                continue;
	        }
	        if (yCount != 0 && next == y) {
	            yCount++;
                continue;
	        }
	        if (xCount == 0)
	        {
	            x = next;
	            xCount++;
	            continue;
	        }
	        if (yCount == 0)
	        {
	            y = next;
	            yCount++;
	            continue;
	        }
	        xCount--;
	        yCount--;
	    }
	    
	    
	    //int limit = (int)Math.ceil((double)a.size() / 3.0);
	    int limit = a.size() / 3;
	    
	    //System.out.println("x: " + x);
	    //System.out.println("y: " + y);
	    //System.out.println("xCount: " + xCount);
	    //System.out.println("yCount: " + yCount);
	    //System.out.println("Limit: " + limit);
	    
	    int actualCountX = 0;
	    int actualCountY = 0;
	    for (int i = 0; i < a.size(); i++)
	    {
	        if (a.get(i) == x) {
	            actualCountX++;
	            if (actualCountX > limit) {
	                return x;
	            }
	        }
	        if (a.get(i) == y) {
	            actualCountY++;
	            if (actualCountY > limit) {
	                return y;
	            }
	        }
	    }
	    
	    //System.out.println("Actual xCount: " + actualCountX);
	    //System.out.println("Actual yCount: " + actualCountY);
	    
	    return -1;
	}
	
	private int stupidRepeatedNumber(final List<Integer> a) {
	    for (int i = 0; i < a.size(); i++)
	    {
	        int candidate = a.get(i);
	        int count = 0;
	        for (int j = 0; j < a.size(); j++) {
	            if (a.get(j) == candidate)
	            {
	                count++;
	            }
	        }
	        if (count > a.size() / 3)
	        {
	            return candidate;
	        }
	    }
	    return -1;
	}
}
