class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = map(str,digits)
        digits = int("".join(x))
        digits += 1
        x = []
        for i in str(digits):
            x.append(int(i))
        return x