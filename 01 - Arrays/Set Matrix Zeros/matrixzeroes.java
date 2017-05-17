public class Solution {
	public void setZeroes(ArrayList<ArrayList<Integer>> a) {
	    if (a == null)
	    {
	        return;
	    }
	    int m = a.size();
	    if (m == 0)
	    {
	        return;
	    }
	    int n = a.get(0).size();
	    
	   // for (int i = 0; i < m; i++) {
	   //     ArrayList<Integer> row = a.get(i);
	   //     boolean rowMarked = false;
	   //     for (int j = 0; j < n; j++) {
    //             int elem = row.get(j);
    //             if (elem == 0) {
    //                 rowMarked = true;
    //                 // Set whole column to 2s
    //                 // System.out.print("Setting whole column" + j + " to zeroes");
    //                 for (int i2 = 0; i2 < m; i2++) {
    //     	            int elem2 = a.get(i2).get(j);
    //     	            if (elem2 != 0) {
    //                         a.get(i2).set(j, 2);
    //                     }
    // 	            }
    //             }
	   //     }
	   //     if (rowMarked) {
	   //         // set whole row to 2s
	   //         for (int j = 0; j < n; j++) {
    //                 int elem = row.get(j);
    //                 if (elem != 0) {
    //                     row.set(j, 2);
    //                 }
    // 	        }
    	        
	   //     }
	   // }
	    
	    for (int i = 0; i < m; i++) {
	        for (int j = 0; j < n; j++) {
	            int elem = a.get(i).get(j);
	            if (elem == 0) {
	                if (i == 0 && j == 0) {
	                    a.get(0).set(0, 5);
	                }
	                int rowDesignator = a.get(i).get(0);
	                int columnDesignator = a.get(0).get(j);
	                if (rowDesignator == 1) {
	                    a.get(i).set(0, 2);
	                }
	                if (rowDesignator == 3) {
	                    a.get(i).set(0, 5);
	                }
	                if (columnDesignator == 1) {
	                    a.get(0).set(j, 3);
	                }
	                if (columnDesignator == 2) {
	                    a.get(0).set(j, 5);
	                }
	            }
	        }
	    }
	    
	    for (int i = 1; i < m; i++) {
	        int rowDesignator = a.get(i).get(0);
	        if (rowDesignator == 1) {
	            continue;
	        }
	        for (int j = 0; j < n; j++) {
	            a.get(i).set(j, 0);
	        }
	    }
	    
	    for (int j = 1; j < n; j++) {
            int columnDesignator = a.get(0).get(j);
            if (columnDesignator == 1) {
	            continue;
	        }
	        for (int i = 0; i < m; i++) {
	            a.get(i).set(j, 0);
	        }
        }
        
        int corner = a.get(0).get(0);
        if (corner == 1) {
            return;
        }
        if (corner == 0 || corner == 2 || corner == 5)
        {
            for (int j = 1; j < n; j++) {
                a.get(0).set(j, 0);
            }
        }
        if (corner == 0 || corner == 3 || corner == 5)
        {
            for (int i = 1; i < m; i++) {
                a.get(i).set(0, 0);
            }
        }
	    a.get(0).set(0, 0);
	}
}
