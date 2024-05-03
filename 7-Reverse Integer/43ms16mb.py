class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        reversed_num = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            if reversed_num > INT_MAX // 10 or (reversed_num == INT_MAX // 10 and digit > 7):
                return 0
            if reversed_num < INT_MIN // 10 or (reversed_num == INT_MIN // 10 and digit < -8):
                return 0

            reversed_num = reversed_num * 10 + digit

        return sign * reversed_num