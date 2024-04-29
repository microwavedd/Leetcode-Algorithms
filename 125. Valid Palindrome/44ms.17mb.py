class Solution:
    def isPalindrome(self, s: str) -> bool:
        y = [i for i in s if i.isalpha() or i.isnumeric()]
        return "".join(y).lower() == "".join(y).lower()[::-1]