public class Solution {
	public void rotate(ArrayList<ArrayList<Integer>> a) {
	    int n = a.size();

	    for (int rad = 0; rad < n / 2; rad++)
	    {
	        int firstIdx = rad;
	        int lastIdx = n - rad - 1;
	        
	        for (int j = firstIdx; j < lastIdx; j++) {
	            //System.out.println("Iteration");
	            int tmpCur = a.get(firstIdx).get(j);
	            int curX = firstIdx;
	            int curY = j;
	            for (int count = 0; count < 4; count++) {
    	            int targetX = rotateX(curX, curY, n);
    	            int targetY = rotateY(curX, curY, n);
    	            //System.out.println("Moving [" + curX + "][" + curY + "] = " + tmpCur + 
    	            //" to [" + targetX + "][" + targetY + "]");
    	            int tmpNext = a.get(targetX).get(targetY);
    	            a.get(targetX).set(targetY, tmpCur);
    	            tmpCur = tmpNext;
    	            curX = targetX;
    	            curY = targetY;
	            }
	        }
	    }
	    
	}
	
	private int rotateX(int i, int j, int n) {
	    return j;
	}
	
	private int rotateY(int i, int j, int n) {
	    return n - i - 1;
	}
}
