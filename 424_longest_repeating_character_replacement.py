# [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ch_count = {}
        l, r = 0, 0
        res = 0
        max_freq = 0
        for r in range(len(s)):
            ch_count[s[r]] = ch_count.get(s[r], 0) + 1
            max_freq = max(max_freq, ch_count[s[r]])
            while (r - l + 1) - max_freq > k:
                ch_count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res


testcases = [
    "ABAB",
    2,
    "AABABBA",
    1,
]


for i in range(0, len(testcases), 2):
    print(Solution().characterReplacement(testcases[i], testcases[i + 1]))
