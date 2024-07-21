# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        # start of substring
        start = 0
        # index of characters last seen
        cdict = dict()
        for i, c in enumerate(s):
            if c in cdict and cdict[c] >= start:
                start = cdict[c] + 1
            res = max(res, i - start + 1)
            cdict[c] = i
        return res

    def lengthOfLongestSubstringStringManipulation(self, s: str) -> int:
        res = 0
        cur = ""
        for c in s:
            try:
                index = cur.index(c)
                cur = cur[index + 1 :]
            except ValueError:
                pass
            cur = cur + c
            if len(cur) > res:
                res = len(cur)
        return res


testcases = [
    "abcabcbb",
    "bbbbb",
    "pwwkew",
    " ",
]

for testcase in testcases:
    print(Solution().lengthOfLongestSubstring(testcase))
