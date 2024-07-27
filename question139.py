# [139. Word Break](https://leetcode.com/problems/word-break/)


from collections import deque
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True
        for si in range(n - 1, -1, -1):
            for word in wordDict:
                if si + len(word) <= n and s[si : si + len(word)] == word:
                    si[i] = dp[i + len(word)]
                if dp[i]:
                    break
        return dp[0]

        def dp(si):
            if si == n:
                return True
            if si in cache:
                return cache[si]
            result = False
            for word in wordDict:
                if si + len(word) <= n and s[si : si + len(word)] == word:
                    result = result or dp(si + len(word))
            cache[si] = result
            return result

        cache = {}
        return dp(0)

    def wordBreakRecursive(self, s: str, wordDict: List[str]) -> bool:
        def dp(si):
            if si == n:
                return True
            if si in cache:
                return cache[si]
            result = False
            for word in wordDict:
                if si + len(word) <= n and s[si : si + len(word)] == word:
                    result = result or dp(si + len(word))
            cache[si] = result
            return result

        n = len(s)
        cache = {}
        return dp(0)


testcases = [
    "leetcode",
    ["leet", "code"],
    "applepenapple",
    ["apple", "pen"],
    "catsandog",
    ["cats", "dog", "sand", "and", "cat"],
    "aaaaaaa",
    ["aaaa", "aaa"],
    "cars",
    ["car", "ca", "rs"],
]

for i in range(0, len(testcases), 2):
    print(Solution().wordBreak(testcases[i], testcases[i + 1]))
