# [338. Counting Bits](https://leetcode.com/problems/counting-bits/)


from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        res = [0 for _ in range(n + 1)]
        cur = 1
        for i in range(1, n + 1):
            if i < cur * 2:
                res[i] = 1 + res[i - cur]
            else:
                cur = i
                res[i] = 1
        return res


testcases = [0, 1, 2, 5, 16]


for testcase in testcases:
    print(Solution().countBits(testcase))
