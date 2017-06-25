public class Solution {
    public int findMinXor(ArrayList<Integer> A) {
        Collections.sort(A);
        int minxor = A.get(0) ^ A.get(1);
        for (int i = 0; i < A.size() - 1; i++) {
            int tmp = A.get(i) ^ A.get(i+1);
            if (tmp < minxor) {
                minxor = tmp;
            }
        }
        return minxor;
        
    }
    
}
