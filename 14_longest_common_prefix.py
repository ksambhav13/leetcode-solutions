# [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)


from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        lenp = len(prefix)
        for i in range(1, len(strs)):
            lenp = min(lenp, len(strs[i]))
            for j in range(lenp):
                if prefix[j] != strs[i][j]:
                    lenp = j
                    break
        return prefix[0:lenp]


testcases = [
    ["flower", "flow", "flight"],
    ["dog", "racecar", "car"],
    ["ab", "a"],
]


for testcase in testcases:
    print(Solution().longestCommonPrefix(testcase))
