public class Solution {
	public void arrange(ArrayList<Integer> a) {
	    int N = a.size();
	    
        for (int i = 0; i < N; i++) {
            int pointedOldVal = a.get(a.get(i)) % N;
            int combinedVal = a.get(i) + pointedOldVal * N;
            a.set(i, combinedVal);
        }
        
        for (int i = 0; i < N; i++) {
            int combinedVal = a.get(i);
            int newVal = combinedVal / N;
            a.set(i, newVal);
        }
    
	    
	}
}
