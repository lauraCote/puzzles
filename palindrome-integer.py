class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        number = x
        reverseNumber: int = 0

        while x != 0:
            pop = x % 10
            x //= 10
            reverseNumber = reverseNumber * 10 + pop

        return reverseNumber == number

print(Solution().isPalindrome(10))