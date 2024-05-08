class Solution:
    def reverseWords(self, s: str) -> str:
        x = []
        for i in s.split()[::-1]:
            x.append(i)
        return " ".join(x)