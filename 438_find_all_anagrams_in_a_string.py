# [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)


from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        p_chars = {}
        for ch in p:
            p_chars[ch] = p_chars.get(ch, 0) + 1
        s_chars = {}

        for i in range(len(s)):
            if i >= len(p):
                s_chars[s[i - len(p)]] = s_chars[s[i - len(p)]] - 1
            s_chars[s[i]] = s_chars.get(s[i], 0) + 1

            is_anagram = True
            for ch, count in p_chars.items():
                if s_chars.get(ch, 0) != count:
                    is_anagram = False
                    break

            if is_anagram:
                res.append(i - len(p) + 1)

        return res


testcases = [
    "cbaebabacd",
    "abc",
    "abab",
    "ab",
]


for i in range(0, len(testcases), 2):
    print(Solution().findAnagrams(testcases[i], testcases[i + 1]))
