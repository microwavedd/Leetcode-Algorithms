public class Solution {
    public bool IsPalindrome(string s) {
        List<char> y = new List<char>();
        foreach (char c in s) {
            if (char.IsLetterOrDigit(c)) {
                y.Add(char.ToLower(c));
            }
        }
        string str = new string(y.ToArray());
        return str == new string(str.Reverse().ToArray());
    }
}