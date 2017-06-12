class Solution {
    public int solve(string A) {
        if (A.Length <= 1) {
            return 0;
        }
        int i = 0;
        for (i = A.Length - 1; i > 0; i--) {
            int len = i + 1;
            if (isPalindrom(A.Substring(0,len))) {
                break;
            }
        }
        
        if (i == A.Length - 1) {
            return 0;
        }
        
        int firstBreakingIndex = i + 1;
        
        return A.Length - firstBreakingIndex;
    }
    
    private bool isPalindrom(string s) {
        string r = Reverse(s);
        return s == r;
    }
    
    private static string Reverse( string s )
    {
        char[] charArray = s.ToCharArray();
        Array.Reverse( charArray );
        return new string( charArray );
    }
}
