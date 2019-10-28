import sys

class Solution:
    def reverse(self, x: int) -> int:
        rev: int = 0
        while x != 0:
            pop: int = x % 10
            x //= 10
            if (rev > (2147483647 / 10)) or (rev == 2147483647 and pop > 7):
                return 0
            if (rev < (-2147483648 / 10)) or (rev == -2147483648 and pop < -8):
                return 0
            rev = rev * 10 + pop
        return rev
       

print(Solution().reverse(123))
