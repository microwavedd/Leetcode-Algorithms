public class Solution {
    public int[] PlusOne(int[] digits) {
        for (int i=digits.Length-1; i>=0; i--) {
            digits[i] = ++digits[i] % 10;
            if (digits[i] != 0) {
                return digits;
            }
        }
        
        int[] result = new int[] {1};
        return result.Concat(digits).ToArray();
    }
}