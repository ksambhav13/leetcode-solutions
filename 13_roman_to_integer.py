# [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)


class Solution:
    def romanToInt(self, s: str) -> int:
        pre = ""
        vals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        subs = {"V": "I", "X": "I", "L": "X", "C": "X", "D": "C", "M": "C"}

        res = 0

        for ch in s:
            print(f"{pre=}")
            if ch == pre:
                res += vals[ch]
                pre = ""
            elif subs.get(ch, None) == pre:
                res = res - vals[pre] + vals[ch] - vals[pre]
                pre = ""
            else:
                res = res + vals[ch]
            if ch in ("I", "X", "C"):
                pre = ch
        return res


testcases = [
    # "III",
    # "LVIII",
    "MCMXCIV",
]


for testcase in testcases:
    print(Solution().romanToInt(testcase))
