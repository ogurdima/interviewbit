public class Solution {
	// DO NOT MODIFY THE LIST
	public ArrayList<Integer> searchRange(final List<Integer> a, int b) {
	    ArrayList<Integer> result = new ArrayList<Integer>();
	    
	    int left = 0;
	    int right = a.size() - 1;
	    int mid = 0;
	    while(left < right) {
	        mid = (left + right) / 2;
	        if (mid == left || mid == right) {
	            break;
	        }
	        int elem = a.get(mid);
	        if (elem < b) {
	            left = mid;
	            continue;
	        }
	        if (elem == b && (mid == 0 || a.get(mid-1) != b)) {
	            break;
	        }
            right = mid;
            continue;
	        
	    }
	    int leftIndex = -1;
	    if (a.get(mid) != b) {
	        result.add(0, -1);
	        result.add(1, -1);
	        return result;
	    }
	    leftIndex = mid;
	    
	    left = 0;
	    right = a.size() - 1;
	    mid = 0;
	    while(left < right) {
	        mid = (left + right) / 2;
	        if (mid == left) {
	            mid++;
	        }
	        if (mid == right) {
	            //System.out.println("l:"+left+"m:"+mid+"r:"+right);
	            break;
	        }
	        int elem = a.get(mid);
	        if (elem > b) {
	            right = mid;
	            continue;
	        }
	        if (elem == b && (mid == a.size() - 1 || a.get(mid+1) != b)) {
	            //System.out.println("mid: "+mid+" next: " + a.get(mid+1));
	            break;
	        }
            left = mid;
            continue;
	    }
	    
	    if (a.get(mid) != b) {
	        result.add(0, -1);
	        result.add(1, -1);
	        return result;
	    }
	    
        result.add(0, leftIndex);
	    result.add(1, mid); 
	    
	    return result;
	}
}
