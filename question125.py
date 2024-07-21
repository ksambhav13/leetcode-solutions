# [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # pattern = re.compile("[\W_]+")
        # stripped = pattern.sub("", s).lower()
        stripped = s.lower()

        i, j = 0, len(stripped) - 1
        while i < j:
            if not stripped[i].isalnum():
                i += 1
                continue
            if not stripped[j].isalnum():
                j -= 1
                continue
            if stripped[i] != stripped[j]:
                return False
            i += 1
            j -= 1
        return True


testcases = [
    "A man, a plan, a canal: Panama",
    "race a car",
    " ",
]

for testcase in testcases:
    print(Solution().isPalindrome(testcase))
