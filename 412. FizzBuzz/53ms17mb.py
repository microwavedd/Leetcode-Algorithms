class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        x = []
        for i in range(1,n + 1):
            if i % 5 == 0 and i % 3 == 0:
                x.append("FizzBuzz")
            elif i % 5  == 0:
                x.append("Buzz")
            elif i % 3 == 0:
                x.append("Fizz")
            else:
                x.append(str(i))
        return x