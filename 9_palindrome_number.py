# [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        num = x
        rev = 0
        while num > 0:
            rev = rev * 10 + (num % 10)
            num = num // 10
        return rev == x


testcases = [
    121,
    -121,
    10,
]


for testcase in testcases:
    print(Solution().isPalindrome(testcase))
