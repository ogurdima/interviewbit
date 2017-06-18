class Solution {
    public string convert(string A, int B) {
        if (B <= 1) {
            return A;
        }
        string result = "";
        for (int i = 0; i < B; i++) {
            string rowString = "";
            int idx = i;
            bool isGrowing = true;
            while (idx < A.Length) {
                if (i == B - 1 && isGrowing) {
                    isGrowing = false;
                    continue;
                }
                if (i == 0 && !isGrowing) {
                    isGrowing = true;
                    continue;
                }
                rowString += A[idx];
                
                if (isGrowing) {
                    int leftTilEnd = B - 1 - i;
                    idx += leftTilEnd + leftTilEnd;
                    isGrowing = false;
                    continue;
                }
                else {
                    int leftTilEnd = i;
                    idx += leftTilEnd + leftTilEnd;
                    isGrowing = true;
                    continue;
                }
            }
            result += rowString;
        }
        
        return result;
        
    }
}
