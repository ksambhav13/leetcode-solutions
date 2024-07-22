# [409. Longest Palindrome](https://leetcode.com/problems/longest-palindrome/)


class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars = set()
        pairs = 0
        for c in s:
            if c in chars:
                chars.remove(c)
                pairs += 1
            else:
                chars.add(c)
        return 2 * pairs + (1 if chars else 0)


testcases = [
    "abccccdd",
    "a",
]


for testcase in testcases:
    print(Solution().longestPalindrome(testcase))
