# [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)


from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            ss = "".join(sorted(s))
            res[ss].append(s)
        return res.values()


testcases = [
    ["eat", "tea", "tan", "ate", "nat", "bat"],
    [""],
    ["a"],
]


for testcase in testcases:
    print(Solution().groupAnagrams(testcase))
