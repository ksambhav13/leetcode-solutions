# [190. Reverse Bits](https://leetcode.com/problems/reverse-bits/)


class Solution:
    def reverseBits(self, n: int) -> int:
        num = 0
        i = 0
        while n > 0:
            i += 1
            num = num * 2 + (n % 2)
            n = n // 2

        while i < 32:
            i += 1
            num *= 2

        return num


testcases = [
    43261596,
    4294967293,
]


for testcase in testcases:
    print(Solution().reverseBits(testcase))
