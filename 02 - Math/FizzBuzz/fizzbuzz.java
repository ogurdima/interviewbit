public class Solution {
    public ArrayList<String> fizzBuzz(int A) {
        ArrayList<String> res = new ArrayList<String>();
        for (int i = 1 ; i <= A; i++)
        {
            String tmp = "";
            if (i % 3 == 0) {
                tmp = tmp + "Fizz";
            }
            if (i % 5 == 0) {
                tmp = tmp + "Buzz";
            }
            if (tmp.isEmpty()) {
                tmp = String.valueOf(i);
            }
            res.add(tmp);
        }
        return res;
    }
}
