# [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        longest = 0
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    longest = max(longest, i - stack[-1])

        return longest

    def longestValidParenthesesStack(self, s: str) -> int:
        stack = []
        longest = 0
        pairs = []
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append((ch, i))
            elif stack and stack[-1][0] == "(":
                (ch, sid) = stack.pop()
                pairs.append((sid, i))
        pairs = sorted(pairs)
        print(f"{pairs=}")

        cur = None
        for pair in pairs:
            if cur and pair[0] - cur[1] == 1:
                cur = (cur[0], pair[1])
            elif cur and pair[0] > cur[0] and pair[1] < cur[1]:
                continue
            else:
                cur = pair
            if cur and (cur[1] - cur[0] + 1) > longest:
                longest = cur[1] - cur[0] + 1
        return longest


testcases = [
    # "(()",
    # "()",
    # "(",
    # ")()())",
    # "(()())",
    # "",
    # "()()",
    # "()(()",
    # "()(())",
    # "((()))())",
    "()(()",
]


for testcase in testcases:
    print(Solution().longestValidParenthesesStack(testcase))
