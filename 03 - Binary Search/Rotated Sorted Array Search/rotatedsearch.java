public class Solution {
	// DO NOT MODIFY THE LIST
	public int search(final List<Integer> a, int b) {
	    if (a.size() == 0) {
	        return -1;
	    }
	    if (a.size() == 1) {
	        if (a.get(0) == b) {
	            return 0;
	        }
	        return -1;
	    }
	    
	    int last = a.size() - 1;
	    int pivotIdx = findPivot(a, 0, last);
	    //System.out.println("Found pivot: [" + pivotIdx + "] = " + a.get(pivotIdx));
	    int leftRes = binarySearch(a, b, 0, pivotIdx - 1);
	    if (leftRes != -1) {
	        //System.out.println("a["+ leftRes+"] = " + a.get(leftRes));
	        return leftRes;
	    }
	    int rightRes = binarySearch(a, b, pivotIdx, last);
	    if (rightRes != -1) {
	        //System.out.println("a["+ rightRes + "] = " + a.get(rightRes));
	    }
	    return rightRes;
	}
	
	private int binarySearch(final List<Integer> a, int target, int left, int right) {
	    int last = right;
	    while (left <= right) {
	        int mid = (left + right) / 2;
	        //System.out.println("|" + left + "|" + mid + "|" + right + "|");
	        //System.out.println("|" + a.get(left) + "|" + a.get(mid) + "|" + a.get(right) + "|");
	        int elem = a.get(mid);
	        if (elem == target) {
	            return mid;
	        }
	        if (elem > target) {
	            right = mid - 1;
	        }
	        else {
	            left = mid + 1;
	        }
	    } 
	    //System.out.println("x["+ mid+"] = " + a.get(mid));
	    if (left <= last && a.get(left) == target) {
	        return left;
	    }
	    return -1;
	}
	
	private int findPivot(final List<Integer> a, int left, int right) {
	    int last = right;
	    int first = left;
	    while (left <= right && a.get(left) > a.get(right)) {
	        int mid = (left + right) / 2;
	        int elem = a.get(mid);
	        if (elem <= a.get(left)) {
	            if (mid == left) {
	                return mid;
	            }
	            if (elem > a.get(mid-1)) {
	                return mid;
	            }
	        }
	        if (elem < a.get(left)) {
	            right = mid - 1;
	        }
	        else {
	            left = mid + 1;
	        }
	    }
	    return left;
	}
	
	
}
