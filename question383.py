# [383. Ransom Note](https://leetcode.com/problems/ransom-note/)


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cdict: dict[str, int] = {}
        for s in magazine:
            cdict[s] = cdict.get(s, 0) + 1
        for s in ransomNote:
            val = cdict.get(s, 0) - 1
            if val < 0:
                return False
            cdict[s] = val
        return True


testcases = [
    "a",
    "b",
    "aa",
    "ab",
    "aa",
    "aab",
]

for i in range(0, len(testcases), 2):
    print(Solution().canConstruct(testcases[i], testcases[i + 1]))
