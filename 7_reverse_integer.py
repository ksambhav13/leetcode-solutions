# [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/)


class Solution:
    def reverse(self, x: int) -> int:
        power = 1
        num = 0
        t = abs(x)
        while t > 0:
            num *= 10
            num += t % 10
            power *= 10
            t = t // 10
        if x > 0 and t >= 2**31:
            return 0
        if x < 0 and t > (2**31):
            return 0

        return num if x > 0 else -num


testcases = [
    123,
    -123,
    120,
]


for testcase in testcases:
    print(Solution().reverse(testcase))
