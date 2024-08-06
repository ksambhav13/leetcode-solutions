# [874. Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_next_characher(inp, end):
            bs = 0
            while end >= 0:
                if inp[end] == "#":
                    bs += 1
                elif bs > 0:
                    bs -= 1
                else:
                    break
                end = end - 1
            return end

        ps, pt = len(s) - 1, len(t) - 1
        while ps >= 0 or pt >= 0:
            ps = get_next_characher(s, ps)
            pt = get_next_characher(t, pt)
            if ps < 0 and pt < 0:
                return True
            if ps < 0 or pt < 0:
                return False
            if s[ps] != t[pt]:
                return False
            ps -= 1
            pt -= 1
        return True

    def backspaceCompareStack(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        for ch in s:
            if ch == "#":
                stack_s and stack_s.pop()
            else:
                stack_s.append(ch)
        for ch in t:
            if ch == "#":
                stack_t and stack_t.pop()
            else:
                stack_t.append(ch)
        if len(stack_s) != len(stack_t):
            return False
        return stack_s == stack_t


testcases = [
    "ab#c",
    "ad#c",
    # "ab##",
    # "c#d#",
    # "a#c",
    # "b",
    # "y#fo##f",
    # "y#f#o##f",
]


for i in range(0, len(testcases), 2):
    print(Solution().backspaceCompare(testcases[i], testcases[i + 1]))
