public class Solution {
    public int solve(ArrayList<Integer> A, int B, int C) {
        int lenC = 0;
        int tmp = C;
        while(tmp > 0) {
            lenC++;
            tmp /= 10;
        }
        int totalDigits = A.size();
        if (totalDigits == 0 || B > lenC) {
            return 0;
        }
        if (B == 1) {
            int ok = 0;
            for (int i = 0; i < totalDigits; i++) {
                if (A.get(i) < C) {
                    ok++;
                }
            }
            return ok;
        }
        if (B < lenC) {
            if (A.get(0) == 0) {
                return (totalDigits-1) * (int)Math.pow(totalDigits, B-1); 
            }
            return (int)Math.pow(totalDigits, B);
        }
        
        ArrayList<Integer> digit = new ArrayList<Integer>(lenC);
        ArrayList<Boolean> haveSameFirstAsC = new ArrayList<Boolean>(lenC);
        ArrayList<Boolean> digitExistsInSet = new ArrayList<Boolean>(10);
        
        ArrayList<Integer> results = new ArrayList<Integer>(lenC);
        
        
        
        for (int i = 0; i < lenC; i++) {
            haveSameFirstAsC.add(i, false);
            digit.add(i, 0);
            results.add(i, 0);
        }
        
        for (int i = 0; i < 10; i++) {
            digitExistsInSet.add(i, false);
        }
        
        for (int i = 0; i < totalDigits; i++) {
            digitExistsInSet.set(A.get(i), true);
        }
        
        
        //System.out.println("lenC is: " + lenC);
        tmp = C;
        for (int i = lenC - 1; i >= 0; i--) {
            //System.out.println("tmp is: " + tmp);
            digit.set(i, tmp % 10);
            tmp /= 10;
        }
        
        // System.out.println("digit:");
        // for (int i = 0; i < lenC; i++) {
        //     System.out.println(digit.get(i) + ",");
        // }
        
        for (int i = 0; i < lenC; i++) {
            if (i > 0 && haveSameFirstAsC.get(i-1) == false) {
                haveSameFirstAsC.set(i, false);
                continue;
            }
            if (digitExistsInSet.get(digit.get(i))) {
                haveSameFirstAsC.set(i, true);
            }
        }
        
        // System.out.println("haveSameFirstAsC:");
        // for (int i = 0; i < lenC; i++) {
        //     System.out.println(haveSameFirstAsC.get(i) + ",");
        // }
        
     
        
        for (int i = 0; i < totalDigits; i++) {
            if (A.get(i) < digit.get(0) && A.get(i) != 0) {
                int oldres = results.get(0);
                results.set(0, oldres + 1);
            }
        }
        
        //System.out.println("results[0] = " + results.get(0));
        
        for (int i = 1; i < lenC; i++) {
            results.set(i, results.get(i-1) * totalDigits);
            if (haveSameFirstAsC.get(i-1)) {
                for (int j = 0; j < totalDigits; j++) {
                    if (A.get(j) < digit.get(i)) {
                        int oldres = results.get(i);
                        results.set(i, oldres + 1);
                    }
                }
            }
        }
        

        
        return results.get(lenC-1);
        
        
    }
}
