# [91. Decode Ways](https://leetcode.com/problems/decode-ways/)


class Solution:
    def numDecodings(self, s: str) -> int:
        nums = [str(i) for i in range(1, 26)]
        self.count = 0

        def dfs(str):
            if not str:
                return True

            v1 = dfs(str[1:]) if str[0] != "0" else False
            v2 = dfs(str[2:]) if str[0:2] in nums else False
            if v1 and v2:
                self.count += 1

            return v1 or v2

        valid = dfs(s)
        if valid:
            return self.count
        else:
            return 0


testcases = [
    "1111",
    "12",
    "226",
    "06",
    "1065",
    "106",
]


for testcase in testcases:
    print(Solution().numDecodings(testcase))
