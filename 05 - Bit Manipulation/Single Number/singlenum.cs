class Solution {
    public int singleNumber(List<int> A) {
        return A.Aggregate(0, (acc, x) => acc ^ x);
    }
}
