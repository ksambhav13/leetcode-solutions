# [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cdict: dict[str, int] = {}
        for c in s:
            cdict[c] = cdict.get(c, 0) + 1
        for c in t:
            val = cdict.pop(c, 0) - 1
            if val < 0:
                return False
            elif val > 0:
                cdict[c] = val
        return False if cdict else True


testcases = [
    "anagram",
    "nagaram",
    "rat",
    "tara",
]

for i in range(0, len(testcases), 2):
    print(Solution().isAnagram(testcases[i], testcases[i + 1]))
