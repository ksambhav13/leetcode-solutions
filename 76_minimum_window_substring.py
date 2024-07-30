# [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)


from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = {}
        for ch in t:
            t_count[ch] = t_count.get(ch, 0) + 1
        s_count = {}
        res, lres = None, len(s)
        matched, total = 0, len(t_count)
        l = 0
        for r in range(len(s)):
            ch = s[r]
            if ch in t_count:
                s_count[ch] = s_count.get(ch, 0) + 1

                if s_count[ch] == t_count[ch]:
                    matched += 1

            while matched == total:
                # update the result
                if (r - l) < lres:
                    res = (l, r)
                    lres = r - l
                # remove from left
                lch = s[l]
                if lch in t_count:
                    s_count[lch] -= 1
                    if s_count[s[l]] < t_count[s[l]]:
                        matched -= 1
                l += 1
        return s[res[0] : res[1] + 1] if res else ""


testcases = [
    "ADOBECODEBANC",
    "ABC",
    "a",
    "a",
    "a",
    "aa",
]

# ADOBE CODEB ANC

for i in range(0, len(testcases), 2):
    print(Solution().minWindow(testcases[i], testcases[i + 1]))
