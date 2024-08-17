# [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n % 2
            n = n // 2
        return count


testcases = [
    11,
    128,
    2147483645,
]


for testcase in testcases:
    print(Solution().hammingWeight(testcase))
